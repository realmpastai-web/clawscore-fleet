#!/bin/sh
# Plant lab files, then become an idle PID 1 so /proc/1/environ keeps the planted names.
set -eu
node /opt/lab/apply-plant.js > /tmp/claw.env
set -a
# shellcheck disable=SC1091
. /tmp/claw.env
set +a
rm -f /tmp/claw.env
exec sleep infinity
