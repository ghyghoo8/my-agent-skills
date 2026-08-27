# My Agent Skills

一个全新的、skills-only 的 Codex Plugin：在同一个插件中提供 24 个经来源追踪的工程工作流，以及本仓库原创的模块化架构分流能力。

本仓库不是 fork，不包含上游 Git 历史。上游内容以 commit-id 快照追踪；完整的上游介绍请见 [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills/blob/main/README.md)。

## Install

```bash
# 首次使用时注册一次 Marketplace
codex plugin marketplace add ghyghoo8/my-agent-skills --ref main

# 安装唯一的 Plugin
codex plugin add my-agent-skills@my-agent-skills
```

安装后新建 Codex 会话，让 25 个 Skill 被重新发现。后续获取仓库更新：

```bash
codex plugin marketplace upgrade my-agent-skills
codex plugin add my-agent-skills@my-agent-skills
```

## What It Contains

- 24 个来自上游快照的工程 Skill，覆盖定义、规划、实现、测试、审查与交付。
- `$modular-architecture-design`：在职责、所有权、依赖方向、公共契约或迁移边界可能实质变化时，先做只读、证据驱动的分流。

Architecture Gate 只选择一条路径：

| Path | Meaning |
|---|---|
| `DIRECT` | 边界稳定，可直接实施。 |
| `BOUNDARY_NOTE` | 记录简短边界说明后实施。 |
| `ARCHITECTURE_GATE` | 暂停业务实现，先接受一份最小架构简报。 |
| `DISCOVERY` | 只做有界调查或隔离原型，取得证据后重新分流。 |

文件数、文件长度、未来复用、外部 API、用户说“模块化”或想象中的规模，都不是单独触发架构门禁的理由。

显式调用示例：

```text
$using-agent-skills 为这个任务选择合适的工程工作流。
$modular-architecture-design 在实现前判断这次改动是否改变架构边界。
```

## Soft Gate

`modular-architecture-design` 默认允许隐式调用，但它仍是软门禁。插件不会自动修改用户项目规则。需要强制暂停时，可自行把以下片段加入项目 `AGENTS.md`：

```markdown
Before a change that may alter responsibility, ownership, dependency direction,
public contracts, or migration boundaries, invoke `$modular-architecture-design`.
For `ARCHITECTURE_GATE` or `DISCOVERY`, do not modify business implementation
until the required acceptance or discovery-and-retriage step is complete.
```

## Repository

```text
.agents/plugins/marketplace.json          # 单一 Marketplace 条目
plugins/my-agent-skills/                  # 唯一 Codex Plugin
  .codex-plugin/plugin.json
  skills/                                 # 25 个 Skill
  references/                             # Skill 共享参考资料
evals/architecture-gate/cases.yaml        # 架构分流评测
PROVENANCE.md                              # 来源 commit-id 与适配边界
UPSTREAM.md                                # 后续 diff 更新流程
```

插件本身不内置 MCP、hooks、联网组件、遥测、运行时脚本或外部依赖，也不会自行上传仓库内容。需要检索资料的 Skill 只使用宿主已经提供且用户允许的能力；`browser-testing-with-devtools` 只有在用户另行配置 Chrome DevTools MCP 后才能使用浏览器能力，插件不会替用户安装或配置它。

评测关注路径选择、停写边界、证据使用和拒绝投机抽象，不测试固定措辞。详见 [evals/README.md](evals/README.md)。

## Versioning and Contribution

当前版本为 `0.1.0`。PATCH 仅用于不改变行为语义的修正；MINOR 用于兼容的新能力、Skill 或上游快照更新；MAJOR 用于改变路径含义、暂停语义或其他公开输出契约。

参见 [CONTRIBUTING.md](CONTRIBUTING.md)、[SECURITY.md](SECURITY.md)、[PROVENANCE.md](PROVENANCE.md) 和 [UPSTREAM.md](UPSTREAM.md)。项目采用 [MIT License](LICENSE)，不代表 OpenAI 或上游项目官方产品，也未获其背书。
