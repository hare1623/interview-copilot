from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.db.database import engine
from app.db.models import Base
from app.api.analyze import router as analyze_router
from app.api.interview import router as interview_router
from app.exceptions.handlers import global_exception_handler

Base.metadata.create_all(bind=engine)
app = FastAPI(debug=False)
app.add_exception_handler(Exception, global_exception_handler)
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
app.include_router(interview_router, prefix="/interview", tags=["Interview"])


@app.get("/")
def root():
    return {"message": "Backend running successfully"}
