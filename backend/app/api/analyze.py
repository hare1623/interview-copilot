from fastapi import APIRouter, UploadFile, File
from app.schemas.response_schema import APIResponseSchema

import shutil
import os

from app.services.resume_analysis_service import ResumeAnalysisService

router = APIRouter()

UPLOAD_FOLDER = "uploads"

analysis_service = ResumeAnalysisService()


@router.post("/resume", response_model=APIResponseSchema)
async def analyze_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    result = analysis_service.analyze_resume(file_path)

    return {"success": True, "message": "Resume analyzed successfully", "data": result}
