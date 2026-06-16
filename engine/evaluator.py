import math


class Evaluator:

    @staticmethod
    def precision_at_k(
            recommended,
            relevant,
            k=5):

        recommended = recommended[:k]

        hits = len(
            set(recommended)
            &
            set(relevant)
        )

        return hits / k

    @staticmethod
    def recall_at_k(
            recommended,
            relevant,
            k=5):

        recommended = recommended[:k]

        hits = len(
            set(recommended)
            &
            set(relevant)
        )

        if len(relevant) == 0:
            return 0

        return hits / len(relevant)

    @staticmethod
    def ndcg_at_k(
            recommended,
            relevant,
            k=5):

        dcg = 0

        for i, item in enumerate(
                recommended[:k]):

            if item in relevant:
                dcg += 1 / math.log2(i + 2)

        ideal = sum(
            1 / math.log2(i + 2)
            for i in range(
                min(len(relevant), k)
            )
        )

        if ideal == 0:
            return 0

        return dcg / ideal