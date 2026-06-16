from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime

from data.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    interests = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    skills = relationship("UserSkill", back_populates="user")
    interactions = relationship("Interaction", back_populates="user")


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String)
    difficulty = Column(String)
    popularity = Column(Float, default=0)

    skills = relationship("ContentSkill", back_populates="content")
    interactions = relationship("Interaction", back_populates="content")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    users = relationship("UserSkill", back_populates="skill")
    contents = relationship("ContentSkill", back_populates="skill")


class UserSkill(Base):
    __tablename__ = "user_skills"

    user_id = Column(Integer,
                     ForeignKey("users.id"),
                     primary_key=True)

    skill_id = Column(Integer,
                      ForeignKey("skills.id"),
                      primary_key=True)

    proficiency = Column(Float, default=1.0)

    user = relationship("User", back_populates="skills")
    skill = relationship("Skill", back_populates="users")


class ContentSkill(Base):
    __tablename__ = "content_skills"

    content_id = Column(Integer,
                        ForeignKey("content.id"),
                        primary_key=True)

    skill_id = Column(Integer,
                      ForeignKey("skills.id"),
                      primary_key=True)

    content = relationship("Content", back_populates="skills")
    skill = relationship("Skill", back_populates="contents")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("content.id"))

    type = Column(String)
    rating = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship("User", back_populates="interactions")
    content = relationship("Content", back_populates="interactions")