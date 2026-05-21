from sqlalchemy import Column, Integer, String, Text

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