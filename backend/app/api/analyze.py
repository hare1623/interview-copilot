from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil
import os

from app.services.resume_analysis_service import (
    ResumeAnalysisService
)

router = APIRouter()

UPLOAD_FOLDER = "uploads"

analysis_service = ResumeAnalysisService()


@router.post("/resume")

async def analyze_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = (
        analysis_service.analyze_resume(
            file_path
        )
    )

    return result