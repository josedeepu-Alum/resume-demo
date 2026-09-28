from langgraph.graph import (
    START,
    END,
    StateGraph
)

from agent.state import State

from agent.nodes.document_reader import (
    document_reader
)

from agent.nodes.jev_agent import (
    jev_agent
)

from agent.nodes.gpt_agent import (
    gpt_agent
)

from agent.nodes.comparison_agent import (
    comparison_agent
)

from agent.nodes.report_agent import (
    report_agent
)

builder = StateGraph(
    State
)

builder.add_node(
    "document_reader",
    document_reader
)

builder.add_node(
    "jev_agent",
    jev_agent
)

builder.add_node(
    "gpt_agent",
    gpt_agent
)

builder.add_node(
    "comparison_agent",
    comparison_agent
)

builder.add_node(
    "report_agent",
    report_agent
)

builder.add_edge(
    START,
    "document_reader"
)

builder.add_edge(
    "document_reader",
    "jev_agent"
)

builder.add_edge(
    "jev_agent",
    "gpt_agent"
)

builder.add_edge(
    "gpt_agent",
    "comparison_agent"
)

builder.add_edge(
    "comparison_agent",
    "report_agent"
)

builder.add_edge(
    "report_agent",
    END
)

graph = builder.compile(
    name="JEV_vs_GPT_Comparison"
)