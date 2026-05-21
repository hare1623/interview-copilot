from app.services.pdf_service import PDFService
from app.services.profile_extraction_service import ProfileExtractionService


pdf_service = PDFService()

profile_service = ProfileExtractionService()


resume_text = pdf_service.extract_text(
    "uploads/Hareharan-Angular Developer.pdf"
)

response = profile_service.extract_profile(
    resume_text
)

print(response)