# Skill 行为与模型执行评测 — 2026-09-10

交付候选版本：**4.1.0**。当前评测状态：**READY**。完整机器记录见 [results-2026-09-10.json](results-2026-09-10.json)。

原始基线保持为 4.0.0 的 27 条规划案例与 46 条路由案例，共 73 条；已获得 73 条独立模型响应、73 条独立评分。修补后的当前案例库包含 27 条规划、49 条路由和 21 条架构案例；新增覆盖与复测单独计数。

## 方法与边界

每条行为案例使用新的 Astra ultra 上下文，只给原始请求、最小项目事实和冻结的 Skill 内容；执行者没有收到预期答案或评分断言。独立 Astra ultra 评分者逐项对照原始断言与保存的响应、轨迹及产物。现实项目写入、派发、浏览器或集成检查在该环境中不可观察时记为 UNOBSERVABLE，不由计划文本代替。

跨模型执行采用相同的权威文档、详细开发指引、明确 Roadmap 和任务卡。五个认可组合各运行库存事务、投递对账、回归测试编写三个本地 Python 任务，每个组合每题一次。执行者可做自测；独立检查和最终审查归 Astra ultra。固定随机顺序种子为 20260910。

模型请求参数与 CLI 实际回执分别保存，检查 exact model/effort 生效组合。没有使用 Luna、medium、经济档、max 替代，也没有因成本、速度或失败切换模型。运行耗时和 CLI 报告 token 保留于机器记录，不作为价格或受控性能结论。

## 行为结果

| 基线套件 | 已完成响应 | 已评分 | 首轮结果 |
|---|---:|---:|---|
| planning-and-task-breakdown | 27/27 | 27 | PASS 20, INCONCLUSIVE 7 |
| discovery | 46/46 | 46 | PASS 38, INCONCLUSIVE 5, FAIL 3 |

原始失败或无法判定的结果不覆盖：

| 案例 | 首轮 | 最新补充结果 | 处理 |
|---|---|---|---|
| p05 / near-term-cards-are-executable-without-speculative-detail | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p17 / planner-technical-decisions-remain-subordinate-to-authority | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p22 / missing-authority-requires-prerequisite-preparation | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p23 / missing-development-document-requires-preparation | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p25 / missing-roadmap-requires-prerequisite-preparation | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p26 / vague-phase-list-is-not-explicit-milestone-roadmap | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| p27 / sufficient-three-document-baseline-proceeds-without-reconfirmation | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| d14 / negative-summary-only-external-material | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| d17 / boundary-two-modules-stable-responsibilities | FAIL | PASS | 修正架构/API 路由交接，使用新冻结候选版本复测 |
| d22 / boundary-decline-is-not-reasked | FAIL | PASS | 明确 owner 与查阅记录的轨迹含义；原案例与 Skill 不变 |
| d29 / negative-capability-status-query | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| d38 / positive-authority-grounded-milestone-roadmap | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| d43 / boundary-roadmap-request-with-undefined-behavior | FAIL | PASS | 独立仲裁后修正过严的唯一 owner 断言；原请求、事实与 Skill 保持不变 |
| d45 / boundary-milestone-entry-needs-detailed-development-document | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |
| d46 / boundary-milestone-entry-needs-explicit-roadmap | INCONCLUSIVE | PASS | 补充缺少的项目事实，原请求与断言不变 |

规划 p05 补充已接受的契约、里程碑退出条件和职责；p17 补充可选实现组合、责任人、夹具和命令；路由 d14 补上被摘要的文章及其引用式指令文本。p22 补充相互冲突的权威候选内容，p23 补充开发文档所需的现有源文件职责、接口、验收和命令；p25–p27 补充形成或细化具体 Roadmap/任务卡所需的同类事实，并保留各自缺失、笼统或已充分的 Roadmap 条件。d29 补充状态查询所需的权属登记和当前观测回执，d38 补充产品任务推导所需的既有契约和 Roadmap 内容；d45、d46 补充修复开发文档或 Roadmap 所需的同类内容，保留原本不充分的文档条件。这些都是输入不充分，不能算作已证实的 Skill 缺陷。

路由 d17 暴露真实的发现与交接冲突：稳定 owner 的内部契约变化被 API Skill 接走。第一次 4.1.0 候选修补仍失败；最终候选明确已有模块间契约变化先做架构分流，并保留既定 API 文档工作的原 owner。两次旧失败及新结果均保留。

当前候选的受影响集为 14 条（7 条 discovery、7 条显式 architecture），覆盖 DIRECT、BOUNDARY_NOTE、ARCHITECTURE_GATE、DISCOVERY 和 API owner 非拦截；已评分 14/14，PASS 14/14。这不声称对当前版本重新全跑全部案例库。

d43 的独立复核确认原唯一 owner 断言过严：核心用户意图尚未明确时，先用 interview-me 澄清符合既有 Skill；规格制定仍应在依赖任务拆解之前完成。保留原 FAIL 和判因，修正评测为接受合理访谈或规格路线，补跑原请求及显式访谈、意图已定但行为未定两个边界案例。未修改访谈或规格 Skill，也未把此次变化当作 Skill 缺陷修复。

d22 的独立仲裁确认是 owner 轨迹标签错误：实际响应尊重拒绝，没有重复提议或批评。保留原 FAIL，单独记录该行为事实；补充复测仅明确 selected_skills 与 skill_files_read 的通用区别，没有修改 Skill 或提供本案例答案。

## 模型执行比较

| 实际配置 | 库存事务 /35 | 投递对账 /35 | 回归测试编写 /30 |
|---|---:|---:|---:|
| gpt-6-astra ultra | 35 | 35 | 30 |
| gpt-6-astra xhigh | 35 | 35 | 30 |
| gpt-5.6-sol ultra | 35 | 35 | 30 |
| gpt-5.6-sol xhigh | 35 | 35 | 30 |
| gpt-5.6-terra ultra | 35 | 35 | 30 |

分数是加权结果分，不是测试条数。每项还要求关键检查全部通过、受保护文档和代码范围不变。三个任务覆盖事务/幂等/租户隔离、未知副作用与旧状态对账，以及权限、原子性和版本冲突的回归证据。

最终独立审查发现库存测试的一个盲区：Sol xhigh、Sol ultra、Terra ultra 的提交和原参考实现先把数量转成十进制 JSON，极大正整数可能在库存或重试冲突判断前触发 ValueError。Astra 两份提交分别通过提前判断或十六进制指纹处理这一点。该发现来自逐份源码审查、保存的 Astra 原始自测失败日志，以及 Python 标准库对 10**5000 的独立复现；不是五份产物的新增统一运行结果。原 35 分和所有提交保持不变，完整契约正确性不能由这些分数推定；后续基准修订应统一补上此边界。

回归测试题 v1 的输入验证措辞存在歧义；独立盲审确认后，保存两次旧输出并排除于主比较。题面、候选实现、参考实现和三个单缺陷变体统一修正为 v2，再让全部五个组合用新的隔离上下文运行。未启动的三份旧作业不计为执行或失败。评分同时要求所报回归在正确参考实现通过、在候选实现确实暴露问题；正常 API 调用产生的意外异常可构成有效回归，导入失败不可得分。

这些样本用于检验当前任务条件下能否达标，不足以证明跨模型等价、统计排序、长期可靠性或 Skill 的因果增益。保持质量优先的既定职责分工：Astra ultra 主控/规划/关键独立审查；Astra xhigh 执行首选、Sol xhigh 次选、Sol ultra 增强选项；Terra ultra 仅作明确有界执行的最低认可组合。

## 交付证据

本地证据包包含冻结 Skill/案例、每次独立输入输出、配置与耗时回执、独立评分、基准种子/隐藏检查/参考实现/变体、修补迭代、原始日志和复现脚本。静态 HTML 查看器汇集原始案例、补充复测与主比较，UNOBSERVABLE 不计为通过或失败。浏览器安全策略拦截了本地文件预览；已做数据解析和 JavaScript 语法检查，未声称验证浏览器显示。

静态校验状态：True。命令为 `rtk proxy python3 evidence/validate_source.py`；包含 27 个 Skill quick validators、插件 validator、JSON/YAML、唯一 Skill 与源归属、固定 commit、元数据预算、相对链接、私有路径/密钥/脚手架扫描和 `git diff --check`。该脚本记录本次本地主机的路径；迁移时按证据包 README 调整。

最终独立 Astra ultra 审查：PASS。完整结论及对应运行回执保存在证据包 delivery/final-audit/ 与 results/ 中。

未执行插件安装、发布、Git commit/push 或真实应用验收。StellarSight 场景的策略迁移和 Goal 推进另有独立记录：此前已完成策略与首台设备核对，并因缺少真实告警及触发/恢复证据记录过 BLOCKED。交付前只读复查显示该任务已开始新一轮处理，尚无本轮结果；当前 Goal 状态未重新核实，不能沿用旧阻塞记录或声称开发里程碑完成。
