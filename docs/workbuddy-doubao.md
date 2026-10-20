# WorkBuddy／豆包电脑版上手

[简体中文](workbuddy-doubao.md) · [English](workbuddy-doubao.en.md) · [返回首页](../README.md)

从界面导入技能，然后把简历、照片和招聘链接交给工作任务。个人资料留在你的私人工作目录，安装包里不包含任何真实简历或登录凭据。

## 先下载哪个包

|文件|用途|
|---|---|
|[lessfill-workbuddy.zip](https://github.com/lgh88666/lessfill/releases/download/v0.1.0-preview.1/lessfill-workbuddy.zip)|按 WorkBuddy 公开技能字段补齐名称、双语简介和版本的导入包|
|[lessfill-skill.zip](https://github.com/lgh88666/lessfill/releases/download/v0.1.0-preview.1/lessfill-skill.zip)|标准 `SKILL.md` 指令与资源包；适用于接受该结构的技能导入/创建入口|

包内根目录包含 `SKILL.md`、`references/`、`examples/` 和许可证，不包含整个 GitHub 仓库、图片或 `.git` 历史。请下载 Release 的具体附件，不把 GitHub 自动生成的 Source code ZIP 当作同一个导入包。

## WorkBuddy

1. 打开 WorkBuddy 的技能板块。不同版本可能显示为「技能」或「专家·技能·连接器 → 技能」。
2. 选择「添加技能 → 上传技能」，上传 `lessfill-workbuddy.zip`，确认导入后保持启用。
3. 新建工作任务，选择一个可读写的私人工作目录，提供简历文件、可选照片和网申链接。
4. 让 Agent 先检查当前任务的网页编辑、文件上传与本地保存能力；根据实际能力执行，不先要求安装 Jev/Playwright。

以上导入入口依据 [WorkBuddy 官方技能说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)；包的元信息依据 [开放平台技能结构](https://open.workbuddy.cn/docs/skill)。本项目未在你的 WorkBuddy 客户端实际导入和投递，不把按格式打包等同于兼容性已验证。

## 豆包电脑版工作任务技能

这里指豆包电脑版的「工作任务／技能」入口，不是普通聊天窗口。当前公开官方资料未提供足够细节来核实各版本的本地 ZIP 导入步骤，因此不写死未经核实的按钮名称。

- **当前版本提供本地技能包导入**：选择通用 `lessfill-skill.zip`，检查是否能正确识别 `SKILL.md` 及附带参考文件。
- **当前版本提供创建技能／添加资源**：先解压通用包，将入口说明和完整资源目录交给其创建流程；只有该入口能读取这些文件时才继续，不只粘贴一段简介就声称安装完成。
- **当前版本没有上述入口**：若工作任务支持读取本地文件，可把解压目录路径发给它，要求读取 `SKILL.md` 后执行。没有文件和网页工具时只能做资料整理，无法保证自动填表或上传。

如果看到导入格式错误、资源读取失败或网页工具缺失，请提供脱敏后的界面和错误提示，便于补充对应版本说明。请勿附真实简历、密钥或登录状态截图。

## 复制这段开始

```text
使用 LessFill（resume-autofill）填写这个网申：<招聘网址>
简历：<路径或已上传文件>
照片：<路径或已上传文件，可选>

优先使用当前工作任务已授权的网页工具；请先确认能编辑字段和上传附件。
允许把这些资料填入该网站、上传简历和照片并保存草稿，不提交申请。
缺少信息时集中问我；我确认的长期事实写回私人个人信息文档，下次复用。
首次请创建私有飞书投递表，使用浏览器操作，以后复用同一张表。
```

若想使用飞书 MCP，把最后一句改成“飞书使用我已接入的 MCP”；也可以说“暂不登记飞书”。这些选择互不绑定。

登录、验证码、最终内容检查和申请提交仍由你处理。Agent 无法操作某个环节时应清楚报告并保留现场，而非宣称全部完成。
