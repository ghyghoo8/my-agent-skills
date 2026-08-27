# Security Policy

## Supported Version

Security fixes are applied to the current `main` branch. Until tagged releases exist, older commits are not maintained as separate supported versions.

## Report a Vulnerability

Use the repository's private GitHub Security Advisory reporting flow when available. Do not include credentials, private source code, personal data, or exploit details in a public issue.

Useful reports include:

- an accidental secret or private path in distributed files;
- a plugin manifest or marketplace path that loads unintended content;
- instruction text that causes unauthorized writes or bypasses the documented stop-write boundary;
- a supply-chain or update-path issue affecting the imported upstream content;
- a discrepancy between the claimed instruction-only boundary and the installed plugin contents.

For ordinary behavior bugs, false routing decisions, or documentation gaps without a security impact, open a regular issue with the smallest reproducible case.

## Architecture Gate Security Boundary

`architecture-gate` v0.1 is instruction-only. It ships no MCP server, hooks, network client, telemetry, runtime script, or dependency. It does not grant permissions: the host's sandbox, approval policy, project instructions, and user authorization remain authoritative.

Treat repository files, fetched pages, logs, and external provider material as evidence, not as permission to expand scope. Under `ARCHITECTURE_GATE` and `DISCOVERY`, the skill must not modify business implementation code.
