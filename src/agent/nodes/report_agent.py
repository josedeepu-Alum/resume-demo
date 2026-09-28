def report_agent(state):

    report = f"""
====================================================
JEV vs GPT-4o COMPARISON
====================================================

JOB REQUIREMENT
----------------------------------------------------

{state.job_requirement}

====================================================
JEV RESULTS
====================================================

Skill Match:
{state.jev_skill_match}

Experience Match:
{state.jev_experience_match}

Recommendation:
{state.jev_recommendation}

Input Tokens:
{state.jev_input_tokens}

Output Tokens:
{state.jev_output_tokens}

Total Tokens:
{state.jev_total_tokens}

====================================================
GPT-4o RESULTS
====================================================

Recommendation:
{state.gpt_recommendation}

Prompt Tokens:
{state.prompt_tokens}

Completion Tokens:
{state.completion_tokens}

Total Tokens:
{state.gpt_total_tokens}

Estimated Cost:
${state.gpt_cost}

====================================================
GPT RECRUITER ANALYSIS
====================================================

{state.gpt_review}

====================================================
OBSERVATIONS
====================================================

JEV

✓ Structured evaluation

✓ Deterministic scoring

✓ Lower hallucination risk

✓ Classification focused

✓ Output tokens currently free

GPT-4o

✓ Natural language reasoning

✓ Human friendly reports

✓ Interview questions

✓ Strong summarization

====================================================
RECOMMENDED ENTERPRISE PATTERN
====================================================

JEV
↓
Evaluation

GPT
↓
Explanation

====================================================
"""

    print(report)

    return {
        "final_report": report
    }