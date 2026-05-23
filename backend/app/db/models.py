from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

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


class InterviewSession(Base):

    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer, ForeignKey("candidate_profiles.id"))

    started_at = Column(DateTime, default=datetime.utcnow)

    status = Column(String, default="started")


class InterviewAnswer(Base):

    __tablename__ = "interview_answers"

    question_id = Column(Integer)

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer, ForeignKey("interview_sessions.id"))

    question = Column(Text)

    answer = Column(Text)

    score = Column(Integer)

    feedback = Column(Text)
