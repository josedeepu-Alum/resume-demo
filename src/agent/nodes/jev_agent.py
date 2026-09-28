import json
import os

import requests


def jev_agent(state):

    skill_levels = [
        "Poor Match",
        "Partial Match",
        "Good Match",
        "Strong Match",
        "Excellent Match"
    ]

    experience_levels = [
        "No Relevant Experience",
        "Limited Experience",
        "Relevant Experience",
        "Strong Experience",
        "Excellent Experience"
    ]

    payload = {

        "model": "jev-latest",

        "state": f"""
Job Requirement

{state.job_requirement}

Resume

{state.resume_text}
""",

        "questions": {

            "skill_match": {

                "type": "score",

                "instructions":
                    "How well do the candidate skills match the job requirement?",

                "criteria":
                    skill_levels
            },

            "experience_match": {

                "type": "score",

                "instructions":
                    "How well does the candidate experience match the job requirement?",

                "criteria":
                    experience_levels
            },

            "hire_decision": {

                "type": "choice",

                "instructions":
                    "What should be the hiring recommendation?",

                "criteria": {

                    "REJECT":
                        "Candidate does not meet requirements",

                    "MAYBE":
                        "Candidate partially matches",

                    "SHORTLIST":
                        "Candidate strongly matches"
                }
            }
        }
    }

    response = requests.post(
        "https://api.typesafe.ai/v1/systemone",
        headers={
            "Authorization":
                f"Bearer {os.getenv('TYPESAFE_API_KEY')}",
            "Content-Type":
                "application/json"
        },
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    print(
        json.dumps(
            data,
            indent=2
        )
    )

    answers = data.get(
        "answers",
        {}
    )

    usage = data.get(
        "usage",
        {}
    )

    skill_answer = answers.get(
        "skill_match",
        {}
    )

    experience_answer = answers.get(
        "experience_match",
        {}
    )

    decision_answer = answers.get(
        "hire_decision",
        {}
    )

    skill_score = float(
        skill_answer.get(
            "score",
            0
        )
    )

    experience_score = float(
        experience_answer.get(
            "score",
            0
        )
    )

    skill_max = (
        len(skill_levels) - 1
    )

    experience_max = (
        len(experience_levels) - 1
    )

    skill_percent = round(
        (skill_score / skill_max) * 100,
        1
    )

    experience_percent = round(
        (experience_score / experience_max) * 100,
        1
    )

    input_tokens = usage.get(
        "input_tokens",
        0
    )

    output_tokens = usage.get(
        "output_tokens",
        0
    )

    return {

        "jev_raw_response":
            json.dumps(
                data,
                indent=2
            ),

        "jev_skill_raw_score":
            skill_score,

        "jev_experience_raw_score":
            experience_score,

        "jev_skill_match":
            skill_percent,

        "jev_experience_match":
            experience_percent,

        "jev_recommendation":
            decision_answer.get(
                "choice",
                "UNKNOWN"
            ),

        "jev_input_tokens":
            input_tokens,

        "jev_output_tokens":
            output_tokens,

        "jev_total_tokens":
            input_tokens + output_tokens
    }