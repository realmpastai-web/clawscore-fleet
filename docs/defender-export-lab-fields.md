# Lab-derived Defender export fields

Spec line 14 (`docs/inputs/export-spec-v0.2.1.md`) says Device ID is a string and its format is UNPROVEN. The value this repo writes is lab-derived, Defender format UNPROVEN.

## Device ID

The v0.2 lab scan evidence does not record a host id or a container id. `evidence/scan.json` installs, `evidence/ps.txt`, `evidence/lab-up.log`, and `fleet/hosts.txt` name each lab container (`claw-01` through `claw-30`) and do not store a runtime id. `aadDeviceId` stays an empty string because the scan does not record a directory device id. The CSV Device ID column is not that field.

For each install, Device ID is the lowercase hex SHA-256 of the UTF-8 bytes of a canonical JSON object built only from fields already present on that `scan.json` install:

- `id` (the install id recorded by the scan)
- `device` (`agent365.device`)
- `install_root`
- `config_paths`, sorted lexicographically

Encoding: `json.dumps` with `sort_keys=True`, `ensure_ascii=True`, and separators `(',', ':')` (no spaces). The same install record always hashes to the same id. No random value is added.

`clawscore_fleet.export_defender.lab_device_id` is the implementation.

## First seen, Timestamp, LastUpdatedDateTime

`evidence/scan.json`, `evidence/scan.log`, `evidence/ps.txt`, `evidence/lab-up.log`, and `evidence/verify-report.json` do not contain a lab observation clock. Published times in `evidence/cve-map.json`, `evidence/landscape-check.log`, and `evidence/feed-check.log` are advisory-feed times, so they are not used as a device discovery time. File modification times are not read.

`make export` and `make verify` therefore record one observation time when `evidence/lab-scan-observed-at.txt` is absent. The file is a single ISO 8601 UTC line with second precision, for example `2026-10-17T12:34:56Z`. After that line is committed, both commands read it and do not rewrite it. First seen (File A), Timestamp, and LastUpdatedDateTime (File B) are that one recorded observation, because the evidence has no separate first-seen or last-updated clock.

## PublishedStatus

File B sets PublishedStatus to JSON null. Spec line 33 allows Draft or Published and marks the value for local agents UNPROVEN, so the export does not choose either string.
