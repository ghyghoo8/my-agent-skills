---
name: performance-optimization
description: Measures and improves frontend, backend, query, or database performance. Use when a constraint, regression, or profiled bottleneck exists. Do not optimize from hypothetical scale alone.
---

# Performance Optimization

## Overview

Measure before optimizing. Performance work without measurement is guessing — and guessing leads to premature optimization that adds complexity without improving what matters. Profile first, identify the actual bottleneck, fix it, measure again. Optimize only what measurements prove matters.

## When to Use

- Performance requirements exist in the spec (load time budgets, response time SLAs)
- Users or monitoring report slow behavior
- Core Web Vitals scores are below thresholds
- You suspect a change introduced a regression
- Building features that handle large datasets or high traffic

**When NOT to use:** Don't optimize before you have evidence of a problem. Premature optimization adds complexity that costs more than the performance it gains.

## Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | ≤ 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

## The Optimization Workflow

```
1. MEASURE  → Establish baseline with real data
2. IDENTIFY → Find the actual bottleneck (not assumed)
3. FIX      → Address the specific bottleneck
4. VERIFY   → Measure again; keep or revert
5. GUARD    → Add monitoring or tests to prevent regression
```

### Step 1: Measure

Read linked reference sections only when the measured symptom or chosen approach
needs their detail. Skip unrelated frontend/backend examples; the checklist is
not a requirement to read the entire reference or run every command.

Two complementary approaches — select evidence suited to the claim and authorized scope:

- **Synthetic (Lighthouse, DevTools Performance tab):** Controlled conditions, reproducible. Best for CI regression detection and isolating specific issues.
- **RUM (web-vitals library, CrUX):** Real user data in real conditions. Use available, authorized field evidence to validate actual user impact. Without it, report the controlled measurement improvement and leave production user impact unverified; do not install telemetry merely to finish local work.

For frontend profiling and field-data examples, read the relevant
[frontend measurement section](../../references/performance-checklist.md#inp-field-data-and-devtools-workflow).
For API/database timing, read the
[backend measurement example](../../references/performance-checklist.md#backend-measurement-example).

### Where to Start Measuring

Use the symptom to decide what to measure first:

```
What is slow?
├── First page load
│   ├── Large bundle? --> Measure bundle size, check code splitting
│   ├── Slow server response? --> Measure TTFB in DevTools Network waterfall
│   │   ├── DNS long? --> Add dns-prefetch / preconnect for known origins
│   │   ├── TCP/TLS long? --> Enable HTTP/2, check edge deployment, keep-alive
│   │   └── Waiting (server) long? --> Profile backend, check queries and caching
│   └── Render-blocking resources? --> Check network waterfall for CSS/JS blocking
├── Interaction feels sluggish
│   ├── UI freezes on click? --> Profile main thread, look for long tasks (>50ms)
│   ├── Form input lag? --> Check re-renders, controlled component overhead
│   └── Animation jank? --> Check layout thrashing, forced reflows
├── Page after navigation
│   ├── Data loading? --> Measure API response times, check for waterfalls
│   └── Client rendering? --> Profile component render time, check for N+1 fetches
└── Backend / API
    ├── Single endpoint slow? --> Profile database queries, check indexes
    ├── All endpoints slow? --> Check connection pool, memory, CPU
    └── Intermittent slowness? --> Check for lock contention, GC pauses, external deps
```

### Step 2: Identify the Bottleneck

Common bottlenecks by category:

**Frontend:**

| Symptom | Likely Cause | Investigation |
|---------|-------------|---------------|
| Slow LCP | Large images, render-blocking resources, slow server | Check network waterfall, image sizes |
| High CLS | Images without dimensions, late-loading content, font shifts | Check layout shift attribution |
| Poor INP | Heavy JavaScript on main thread, large DOM updates | Check long tasks in Performance trace |
| Slow initial load | Large bundle, many network requests | Check bundle size, code splitting |

**Backend:**

| Symptom | Likely Cause | Investigation |
|---------|-------------|---------------|
| Slow API responses | N+1 queries, missing indexes, unoptimized queries | Check database query log |
| Memory growth | Leaked references, unbounded caches, large payloads | Heap snapshot analysis |
| CPU spikes | Synchronous heavy computation, regex backtracking | CPU profiling |
| High latency | Missing caching, redundant computation, network hops | Trace requests through the stack |

### Step 3: Fix Common Anti-Patterns

#### N+1 Queries (Backend)

When profiling shows N+1 owner lookups, fetch related owners together using the existing ORM or a join; see the [N+1 query example](../../references/performance-checklist.md#n1-query-example).

#### Unbounded Data Fetching

Bound list reads with the project's pagination contract and limits; see the [paginated query example](../../references/performance-checklist.md#paginated-query-example).

#### Queries That Ignore Their Index

"Add an index" is the guess. The query plan is the measurement. Use the target database's plan command and semantics; the linked example is PostgreSQL-style. `EXPLAIN ANALYZE` executes the statement, so run it only for a representative read in an authorized, bounded environment. Do not execute mutating statements this way outside an isolated disposable environment unless the user has explicitly authorized it.

See the [query plan example](../../references/performance-checklist.md#query-plan-example) for PostgreSQL-style syntax; adapt it to the target database.

Three things in the output decide the fix:

| What you see | What it means |
|---|---|
| `Seq Scan` on a large table where you expected an index | No usable index for this predicate |
| Estimated `rows=` off from actual by an order of magnitude | Stale statistics; the planner is choosing on bad information |
| A `Sort` node above the scan | The index covers the filter but not the `ORDER BY` |

Index for the **shape of the query**, not the column in isolation. In a composite index, equality columns come first, then the range or sort column:

See the [index example](../../references/performance-checklist.md#index-example) for the equality-plus-sort shape above.

**When an index will not help:**

| Situation | Why |
|---|---|
| Low selectivity, querying the dominant value (a `status` column that is 95% `active`, filtered on `active`) | A sequential scan is genuinely cheaper; the planner will ignore the index. Filtering on the rare value is the opposite case, and a partial index serves it well |
| Leading wildcard (`LIKE '%term'`) | A B-tree cannot seek without a prefix; needs trigram or full-text |
| Function on the column (`WHERE lower(email) = ?`) | The plain column index is unusable; index the expression instead |
| Write-heavy table | Every index is a tax on every `INSERT`/`UPDATE`; measure the write cost, not just the read gain |

Re-run the same plan measurement after the change. An index that did not improve the plan is a revert (Step 4), and it is not free: it still costs on every write.

#### Connection Pool Exhaustion

Common clues include many endpoints slowing at once, time spent waiting to acquire a connection, and pool-acquisition timeouts. Active or idle session counts and database saturation can vary, so confirm the cause with pool and database metrics before changing capacity.

Reuse one pool per database/configuration in each process, with acquisition timeouts and capacity justified by the combined deployment budget. See the [pool reuse example](../../references/performance-checklist.md#pool-reuse-example).

**Bigger is not faster.** A pool larger than what the database can execute concurrently just relocates the queue from your app to the database, where it is harder to see. Size the combined pools below the database ceiling and retain operational headroom. When instance count is unbounded (serverless, autoscaling), a proxy that multiplexes connections (pgbouncer, RDS Proxy) is usually safer than a higher `max`.

#### Missing Image Optimization (Frontend)

For a measured image bottleneck, use responsive formats and explicit dimensions; prioritize hero/LCP images and lazy-load only below-the-fold images. See the [responsive image example](../../references/performance-checklist.md#responsive-image-example).

#### Unnecessary Re-renders (React)

Profile the component first; stabilize inputs or memoize expensive renders/calculations only where the measured cost justifies it. See the [React render example](../../references/performance-checklist.md#react-render-example).

#### Large Bundle Size

Measure bundle impact before changing imports. Modern bundlers can tree-shake named ESM imports when the dependency marks `sideEffects: false`; split heavy, rarely-used features or routes with appropriate loading states. See the [bundle splitting example](../../references/performance-checklist.md#bundle-splitting-example).

#### Missing Caching (Backend)

Cache what is expensive to produce and read far more often than it changes. Caching a query that was already fast adds a network hop, a staleness bug, and an eviction policy to maintain, in exchange for nothing.

**Pick the layer deliberately:**

| Layer | Visible to | Use when | Cost |
|---|---|---|---|
| In-process (`Map`, LRU) | One instance | Small, hot, per-instance staleness is acceptable | Each instance drifts independently; invalidation reaches only one |
| Shared (Redis, Memcached) | All instances | Instances must agree, or the value is expensive to recompute | A network hop, and another service to run and monitor |
| CDN / edge | Everyone, per URL | Responses are public and identical for a given key | Invalidation is the hard part; assume you cannot recall a bad response quickly |

See the [cache implementation example](../../references/performance-checklist.md#cache-implementation-example) only after choosing the layer, keys, acceptable staleness and invalidation below. Its TTL is illustrative; public HTTP caching requires responses identical for the authorized viewers represented by the key.

**Key design decides correctness.** Every input that changes the response belongs in the key: tenant, locale, permissions, feature flags. A key that omits the viewer is how one user's data gets served to another, and that ships as a performance win.

**Choose a primary invalidation strategy deliberately.** Combine strategies only when their interaction, ordering, and correctness boundary are explicit:

| Strategy | Trade-off |
|---|---|
| TTL | Simplest. You accept staleness up to the TTL, so state the acceptable window explicitly |
| Event or tag based | Targets freshness on write, but delivery, ordering, and failure semantics must be defined |
| Versioned keys (`user:42:profile:v7`) | Never invalidate, just stop reading old keys. Costs memory until eviction |

**Guard against the stampede.** A hot key expires, every concurrent request misses together, and the origin takes the full load at once, which is how a cache turns into an outage instead of preventing one. Serve stale while a single request recomputes (`stale-while-revalidate`), or coalesce concurrent misses behind one in-flight promise so N waiters cause one recompute.

**Do not cache:** anything whose staleness is a correctness bug (balances, permissions, inventory at checkout), or per-user data under a key that does not identify the user. See `../../references/performance-checklist.md` for request coalescing, write strategies, negative caching, and the cache checklist.

### Step 4: Verify (Keep or Revert)

A fix is a hypothesis until you re-measure. This step decides whether it survives.

**Re-measure the way you measured the baseline:** same command, same conditions, same fixed budget (wall-clock, sample count, or request count). A baseline taken on a cold cache against a result taken on a warm one measures the cache, not your change.

**Change one thing at a time.** Three optimizations landed together produce one number, and you cannot attribute it. If they must ship together, measure each in isolation first.

**Beat the noise, not just the mean.** Repeat the measurement and compare the delta against run-to-run variance. A 3% gain inside ±5% variance is not a gain; it is a different sample.

Then decide, strictly:

| Result vs. baseline | Action |
|---|---|
| Past the threshold, tests green | **Keep.** Record the measured before/after numbers. Commit only within user authorization or the applicable project workflow. |
| Within noise (no measurable change) | **Revert.** |
| Worse | **Revert.** |
| Improved, but a test went red | **Revert.** A regression wearing a win's clothing. |

**"Neutral" is a revert, not a keep.** This is the step teams skip: the change is already written, throwing it away feels wasteful, so it lands unmeasured, and the codebase accretes complexity that never bought anything. Code you keep, you maintain forever. Make it pay for itself.

**Correctness gates the metric.** Relevant regression tests and required project checks pass *and* the measured number improves beyond noise. An "optimization" that wins by dropping work the product needed (skipping a validation, caching something that must be fresh, removing an `await` that was load-bearing) is a regression, not a win.

#### Log every attempt, including the reverted ones

Reverted work leaves no trace in git history, which is exactly why the same dead idea gets tried again next quarter. Keep a short ledger so a discarded idea stays discarded:

| Idea | Baseline → Result | Verdict | Why |
|---|---|---|---|
| Memoize the row component | INP 240ms → 235ms | reverted | Inside noise (±15ms). Rows weren't the bottleneck. |
| Virtualize the list | INP 240ms → 90ms | kept | Long tasks gone from the trace. |
| Preconnect to the API origin | LCP 2.8s → 2.8s | reverted | Already same-origin. |

Use the existing project documentation or task-note location, or a section in an authorized PR description; follow project rules for note placement. What matters is that the next person (or the next agent) reads it before proposing an experiment, and doesn't re-run one that already failed.

### Step 5: Guard Against Regression

Guard the primary metric that justified the fix: for example LCP, INP, or API p95 latency. Reuse a representative synthetic check or existing field monitor. Repeat noisy measurements or compare a median/trend so normal variance does not become a flaky gate.

For production user-facing paths, synthetic checks and field monitoring are complementary when both are available and in scope. Use a meaningful field percentile and attribution suited to the metric; CrUX's rolling window is confirmation rather than an immediate alert. Do not install telemetry, add services, or expand CI merely to finish a local optimization. If a guard needs separate authorization or infrastructure, record the remaining gap and a concrete follow-up without claiming protection exists.

When a guard fires, return to Step 1 and establish a fresh baseline before proposing another fix.

**Example budgets, to replace with measured project targets:**

```
JavaScript bundle: < 200KB gzipped (initial load)
CSS: < 50KB gzipped
Images: < 200KB per image (above the fold)
Fonts: < 100KB total
API response time: < 200ms (p95)
Time to Interactive: < 3.5s on 4G
Lighthouse Performance score: ≥ 90
```

Reuse an existing in-scope CI check when applicable; see the
[CI measurement examples](../../references/performance-checklist.md#ci-measurement-examples).

## See Also

For detailed performance checklists, optimization commands, and anti-pattern reference, see `../../references/performance-checklist.md`.


## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "We'll optimize later" | Performance debt compounds. Fix obvious anti-patterns now, defer micro-optimizations. |
| "It's fast on my machine" | Your machine isn't the user's. Profile on representative hardware and networks. |
| "This optimization is obvious" | If you didn't measure, you don't know. Profile first. |
| "Users won't notice 100ms" | Research shows 100ms delays impact conversion rates. Users notice more than you think. |
| "The framework handles performance" | Frameworks prevent some issues but can't fix N+1 queries or oversized bundles. |
| "The query is slow, add an index" | Read the plan first. The index may already exist and be unusable, and every index taxes writes forever. |
| "Just cache it" | Caching an already-cheap call buys nothing and adds a staleness bug. Cache what is expensive *and* re-read far more than written. |
| "Raise the pool size, we're running out of connections" | A larger pool can move the queue somewhere less visible. Find what holds connections and preserve database headroom. |
| "It didn't help much, but it doesn't hurt" | Neutral changes are a revert. You pay maintenance on them forever and got nothing back. |
| "We already wrote it, may as well keep it" | Sunk cost. The measurement doesn't care how long the change took to write. |
| "The improvement is obvious, no need to re-measure" | Then re-measuring is cheap and proves it. Unmeasured wins are how neutral complexity lands. |

## Red Flags

- Optimization without profiling data to justify it
- N+1 query patterns in data fetching
- An index added without a query plan before and after to justify it
- A cache key that omits an input the response depends on (tenant, locale, viewer)
- A cache with no stated staleness window and no invalidation strategy
- Connection pool size raised in response to exhaustion, without finding what holds connections
- List endpoints without pagination
- Images without dimensions, lazy loading, or responsive sizes
- Bundle size growing without review
- Claiming production regression protection without verified monitoring or another applicable guard
- `React.memo` and `useMemo` everywhere (overusing is as bad as underusing)
- Optimizations kept without a re-measurement that justifies them
- Several optimizations bundled into one measurement, so no single change can be attributed
- A "win" that required a test to be changed, skipped, or deleted
- The same failed optimization attempted more than once because nobody recorded the first attempt

## Verification

After a performance change, verify the measured target and applicable impact checks. Project-required checks still apply; unrelated metrics do not become new acceptance criteria:

- [ ] Before and after measurements exist (specific numbers)
- [ ] The result was re-measured the same way as the baseline (same command, same conditions)
- [ ] The improvement exceeds run-to-run variance, not just the mean
- [ ] Changes that didn't beat the baseline were reverted, not kept as neutral
- [ ] Attempts are logged, kept and reverted alike, so a dead idea isn't re-run
- [ ] The specific bottleneck is identified and addressed
- [ ] Targeted Core Web Vitals meet the agreed goal when they are in scope; other user-impact claims are limited to available evidence
- [ ] Bundle impact is checked when the change affects frontend assets
- [ ] New data fetching avoids unnecessary repeated queries when relevant to the change
- [ ] Any new index is justified by a query plan before and after, and its write cost was considered
- [ ] Any new cache states what it keys on and how it goes stale
- [ ] The primary metric has a verified, in-scope regression check or a clearly reported protection gap
- [ ] Relevant regression tests and required project checks pass; run broader tests only when required or justified by unresolved impact
