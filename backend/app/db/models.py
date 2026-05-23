from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON

from app.db.database import Base


class CandidateProfile(Base):

    __tablename__ = "candidate_profiles"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    role = Column(String)

    experience_years = Column(String)

    skills = Column(Text)

    domains = Column(Text)

    summary = Column(Text)


class InterviewQuestion(Base):

    __tablename__ = "interview_questions"

    id = Column(Integer, primary_key=True, index=True)

    skill = Column(String)

    difficulty = Column(String)

    question = Column(Text)

    expected_topics = Column(JSON)

    type = Column(String)

    tags = Column(JSON)
