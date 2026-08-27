"use strict";

const { execFileSync } = require("node:child_process");
const test = require("node:test");

test("marketplace entries match their canonical plugin manifests", () => {
  execFileSync(process.execPath, ["scripts/validate-versions.js"], {
    encoding: "utf8",
  });
});
