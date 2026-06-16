from sqlalchemy.orm import Session
from data.models import *

from datetime import datetime,UTC


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id):
        return self.db.query(User).filter(
            User.id == user_id
        ).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_history(self, user_id):

        return (
            self.db.query(Interaction)
            .filter(
                Interaction.user_id == user_id
            )
            .all()
        )

    def get_user_skills(self, user_id):

        skills = (
            self.db.query(UserSkill)
            .filter(
                UserSkill.user_id == user_id
            )
            .all()
        )

        return [s.skill_id for s in skills]


class ContentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_content(self, content_id):
        return (
            self.db.query(Content)
            .filter(Content.id == content_id)
            .first()
        )

    def get_all_content(self):
        return self.db.query(Content).all()

    def get_popular_content(
            self,
            limit=10):

        return (
            self.db.query(Content)
            .order_by(
                Content.popularity.desc()
            )
            .limit(limit)
            .all()
        )

    def get_content_by_skills(
            self,
            skill_ids):

        content_skills = (
            self.db.query(ContentSkill)
            .filter(
                ContentSkill.skill_id.in_(
                    skill_ids
                )
            )
            .all()
        )

        content_ids = list(
            set(
                cs.content_id
                for cs in content_skills
            )
        )

        return (
            self.db.query(Content)
            .filter(
                Content.id.in_(
                    content_ids
                )
            )
            .all()
        )


class InteractionRepository:

    def __init__(self, db: Session):
        self.db = db

    def record_interaction(
            self,
            user_id,
            content_id,
            interaction_type,
            rating):

        interaction = Interaction(
            user_id=user_id,
            content_id=content_id,
            type=interaction_type,
            rating=rating,
            created_at=datetime.now(UTC)
        )

        self.db.add(interaction)
        self.db.commit()

        return interaction

    def get_user_ratings(
            self,
            user_id):

        interactions = (
            self.db.query(Interaction)
            .filter(
                Interaction.user_id == user_id
            )
            .all()
        )

        return {
            i.content_id: i.rating
            for i in interactions
            if i.rating is not None
        }