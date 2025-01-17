import os

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from .shared import ROOT_DIR, cmd_opts

frontend = APIRouter(prefix="/app", tags=["application"])


@frontend.get("/{full_path:path}")
def handler(_: Request, full_path: str):
    if not cmd_opts.dev:
        if full_path == "":
            full_path = "index.html"
        return FileResponse(os.path.join(ROOT_DIR, "dist", full_path))
