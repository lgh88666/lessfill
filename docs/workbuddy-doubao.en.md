# Getting started with WorkBuddy / Doubao desktop

[简体中文](workbuddy-doubao.md) · [English](workbuddy-doubao.en.md) · [Back to README](../README.en.md)

Import the skill through the app, then give a work task your resume, optional photo, and application URL. Personal information stays in your private working directory; the packages contain no real resumes or credentials.

## Pick a package

|File|Purpose|
|---|---|
|[lessfill-workbuddy.zip](https://github.com/lgh88666/lessfill/releases/download/v0.1.0-preview.1/lessfill-workbuddy.zip)|A WorkBuddy import package with its documented name, bilingual descriptions, and version fields|
|[lessfill-skill.zip](https://github.com/lgh88666/lessfill/releases/download/v0.1.0-preview.1/lessfill-skill.zip)|Standard skill instructions and resources for import/creation tools that accept this structure|

Each archive has `SKILL.md`, `references/`, `examples/`, and the license at its root. It does not contain the entire repository, artwork, or Git history. Download the named Release asset; GitHub's automatic Source code ZIP has a different structure.

## WorkBuddy

1. Open Skills. Depending on the version, this may be under Experts · Skills · Connectors.
2. Choose Add Skill → Upload Skill, select `lessfill-workbuddy.zip`, and keep the imported skill enabled.
3. Start a work task in a private writable directory. Provide your resume, optional photo, and job link.
4. Ask the agent to check actual webpage editing, file upload, and local persistence capabilities first. A working host-provided browser does not need an extra Jev/Playwright connection.

The import steps follow [WorkBuddy's official skills guide](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market); package metadata follows its [open-platform skill structure](https://open.workbuddy.cn/docs/skill). This package has not been imported and used for a real application in your WorkBuddy client; packaging to the documented format is not completed compatibility verification.

## Doubao desktop: Work Tasks / Skills

This refers to the desktop Work Tasks / Skills entry, not ordinary chat. Public official documentation did not provide enough detail to verify local ZIP import steps for every version, so unverified button names are not prescribed here.

- **Your version has local skill import:** Select `lessfill-skill.zip` and check that both `SKILL.md` and its supporting resources are recognized.
- **It offers skill creation / resource attachment instead:** Extract the general package and provide the entry instructions and complete resource directory to that flow. Proceed only if the tool can actually read them; pasting a summary is not a completed installation.
- **Neither entry is available:** If Work Tasks can read local files, provide the extracted directory and ask it to read `SKILL.md`. Without file access and webpage tools, it can help organize information but cannot be assumed to fill forms or upload files.

For import errors, unreadable resources, or missing webpage tools, share a redacted screenshot and error message to help document that version. Do not include real resumes, credentials, or screenshots exposing login secrets.

## Start with this prompt

```text
Use LessFill (resume-autofill) to fill this application: <application URL>
Resume: <path or attached file>
Photo: <path or attached file; optional>

Prefer webpage tools already authorized for this work task.
First confirm you can edit fields and upload files.
You may enter these details on the site, upload my resume and photo,
and save a draft. Do not submit the application.
Ask about missing facts together. Save my confirmed reusable facts
to my private profile and reuse them next time.
On first use, create a private Feishu tracker through the browser,
then keep using that same table.
```

To use Feishu MCP, change the last sentence to use your already connected MCP server. You can also disable tracking. This choice is independent of the browser route.

You still handle login, CAPTCHAs, final review, and submission. If a step is unavailable, the agent should report it clearly and preserve the page rather than claiming everything is complete.
