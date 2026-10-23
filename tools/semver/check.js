"use strict";

const semver = require("semver");

let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (chunk) => {
  raw += chunk;
});
process.stdin.on("end", () => {
  const input = JSON.parse(raw);
  const pairs = input.pairs || [];
  const standard = new Array(pairs.length);
  const prerelease = new Array(pairs.length);
  const errors = [];
  let commaRanges = 0;
  for (let i = 0; i < pairs.length; i += 1) {
    const version = pairs[i][0];
    const range = pairs[i][1];
    if (String(range).includes(",")) {
      commaRanges += 1;
    }
    try {
      if (!semver.valid(version)) {
        standard[i] = null;
        prerelease[i] = null;
        errors.push([i, "invalid version"]);
        continue;
      }
      standard[i] = semver.satisfies(version, range);
      prerelease[i] = semver.satisfies(version, range, { includePrerelease: true });
    } catch (err) {
      standard[i] = null;
      prerelease[i] = null;
      errors.push([i, String(err && err.message ? err.message : err)]);
    }
  }
  process.stdout.write(
    JSON.stringify({
      semver: require("semver/package.json").version,
      standard,
      prerelease,
      errors,
      comma_ranges: commaRanges,
    })
  );
});
