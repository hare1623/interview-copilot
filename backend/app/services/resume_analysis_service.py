import json
from app.utils.json_parser import JSONParser
from app.services.pdf_service import PDFService
from app.services.profile_extraction_service import ProfileExtractionService
from app.services.candidate_profile_service import CandidateProfileService
from app.core.logger import logger


class ResumeAnalysisService:

    def __init__(self):

        self.pdf_service = PDFService()

        self.profile_service = ProfileExtractionService()

        self.candidate_service = CandidateProfileService()

    def analyze_resume(self, file_path):
        logger.info("Starting resume analysis")

        resume_text = self.pdf_service.extract_text(file_path)
        logger.info("Resume text extracted successfully")

        profile_response = self.profile_service.extract_profile(resume_text)
        logger.info("Profile extracted successfully")

        profile_data = JSONParser.parse_json(profile_response)

        saved_candidate = self.candidate_service.save_profile(profile_data)
        logger.info("Candidate profile saved successfully")

        return {
            "id": saved_candidate.id,
            "name": saved_candidate.name,
            "role": saved_candidate.role,
            "skills": profile_data.get("skills", []),
            "domains": profile_data.get("domains", []),
            "summary": saved_candidate.summary,
        }
