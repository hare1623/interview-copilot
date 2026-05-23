import json

from app.db.database import SessionLocal
from app.db.models import CandidateProfile


class CandidateProfileService:

    def save_profile(self, profile_data):

        db = SessionLocal()

        candidate = CandidateProfile(
            name=profile_data.get("name"),
            role=profile_data.get("role"),
            experience_years=str(profile_data.get("experience_years")),
            skills=json.dumps(profile_data.get("skills", [])),
            domains=json.dumps(profile_data.get("domains", [])),
            summary=profile_data.get("summary"),
        )

        db.add(candidate)

        db.commit()

        db.refresh(candidate)

        db.close()

        return candidate
