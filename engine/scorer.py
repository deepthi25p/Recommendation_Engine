class RecommendationScorer:

    def score(
            self,
            content,
            user_skills=None):

        score = 0

        score += content.popularity * 0.6

        if user_skills:
            score += 0.4

        return round(score, 3)