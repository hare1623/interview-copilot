import json

from app.services.pdf_service import PDFService
from app.services.profile_extraction_service import (
    ProfileExtractionService
)
from app.services.candidate_profile_service import (
    CandidateProfileService
)


pdf_service = PDFService()

profile_service = ProfileExtractionService()

candidate_service = CandidateProfileService()


resume_text = pdf_service.extract_text(
    "uploads/Hareharan-Angular Developer.pdf"
)

profile_response = profile_service.extract_profile(
    resume_text
)

profile_data = json.loads(profile_response)

saved_candidate = candidate_service.save_profile(
    profile_data
)

print(saved_candidate.id)
print(saved_candidate.name)
print(saved_candidate.role)