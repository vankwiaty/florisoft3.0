"""FastAPI backend for Florisoft."""
import sys
from pathlib import Path

# Allow importing config and models from project root when running: uvicorn backend.main:app
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from config import Config

app = FastAPI(title="Florisoft API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cfg = Config()


# --- Pydantic schemas for API ---
class ProformaItemSchema(BaseModel):
    subclient: str
    article: str
    quantity: float
    client_price: float


class ProformaRequestSchema(BaseModel):
    buyer_id: str
    series_name: str
    date: str
    items: list[ProformaItemSchema]


# --- Routes ---
@app.get("/")
def root():
    return {"app": "Florisoft API", "docs": "/docs"}


@app.get("/api/config")
def get_config():
    """Public config for the web app (no secrets in production)."""
    return {
        "excel_path": cfg.excel_path,
        "pdf_output": cfg.pdf_output,
        "margin_threshold": cfg.margin_threshold,
        "deviant_threshold": cfg.deviant_threshold,
        "client_map": cfg.client_map,
        "series_map": cfg.series_map,
    }


@app.get("/api/margins")
def get_margins():
    """Margin calculation – stub; plug in real Excel + logic later."""
    # TODO: load cfg.excel_path, compute margins, return MarginResult as JSON
    return {
        "ok": True,
        "message": "Margin logic not yet implemented",
        "excel_path": cfg.excel_path,
    }


@app.post("/api/margins/upload")
async def upload_margins_excel(file: UploadFile = File(...)):
    """Upload Excel for margin calculation – stub."""
    # TODO: parse file, compute margins
    return {"ok": True, "filename": file.filename, "message": "Upload received; logic not yet implemented"}


@app.get("/api/checklist")
def get_checklist():
    """Checklist PDF – stub."""
    return {"ok": True, "pdf_output": cfg.pdf_output, "message": "Checklist logic not yet implemented"}


@app.post("/api/checklist/generate")
async def generate_checklist(file: Optional[UploadFile] = File(None)):
    """Generate checklist PDF – stub."""
    return {"ok": True, "message": "PDF generation not yet implemented"}


@app.post("/api/proforma")
def create_proforma(body: ProformaRequestSchema):
    """Send proforma to iFirma – stub."""
    # TODO: use models.ProformaRequest and cfg (ifirma_user, ifirma_key, url)
    return {"ok": True, "message": "Proforma API not yet implemented", "buyer_id": body.buyer_id}


@app.get("/api/fetch-email")
def fetch_email():
    """Fetch & email – stub."""
    return {"ok": True, "message": "Fetch & email not yet implemented"}
