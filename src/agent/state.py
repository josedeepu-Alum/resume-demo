from dataclasses import dataclass


@dataclass
class State:

    # Input

    file_path: str = ""

    job_requirement: str = ""

    resume_text: str = ""

    # -----------------------------
    # JEV RESULTS
    # -----------------------------

    jev_raw_response: str = ""

    jev_skill_raw_score: float = 0.0

    jev_experience_raw_score: float = 0.0

    jev_skill_match: float = 0.0

    jev_experience_match: float = 0.0

    jev_recommendation: str = ""

    jev_input_tokens: int = 0

    jev_output_tokens: int = 0

    jev_total_tokens: int = 0

    # -----------------------------
    # GPT RESULTS
    # -----------------------------

    gpt_review: str = ""

    gpt_recommendation: str = ""

    model_name: str = "gpt-4o"

    prompt_tokens: int = 0

    completion_tokens: int = 0

    gpt_total_tokens: int = 0

    gpt_cost: float = 0.0

    # -----------------------------
    # COMPARISON
    # -----------------------------

    token_difference: int = 0

    input_token_difference: int = 0

    output_token_difference: int = 0

    cheaper_model: str = ""

    recommendation_match: bool = False

    overall_winner: str = ""

    insight: str = ""

    # -----------------------------
    # REPORTING
    # -----------------------------

    final_report: str = ""