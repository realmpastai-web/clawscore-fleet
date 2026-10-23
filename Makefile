SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c

ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHON ?= python3.11
export PYTHONPATH := $(ROOT)

MANIFEST ?= fixtures/holdout-example.json

.PHONY: help matrix fingerprints verify-offline lab-up lab-down scan verify demo export feed-check holdout-lab-up holdout-lab-down holdout-scan holdout-report npm-audit-live npm-audit-offline

.DEFAULT_GOAL := help

help:
	@printf '%s\n' 'targets: matrix fingerprints verify-offline lab-up lab-down scan verify demo export feed-check holdout-lab-up holdout-scan holdout-report holdout-lab-down npm-audit-live npm-audit-offline'

matrix:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.release_matrix 2>&1 | tee evidence/matrix.log
	$(PYTHON) -m clawscore_fleet.gates_v023

fingerprints:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.build_fingerprints 2>&1 | tee evidence/fingerprints.log

verify-offline:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.verify_offline 2>&1 | tee evidence/verify-offline.log

lab-up:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.lab_up 2>&1 | tee evidence/lab-up.log

lab-down:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.lab_up down 2>&1 | tee evidence/lab-down.log

scan:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.scan_lab 2>&1 | tee evidence/scan.log

verify:
	mkdir -p evidence
	rc=0; $(PYTHON) -m clawscore_fleet.verify_run 2>&1 | tee evidence/verify.log || rc=$$?; \
	$(PYTHON) -m clawscore_fleet.hash_evidence; \
	exit $$rc

demo:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.demo 2>&1 | tee evidence/demo.log

export:
	mkdir -p evidence/export
	$(PYTHON) -m clawscore_fleet.export_defender 2>&1 | tee evidence/export.log

feed-check:
	mkdir -p evidence
	$(PYTHON) -m clawscore_fleet.feed_check 2>&1 | tee evidence/feed-check.log

holdout-lab-up:
	mkdir -p evidence/holdout
	$(PYTHON) -m clawscore_fleet.holdout_lab up --manifest $(MANIFEST) 2>&1 | tee evidence/holdout/lab-up.log

holdout-lab-down:
	mkdir -p evidence/holdout
	$(PYTHON) -m clawscore_fleet.holdout_lab down 2>&1 | tee evidence/holdout/lab-down.log

holdout-scan:
	mkdir -p evidence/holdout
	$(PYTHON) -m clawscore_fleet.holdout_lab scan 2>&1 | tee evidence/holdout/scan.log

holdout-report:
	mkdir -p evidence/holdout
	$(PYTHON) -m clawscore_fleet.holdout_lab report 2>&1 | tee evidence/holdout/report.log

npm-audit-live:
	mkdir -p evidence/npm-audit
	vers=$$($(PYTHON) -c 'from clawscore_fleet.npm_audit import lab_versions; print(" ".join(lab_versions()))'); \
	$(PYTHON) -m clawscore_fleet.npm_audit --live --versions $$vers --out evidence/npm-audit/ 2>&1 | tee evidence/npm-audit/live.log

npm-audit-offline:
	mkdir -p evidence/npm-audit
	vers=$$($(PYTHON) -c 'from clawscore_fleet.npm_audit import lab_versions; print(" ".join(lab_versions()))'); \
	$(PYTHON) -m clawscore_fleet.npm_audit --offline evidence/npm-audit/raw --versions $$vers --out evidence/npm-audit/ 2>&1 | tee evidence/npm-audit/offline.log
