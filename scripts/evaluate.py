from engine.orchestrator import (
    RecommendationOrchestrator
)

from engine.evaluator import (
    Evaluator
)

engine = (
    RecommendationOrchestrator()
)

users = range(1, 11)

precisions = []
recalls = []
ndcgs = []

for user_id in users:

    recs = (
        engine.get_recommendations(
            user_id
        )
    )

    recommended = [
        r["content_id"]
        for r in recs
    ]

    # Dummy ground truth
    relevant = [1, 2, 3, 4, 5]

    precisions.append(
        Evaluator.precision_at_k(
            recommended,
            relevant
        )
    )

    recalls.append(
        Evaluator.recall_at_k(
            recommended,
            relevant
        )
    )

    ndcgs.append(
        Evaluator.ndcg_at_k(
            recommended,
            relevant
        )
    )

print(
    "Precision@5:",
    sum(precisions) /
    len(precisions)
)

print(
    "Recall@5:",
    sum(recalls) /
    len(recalls)
)

print(
    "NDCG@5:",
    sum(ndcgs) /
    len(ndcgs)
)