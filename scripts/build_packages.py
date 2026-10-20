"""Build private-data-free general and WorkBuddy skill import archives."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def workbuddy_entry(original: str, version: str) -> str:
    frontmatter, body = original.removeprefix("---\n").split("\n---\n", 1)
    description = next(line.split(":", 1)[1].strip() for line in frontmatter.splitlines()
                       if line.startswith("description:"))
    fields = {
        "name": "resume-autofill",
        "display_name": "LessFill · 网申填写助手",
        "display_name_en": "LessFill",
        "description": description,
        "description_zh": description,
        "description_en": "Fill job applications from a resume, upload authorized attachments, save drafts, and maintain a private Feishu tracker. Do not submit applications.",
        "version": version,
        "author": "lgh88666",
        "license": "MIT",
    }
    header = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    resources = "\n\n## WorkBuddy 资源读取\n\n按任务需要读取对应资源，不一次加载全部文件：\n"
    resources += "\n".join(f"- @references/{name}.md" for name in (
        "setup", "host-browser", "files", "feishu", "agent-integration",
        "edge-playwright", "chrome-jev"))
    return "---\n" + header + "\n---\n" + body + resources + "\n"


def build(source: Path, output: Path, version: str) -> None:
    allowed_dirs = {"references", "examples"}
    files = sorted(p for p in source.rglob("*") if p.is_file() and (
        p.relative_to(source).as_posix() in {"SKILL.md", "LICENSE.txt"}
        or p.relative_to(source).parts[0] in allowed_dirs))
    for item in files:
        if item.is_symlink() or not item.resolve().is_relative_to(source.resolve()):
            raise ValueError("Package source must not contain links outside the skill directory.")
        if item.suffix not in {".md", ".json", ".txt"}:
            raise ValueError(f"Unexpected package file: {item.name}")
    output.mkdir(parents=True, exist_ok=True)
    checksums = []
    for name, workbuddy in (("lessfill-skill.zip", False), ("lessfill-workbuddy.zip", True)):
        target = output / name
        with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for item in files:
                relative = item.relative_to(source).as_posix()
                content = item.read_text(encoding="utf-8")
                if workbuddy and relative == "SKILL.md":
                    content = workbuddy_entry(content, version)
                info = ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, content.encode("utf-8"))
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        checksums.append(f"{digest}  {name}")
        print(f"Built {target.name}: {len(files)} files, {target.stat().st_size} bytes")
    (output / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="0.1.0")
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    arguments = parser.parse_args()
    if not re.fullmatch(r"\d+\.\d+\.\d+", arguments.version):
        parser.error("--version must have the form 0.1.0")
    repository = Path(__file__).resolve().parent.parent
    build(repository / "resume-autofill", arguments.output_dir.resolve(), arguments.version)


if __name__ == "__main__":
    main()
