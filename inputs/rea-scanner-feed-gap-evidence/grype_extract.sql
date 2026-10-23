-- Grype DB v6 extraction for npm package openclaw.
-- Form A: blobs.value JSON ranges[].version.constraint, evaluated by
-- clawscore_fleet.versions.parse_comparators and cves.in_range.
-- Ecosystem must be npm. Package name must casefold to openclaw.
-- provider_id is the stored source string (Q1). status is recorded and not filtered.

SELECT vh.name, vh.provider_id, vh.status, vh.withdrawn_date, b.value
FROM affected_package_handles AS aph
JOIN packages AS p ON p.id = aph.package_id
JOIN vulnerability_handles AS vh ON vh.id = aph.vulnerability_id
JOIN blobs AS b ON b.id = aph.blob_id
WHERE p.ecosystem = 'npm'
  AND lower(p.name) = 'openclaw'
ORDER BY vh.name;

-- Q1, every provider id stored on any npm package row:
SELECT vh.provider_id, COUNT(*)
FROM affected_package_handles AS aph
JOIN packages AS p ON p.id = aph.package_id
JOIN vulnerability_handles AS vh ON vh.id = aph.vulnerability_id
WHERE p.ecosystem = 'npm'
GROUP BY vh.provider_id
ORDER BY vh.provider_id;
