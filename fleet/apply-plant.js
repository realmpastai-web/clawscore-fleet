"use strict";

const fs = require("fs");
const path = require("path");

const plantPath = process.env.LAB_PLANT || "/opt/lab/plant.json";
const poolPath = "/opt/lab/secrets-pool.json";
const plant = JSON.parse(fs.readFileSync(plantPath, "utf8"));
const pool = JSON.parse(fs.readFileSync(poolPath, "utf8"));

function shQuote(value) {
  return "'" + String(value).replace(/'/g, "'\\''") + "'";
}

function requireName(name) {
  if (!/^[A-Z][A-Z0-9_]*$/.test(name)) {
    console.error("refusing env name " + name);
    process.exit(1);
  }
  if (!Object.prototype.hasOwnProperty.call(pool, name)) {
    console.error("missing pool entry for " + name);
    process.exit(1);
  }
}

function serverBody(spec) {
  const body = {
    command: spec.command,
    args: spec.args || [],
  };
  const env = {};
  for (const name of spec.env_names || []) {
    requireName(name);
    env[name] = pool[name];
  }
  if (Object.keys(env).length) body.env = env;
  return body;
}

function writeJson(dest, body) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.writeFileSync(dest, JSON.stringify(body, null, 2) + "\n", { mode: 0o600 });
}

function removeFile(dest) {
  try {
    fs.rmSync(dest, { force: true });
  } catch (err) {
    console.error("unable to remove " + dest);
    process.exit(1);
  }
}

for (const dest of [
  "/opt/openclaw/package.json",
  "/opt/openclaw/package-lock.json",
  "/opt/openclaw/node_modules/.package-lock.json",
]) {
  removeFile(dest);
}

const work = plant.work_dir;
const state = plant.state_dir;
fs.mkdirSync(work, { recursive: true });
fs.mkdirSync(state, { recursive: true });
const link = path.join(work, "node_modules");
try {
  fs.lstatSync(link);
  fs.unlinkSync(link);
} catch (err) {
  if (err.code !== "ENOENT") throw err;
}
fs.symlinkSync("/opt/openclaw/node_modules", link);

const pkgJson = path.join(work, "node_modules", "openclaw", "package.json");
if (plant.stripped === "removed") {
  removeFile(pkgJson);
} else if (plant.stripped === "false-version") {
  if (!plant.false_version) {
    console.error("false version missing");
    process.exit(1);
  }
  const parsed = JSON.parse(fs.readFileSync(pkgJson, "utf8"));
  parsed.version = plant.false_version;
  fs.writeFileSync(pkgJson, JSON.stringify(parsed));
} else if (plant.stripped && plant.stripped !== "none") {
  console.error("unknown strip mode");
  process.exit(1);
}

const openclaw = { autoApprove: !!plant.auto_approve };
const openclawServers = plant.openclaw_servers || {};
if (Object.keys(openclawServers).length) {
  const servers = {};
  for (const [name, spec] of Object.entries(openclawServers)) {
    servers[name] = serverBody(spec);
  }
  openclaw.mcp = { servers };
}
writeJson(path.join(state, "openclaw.json"), openclaw);

for (const extra of plant.extra_files || []) {
  if (extra.format === "mcpServers") {
    const servers = {};
    for (const [name, spec] of Object.entries(extra.servers)) servers[name] = serverBody(spec);
    writeJson(extra.path, { mcpServers: servers });
  } else if (extra.format === "single") {
    const body = serverBody(extra.server);
    body.name = extra.name;
    writeJson(extra.path, body);
  } else {
    console.error("unknown mcp format");
    process.exit(1);
  }
}

const lines = [
  "export OPENCLAW_STATE_DIR=" + shQuote(state),
  "export OPENCLAW_CONFIG_PATH=" + shQuote(path.join(state, "openclaw.json")),
];
for (const name of plant.env_names || []) {
  requireName(name);
  lines.push("export " + name + "=" + shQuote(pool[name]));
}
process.stdout.write(lines.join("\n") + "\n");
