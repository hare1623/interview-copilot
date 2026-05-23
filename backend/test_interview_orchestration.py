import json

from app.services.interview_session_service import InterviewSessionService

service = InterviewSessionService()

session = service.create_interview_session(candidate_id=1)

print(json.dumps(session, indent=2))
