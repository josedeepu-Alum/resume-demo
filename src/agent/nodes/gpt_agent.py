import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

MODEL_NAME = "gpt-4o"

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in .env file"
    )

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0,
    api_key=OPENAI_API_KEY
)

def gpt_agent(state):

    prompt = f"""
You are a strict Senior Technical Recruiter.

JOB REQUIREMENTS

{state.job_requirement}

RESUME

{state.resume_text}

Rules:

1. Compare ONLY against the stated job requirements.
2. Do not infer missing skills.
3. Do not assume experience not shown.
4. Missing critical skills must reduce suitability.

Recommendation Rules

SHORTLIST
- Candidate matches 80% or more of requirements.

MAYBE
- Candidate matches 50% to 79%.

REJECT
- Candidate matches below 50%.

Provide:

1. Summary

2. Matching Skills

3. Missing Skills

4. Match Percentage

5. Recommendation
(MUST be SHORTLIST, MAYBE, or REJECT)

6. Reason for Recommendation

7. Five Interview Questions
"""

    result = llm.invoke(prompt)

    review = result.content

    recommendation = "MAYBE"

    review_upper = review.upper()

    if "RECOMMENDATION" in review_upper:

        if "REJECT" in review_upper:
            recommendation = "REJECT"

        elif "SHORTLIST" in review_upper:
            recommendation = "SHORTLIST"

        elif "MAYBE" in review_upper:
            recommendation = "MAYBE"

    usage = result.response_metadata.get(
        "token_usage",
        {}
    )

    prompt_tokens = usage.get(
        "prompt_tokens",
        0
    )

    completion_tokens = usage.get(
        "completion_tokens",
        0
    )

    total_tokens = usage.get(
        "total_tokens",
        0
    )

    input_cost = (
        prompt_tokens / 1000
    ) * 0.0025

    output_cost = (
        completion_tokens / 1000
    ) * 0.0100

    return {

        "gpt_review":
            review,

        "gpt_recommendation":
            recommendation,

        "prompt_tokens":
            prompt_tokens,

        "completion_tokens":
            completion_tokens,

        "gpt_total_tokens":
            total_tokens,

        "gpt_cost":
            round(
                input_cost + output_cost,
                6
            )
    }