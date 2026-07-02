def calculate_score(candidate, semantic_score):

    score = semantic_score * 45

    # -----------------------
    # Skills Score
    # -----------------------

    skills = candidate.get("skills", [])

    skill_score = 0

    for skill in skills:

        proficiency = skill.get("proficiency", "").lower()

        if proficiency == "advanced":
            skill_score += 3

        elif proficiency == "intermediate":
            skill_score += 2

        else:
            skill_score += 1

        skill_score += skill.get("endorsements", 0) * 0.05

    score += min(skill_score,20)

    # -----------------------
    # Behaviour
    # -----------------------

    signals = candidate.get("redrob_signals",{})

    behaviour = (

        signals.get("profile_completeness_score",0)/100

        + signals.get("github_activity_score",0)/10

        + signals.get("interview_completion_rate",0)

        + signals.get("offer_acceptance_rate",0)

    )

    score += behaviour*2.5


    # Verification Bonus
   

    if signals.get("verified_email",False):
        score += 1

    if signals.get("verified_phone",False):
        score += 1

    return round(score,2)