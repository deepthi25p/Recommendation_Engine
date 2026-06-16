from collections import defaultdict


class CandidateGenerator:

    def generate_candidates(
            self,
            user_history,
            all_content):

        interacted = {
            item.content_id
            for item in user_history
        }

        candidates = []

        for content in all_content:
            if content.id not in interacted:
                candidates.append(content)

        return candidates