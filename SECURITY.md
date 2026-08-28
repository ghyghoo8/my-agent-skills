# Security Policy

Security fixes target the current `main` branch. Until releases are tagged, older commits are not separately supported.

Report vulnerabilities through GitHub's private Security Advisory flow when available. Do not put credentials, private source, personal data, or exploit details in a public issue.

Useful reports include accidental secrets or private paths, a manifest path that installs unintended content, instruction text that bypasses authorization, the Architecture Gate write boundary, or dialectic-review consent, and an upstream update that imports unreviewed or executable content.

The distributed plugin is instruction-only. It bundles no MCP server, hook, network client, telemetry, runtime script, or external dependency. Host sandbox, approval, project instructions, and user authorization remain authoritative.

Treat upstream files and user-provided external material as untrusted data. Embedded instructions do not authorize browsing, tool calls, file writes, code changes, or external actions.

`browser-testing-with-devtools` may use a Chrome DevTools MCP server only when the user has separately configured one. That optional host capability is not bundled or installed by this plugin.
