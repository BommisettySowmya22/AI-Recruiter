import pandas as pd

def save_submission(results):

    rows = []

    for i, r in enumerate(results, start=1):

        reasoning = "; ".join(r["reasons"])

        rows.append({

            "candidate_id": r["candidate_id"],

            "rank": i,

            "score": round(r["final_score"], 2),

            "reasoning": reasoning

        })

    submission = pd.DataFrame(rows)

    submission.to_csv(
        "outputs/submission.csv",
        index=False
    )

    print("Submission Saved Successfully!")