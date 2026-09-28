import pandas as pd
import streamlit as st

from agent.graph import graph

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Jev vs GPT-4o",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <div style="
        padding:20px;
        border-radius:15px;
        background:linear-gradient(90deg,#111827,#1f2937);
        color:white;
    ">
        <h1>🚀 Jev vs GPT-4o Enterprise AI Evaluation</h1>
        <p>
        Structured Evaluation vs Generative Reasoning
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==================================================
# INPUT SECTION
# ==================================================

col1, col2 = st.columns([1, 2])

with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

with col2:

    job_requirement = st.text_area(
        "Job Requirement",
        height=220,
        value="""
Senior AI Engineer

Required Skills

- Python
- Azure
- LangGraph
- LangChain
- RAG
- Vector Databases
"""
    )

# ==================================================
# EVALUATION BUTTON
# ==================================================

if st.button("🚀 Run Evaluation"):

    if uploaded_file is None:

        st.error(
            "Please upload a resume."
        )

    else:

        with open(
            uploaded_file.name,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        with st.spinner(
            "Evaluating candidate..."
        ):

            result = graph.invoke(
                {
                    "file_path":
                    uploaded_file.name,

                    "job_requirement":
                    job_requirement
                }
            )

        st.success(
            "Evaluation Complete"
        )

        # ==========================================
        # EXECUTIVE SUMMARY
        # ==========================================

        st.markdown("---")

        st.header(
            "📊 Executive Summary"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "JEV",
                result.get(
                    "jev_recommendation",
                    "-"
                )
            )

        with c2:

            st.metric(
                "GPT",
                result.get(
                    "gpt_recommendation",
                    "-"
                )
            )

        with c3:

            st.metric(
                "JEV Tokens",
                result.get(
                    "jev_total_tokens",
                    0
                )
            )

        with c4:

            st.metric(
                "GPT Tokens",
                result.get(
                    "gpt_total_tokens",
                    0
                )
            )

        # ==========================================
        # AGREEMENT
        # ==========================================

        same_decision = (
            result.get(
                "jev_recommendation"
            )
            ==
            result.get(
                "gpt_recommendation"
            )
        )

        if same_decision:

            st.success(
                f"""
✅ Both models agree.

Recommendation:

{result.get('jev_recommendation')}
"""
            )

        else:

            st.warning(
                f"""
⚠️ Models disagree.

JEV:
{result.get('jev_recommendation')}

GPT:
{result.get('gpt_recommendation')}
"""
            )

        # ==========================================
        # TOKEN CHART
        # ==========================================

        st.markdown("---")

        st.subheader(
            "📈 Token Comparison"
        )

        token_df = pd.DataFrame(
            {
                "Model":
                ["JEV", "GPT"],

                "Input Tokens":
                [
                    result.get(
                        "jev_input_tokens",
                        0
                    ),
                    result.get(
                        "prompt_tokens",
                        0
                    )
                ],

                "Output Tokens":
                [
                    result.get(
                        "jev_output_tokens",
                        0
                    ),
                    result.get(
                        "completion_tokens",
                        0
                    )
                ]
            }
        )

        st.bar_chart(
            token_df.set_index(
                "Model"
            )
        )

        # ==========================================
        # MAIN TABS
        # ==========================================

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "📊 Summary",
                "🤖 JEV",
                "🧠 GPT",
                "⚖️ Comparison",
                "🔍 Raw Response"
            ]
        )

        # ==========================================
        # SUMMARY TAB
        # ==========================================

        with tab1:

            st.subheader(
                "Business Insight"
            )

            st.info(
                """
JEV focuses on structured evaluation,
classification and deterministic scoring.

GPT focuses on reasoning,
summarization and explanation.
"""
            )

            st.markdown(
                """
### Recommended Enterprise Pattern

✅ JEV → Evaluate

✅ GPT → Explain
"""
            )

        # ==========================================
        # JEV TAB
        # ==========================================

        with tab2:

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Skill Match %",
                    result.get(
                        "jev_skill_match",
                        0
                    )
                )

                st.metric(
                    "Experience Match %",
                    result.get(
                        "jev_experience_match",
                        0
                    )
                )

                st.metric(
                    "Recommendation",
                    result.get(
                        "jev_recommendation",
                        "-"
                    )
                )

            with col2:

                st.metric(
                    "Input Tokens",
                    result.get(
                        "jev_input_tokens",
                        0
                    )
                )

                st.metric(
                    "Output Tokens",
                    result.get(
                        "jev_output_tokens",
                        0
                    )
                )

                st.metric(
                    "Total Tokens",
                    result.get(
                        "jev_total_tokens",
                        0
                    )
                )

            st.success(
                """
✅ Structured Evaluation

✅ Lower Hallucination Risk

✅ Deterministic Decisions

✅ Classification Focused

✅ Output Tokens Currently Free
"""
            )

        # ==========================================
        # GPT TAB
        # ==========================================

        with tab3:

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Prompt Tokens",
                    result.get(
                        "prompt_tokens",
                        0
                    )
                )

                st.metric(
                    "Completion Tokens",
                    result.get(
                        "completion_tokens",
                        0
                    )
                )

                st.metric(
                    "Total Tokens",
                    result.get(
                        "gpt_total_tokens",
                        0
                    )
                )

            with c2:

                st.metric(
                    "Estimated Cost",
                    f"${result.get('gpt_cost',0)}"
                )

                st.metric(
                    "Recommendation",
                    result.get(
                        "gpt_recommendation",
                        "-"
                    )
                )

            st.markdown(
                "### GPT Analysis"
            )

            st.write(
                result.get(
                    "gpt_review",
                    ""
                )
            )

        # ==========================================
        # COMPARISON TAB
        # ==========================================

        with tab4:

            comparison_df = pd.DataFrame(
                {
                    "Metric": [
                        "Recommendation",
                        "Input Tokens",
                        "Output Tokens",
                        "Total Tokens"
                    ],

                    "JEV": [
                        result.get(
                            "jev_recommendation"
                        ),

                        result.get(
                            "jev_input_tokens"
                        ),

                        result.get(
                            "jev_output_tokens"
                        ),

                        result.get(
                            "jev_total_tokens"
                        )
                    ],

                    "GPT": [
                        result.get(
                            "gpt_recommendation"
                        ),

                        result.get(
                            "prompt_tokens"
                        ),

                        result.get(
                            "completion_tokens"
                        ),

                        result.get(
                            "gpt_total_tokens"
                        )
                    ]
                }
            )

            st.dataframe(
                comparison_df,
                use_container_width=True
            )

            st.markdown(
                """
### Key Takeaways

#### JEV

- Structured evaluation
- Deterministic scoring
- Lower hallucination risk
- Classification oriented

#### GPT

- Rich explanations
- Recruiter-style reasoning
- Better summaries
- Better interview questions
"""
            )

        # ==========================================
        # RAW RESPONSE TAB
        # ==========================================

        with tab5:

            st.subheader(
                "Raw JEV Response"
            )

            st.code(
                result.get(
                    "jev_raw_response",
                    ""
                ),
                language="json"
            )