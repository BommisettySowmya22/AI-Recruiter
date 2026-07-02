def build_candidate_text(candidate):

    text = ""

    # Basic Information
    text += candidate.get("headline", "") + " "

    # Skills
    skills = candidate.get("skills", [])

    for skill in skills:
        text += skill.get("name", "") + " "

    # Work Experience
    experience = candidate.get("experience", [])

    for job in experience:
        text += job.get("title", "") + " "
        text += job.get("company", "") + " "
        text += job.get("description", "") + " "

    # Projects
    projects = candidate.get("projects", [])

    for project in projects:
        text += project.get("title", "") + " "
        text += project.get("description", "") + " "

    return text