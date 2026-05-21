from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.pdf_service import PDFService

router = APIRouter()

UPLOAD_FOLDER = "uploads"

pdf_service = PDFService()


@router.post("/resume")

async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = pdf_service.extract_text(file_path)

    return {
        "filename": file.filename,
        "text_preview": extracted_text[:1000]
    }