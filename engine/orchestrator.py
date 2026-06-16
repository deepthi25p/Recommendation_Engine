from data.database import SessionLocal
from data.repositories import (
    UserRepository,
    ContentRepository,
    InteractionRepository
)

from engine.candidate_gen import CandidateGenerator
from engine.scorer import RecommendationScorer


class RecommendationOrchestrator:

    def __init__(self):

        self.cache = {}

        self.db = SessionLocal()

        self.user_repo = UserRepository(
            self.db
        )

        self.content_repo = ContentRepository(
            self.db
        )

        self.interaction_repo = (
            InteractionRepository(
                self.db
            )
        )

        self.generator = CandidateGenerator()

        self.scorer = RecommendationScorer()

    def get_recommendations(
            self,
            user_id,
            limit=5):

        if user_id in self.cache:
            return self.cache[user_id]

        user = self.user_repo.get_user(
            user_id
        )

        if not user:
            return []

        history = (
            self.user_repo
            .get_user_history(
                user_id
            )
        )

        # Cold start
        if len(history) == 0:

            popular = (
                self.content_repo
                .get_popular_content(
                    limit
                )
            )

            result = []

            for item in popular:
                result.append(
                    {
                        "content_id":
                        item.id,

                        "title":
                        item.title,

                        "score":
                        item.popularity,

                        "reason":
                        "Popular content"
                    }
                )

            return result

        all_content = (
            self.content_repo
            .get_all_content()
        )

        candidates = (
            self.generator
            .generate_candidates(
                history,
                all_content
            )
        )

        recommendations = []

        user_skills = (
            self.user_repo
            .get_user_skills(
                user_id
            )
        )

        for content in candidates:

            score = self.scorer.score(
                content,
                user_skills
            )

            recommendations.append(
                {
                    "content_id":
                    content.id,

                    "title":
                    content.title,

                    "score":
                    score,

                    "reason":
                    "Matches user interests"
                }
            )

        recommendations.sort(
            key=lambda x:
            x["score"],
            reverse=True
        )

        recommendations = recommendations[
            :limit
        ]

        self.cache[user_id] = (
            recommendations
        )

        return recommendations

    def record_feedback(
            self,
            user_id,
            content_id,
            rating):

        self.interaction_repo.record_interaction(
            user_id,
            content_id,
            "rating",
            rating
        )

        if user_id in self.cache:
            del self.cache[user_id]