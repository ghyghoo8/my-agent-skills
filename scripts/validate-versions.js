#!/usr/bin/env node

"use strict";

const { readFileSync } = require("node:fs");

const manifestPaths = [
  "plugin.json",
  ".codex-plugin/plugin.json",
  ".claude-plugin/plugin.json",
];

const marketplacePaths = [
  ".claude-plugin/marketplace.json",
  ".agents/plugins/marketplace.json",
];

function readJson(filePath) {
  return JSON.parse(readFileSync(filePath, "utf8"));
}

function assertVersion(label, actual, expected) {
  if (actual !== expected) {
    throw new Error(
      `${label} has version ${actual ?? "<missing>"}; expected ${expected}`,
    );
  }
}

const agentSkillsVersion = readJson("plugin.json").version;

for (const manifestPath of manifestPaths) {
  assertVersion(manifestPath, readJson(manifestPath).version, agentSkillsVersion);
}

for (const marketplacePath of marketplacePaths) {
  const entry = readJson(marketplacePath).plugins?.find(
    (plugin) => plugin.name === "agent-skills",
  );
  assertVersion(
    `${marketplacePath} agent-skills entry`,
    entry?.version,
    agentSkillsVersion,
  );
}

const architectureManifestPath =
  "plugins/architecture-gate/.codex-plugin/plugin.json";
const architectureVersion = readJson(architectureManifestPath).version;
const architectureEntry = readJson(
  ".agents/plugins/marketplace.json",
).plugins?.find((plugin) => plugin.name === "architecture-gate");

assertVersion(
  ".agents/plugins/marketplace.json architecture-gate entry",
  architectureEntry?.version,
  architectureVersion,
);

console.log(
  `Plugin versions are consistent: agent-skills ${agentSkillsVersion}, architecture-gate ${architectureVersion}.`,
);
