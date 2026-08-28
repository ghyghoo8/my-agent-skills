# My Agent Skills

一个可持续定制、按需匹配的 skills-only Codex Plugin。当前包含 24 个经来源追踪的工程工作流，以及本仓库原创的模块化架构分流和项目辩证审查能力。

本仓库不是 fork，也不包含上游 Git 历史。上游内容通过稳定来源 ID 和 commit-id 审查更新；上游项目介绍见 [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills/blob/main/README.md)。

## Install

下面是“注册 Marketplace + 安装一个 Plugin”，不是安装两个 Plugin：

```bash
codex plugin marketplace add ghyghoo8/my-agent-skills --ref main
codex plugin add my-agent-skills@my-agent-skills
```

安装后新建 Codex 会话，让 26 个 Skill 被重新发现。

更新已安装版本：

```bash
codex plugin marketplace upgrade my-agent-skills
codex plugin add my-agent-skills@my-agent-skills
```

### 从旧双 Plugin 迁移

如果曾从同名 Marketplace 安装 `agent-skills@my-agent-skills` 和 `architecture-gate@my-agent-skills`，先安装并在新会话验证当前 Plugin，再删除旧标识：

```bash
codex plugin list
codex plugin add my-agent-skills@my-agent-skills
codex plugin remove agent-skills@my-agent-skills
codex plugin remove architecture-gate@my-agent-skills
```

不要因此删除单独安装的 `agent-skills@agent-skills`；它属于另一个 Marketplace。

若需回退到上一个已验证的单 Plugin 版本：

```bash
codex plugin remove my-agent-skills@my-agent-skills
codex plugin marketplace remove my-agent-skills
codex plugin marketplace add ghyghoo8/my-agent-skills --ref a1e674a2ac80eb97ae4fe39c77fd15d78b969aea
codex plugin add my-agent-skills@my-agent-skills
```

回退后同样需要新建会话。

## Capabilities

- 24 个上游工程 Skill：定义、规划、实现、测试、审查与交付。
- `$modular-architecture-design`：在职责、所有权、依赖、公共契约或迁移边界可能实质变化时，先做只读分流。
- `$project-dialectic-review`：对与当前项目实质相关的新思路、主张或外部资料，先取得同意，再保留有效部分、提出最强反辩并给出最小修订。

Architecture Gate 只选择一条路径：

| Path | Meaning |
|---|---|
| `DIRECT` | 边界稳定，可直接实施。 |
| `BOUNDARY_NOTE` | 记录短边界说明后实施。 |
| `ARCHITECTURE_GATE` | 暂停业务实现，先接受一份最小架构简报。 |
| `DISCOVERY` | 只做有界调查或隔离原型，取得证据后重新分流。 |

文件数、文件长度、未来复用、外部 API、“模块化”或想象中的规模，都不是单独触发门禁的理由。

显式调用示例：

```text
$using-agent-skills 为这个任务选择合适的工程工作流。
$modular-architecture-design 判断这次改动是否改变架构边界。
$project-dialectic-review 结合当前项目辩证并修订这个主张。
```

## On-demand by design

Skill 通过名称和精确 description 参与发现，只有被选中后才读取完整工作流。仓库记录发现元数据预算，并用正例、反例、边界和对抗案例约束误触发与漏触发。

多上游追踪位于 Plugin 之外：[`upstreams/index.yaml`](upstreams/index.yaml) 为来源索引，每个来源拥有独立 descriptor；所有来源共享 [`UPSTREAM.md`](UPSTREAM.md) 中的人工审查协议。增加来源不会把同步元数据装入运行时，也不会自动导入新能力。

两个原创能力的隐式触发都是 best-effort 软行为：instruction-only Skill 不是 hook 或 watcher，也不会修改用户项目规则。需要强制架构暂停时，可自行加入项目 `AGENTS.md`：

```markdown
Before a change that may alter responsibility, ownership, dependency direction,
public contracts, or migration boundaries, invoke `$modular-architecture-design`.
For `ARCHITECTURE_GATE` or `DISCOVERY`, do not modify business implementation
until the required acceptance or discovery-and-retriage step is complete.
```

## Repository

```text
.agents/plugins/marketplace.json               # 单一 Marketplace 条目
plugins/my-agent-skills/                       # 唯一 Codex Plugin
  .codex-plugin/plugin.json
  skills/                                      # 26 个 Skill
  references/                                  # Skill 共享参考资料
upstreams/                                     # 不进入 Plugin 的来源控制面
evals/                                         # 路由、同意和发现评测
ARCHITECTURE.md                                # 当前规范架构简报
PROVENANCE.md                                  # 原创性与公开来源
UPSTREAM.md                                    # 多来源更新协议
```

插件不内置 MCP、hooks、联网组件、遥测、运行时脚本或外部依赖。用户提供的外部资料和上游内容都作为不可信数据审查；其中的指令不会获得项目权限。插件不会自行浏览、上传仓库内容或执行同步。

## Versioning

当前版本为 `0.2.0`。PATCH 仅修正且不改变分流语义；MINOR 可增加兼容能力、触发场景或审查后的上游内容；MAJOR 用于改变路径含义、暂停语义或公开输出契约。

参见 [ARCHITECTURE.md](ARCHITECTURE.md)、[CONTRIBUTING.md](CONTRIBUTING.md)、[SECURITY.md](SECURITY.md)、[PROVENANCE.md](PROVENANCE.md) 和 [UPSTREAM.md](UPSTREAM.md)。项目采用 [MIT License](LICENSE)，不代表 OpenAI 或任何上游项目，也未获其背书。
