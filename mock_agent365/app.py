"""Local mock of an Agent 365 / Defender discovery export. No risk score."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

VIEW = json.loads((Path(__file__).resolve().parent / "defender_view.json").read_text())
FIELDS = ["name", "version", "process", "device", "user", "autoApprove", "mcpServers"]

app = FastAPI(title="agent365-mock")


def _csv_text() -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in VIEW["agents"]:
        writer.writerow(
            {
                "name": row["name"],
                "version": row["version"],
                "process": row["process"],
                "device": row["device"],
                "user": row["user"],
                "autoApprove": row["autoApprove"],
                "mcpServers": "|".join(row["mcpServers"]),
            }
        )
    return buffer.getvalue()


@app.get("/agents")
def agents() -> JSONResponse:
    return JSONResponse(VIEW["agents"])


@app.get("/export.csv")
def export_csv() -> PlainTextResponse:
    return PlainTextResponse(_csv_text(), media_type="text/csv")
