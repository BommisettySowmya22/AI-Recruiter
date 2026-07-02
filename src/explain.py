def explain(candidate):

    reasons=[]

    skills=candidate.get("skills",[])

    advanced=[]

    for skill in skills:

        if skill.get("proficiency","").lower()=="advanced":

            advanced.append(skill["name"])

    if advanced:

        reasons.append(
            "Advanced Skills: "
            + ", ".join(advanced[:5])
        )

    signals=candidate.get("redrob_signals",{})

    if signals.get("github_activity_score",0)>7:

        reasons.append("Strong GitHub Activity")

    if signals.get("profile_completeness_score",0)>80:

        reasons.append("Complete Profile")

    if signals.get("interview_completion_rate",0)>0.7:

        reasons.append("High Interview Completion")

    return reasons