from docx import Document
import json
from tqdm import tqdm

from src.embedding import get_embedding
from src.candidate_parser import build_candidate_text
from src.faiss_index import build_index, search
from src.scorer import calculate_score
from src.explain import explain
from src.submission import save_submission



#  Read Job Description


print("=" * 60)
print("Loading Job Description...")
print("=" * 60)

doc = Document("data/job_description.docx")

jd = ""

for para in doc.paragraphs:
    jd += para.text + "\n"

print("Job Description Loaded Successfully!\n")



#  Read Candidates


print("=" * 60)
print("Loading Candidates...")
print("=" * 60)

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

print(f"Total Candidates : {len(candidates)}\n")



#  Build Candidate Embeddings


print("=" * 60)
print("Building Candidate Embeddings...")
print("=" * 60)

candidate_embeddings = []

TEST_SIZE = len(candidates)

for candidate in tqdm(candidates[:TEST_SIZE]):

    text = build_candidate_text(candidate)

    embedding = get_embedding(text)

    candidate_embeddings.append(embedding)

print("\nCandidate Embeddings Created Successfully!\n")



#  Build FAISS Index


print("=" * 60)
print("Building FAISS Index...")
print("=" * 60)

index = build_index(candidate_embeddings)

print("FAISS Index Ready!\n")



#  Job Embedding


print("=" * 60)
print("Creating Job Embedding...")
print("=" * 60)

job_embedding = get_embedding(jd)

print("Job Embedding Created!\n")



#  Search Top Candidates


print("=" * 60)
print("Searching Top Candidates...")
print("=" * 60)



scores, ids = search(
    index=index,
    query_embedding=job_embedding,
    k=100
)

print("Search Completed!\n")



#  Re-ranking


print("=" * 60)
print("Re-ranking Candidates...")
print("=" * 60)

results = []

for semantic, candidate_index in zip(scores, ids):

    candidate = candidates[candidate_index]

    final_score = calculate_score(
        candidate,
        float(semantic)
    )

    reasons = explain(candidate)

    results.append({

        "candidate_id": candidate.get("candidate_id", candidate_index),

        "candidate_index": candidate_index,

        "semantic_score": float(semantic),

        "final_score": final_score,

        "candidate": candidate,

        "reasons": reasons

    })



#  Sort


results = sorted(
    results,
    key=lambda x: x["final_score"],
    reverse=True
)



#  Display Ranking


print("\n")
print("=" * 60)
print("FINAL RANKING")
print("=" * 60)

for rank, item in enumerate(results, start=1):

    print(f"\nRank {rank}")

    print("Candidate :", item["candidate_index"])

    print("Semantic Score :", round(item["semantic_score"], 4))

    print("Final Score :", item["final_score"])

    print("Reasons:")

    for reason in item["reasons"]:
        print("  ✔", reason)



#  Save Top 100


print("\nSaving Top Candidates...\n")

top_candidates = results[:100]

for i, candidate in enumerate(top_candidates, start=1):

    print(
        f"Rank {i} -> Candidate {candidate['candidate_index']}  Score = {candidate['final_score']}"
    )



#  Save Submission


save_submission(top_candidates)

print("\nSubmission Generated Successfully!")
