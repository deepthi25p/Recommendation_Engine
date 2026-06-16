from engine.orchestrator import (
    RecommendationOrchestrator
)


def test_recommendations():

    engine = (
        RecommendationOrchestrator()
    )

    recs = (
        engine.get_recommendations(
            1
        )
    )

    assert isinstance(
        recs,
        list
    )


def test_feedback():

    engine = (
        RecommendationOrchestrator()
    )

    engine.record_feedback(
        1,
        1,
        5
    )

    assert True