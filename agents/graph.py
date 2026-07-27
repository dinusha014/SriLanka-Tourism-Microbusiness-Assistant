from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.rag_agent import RAGAgent
from agents.Planner_agent import PlannerAgent
from agents.Booking_agent import BookingAgent
from agents.budget_agent import BudgetAgent


# Initialise all agents
rag = RAGAgent()
planner = PlannerAgent()
booking = BookingAgent()
budget = BudgetAgent()


class AgentState(TypedDict):
    """Shared state used across the LangGraph workflow."""

    user_input: str
    response: str


def supervisor(state: AgentState):
    """
    Route the user's request to the most suitable AI agent
    and combine the responses when multiple intents are detected.
    """

    query = state["user_input"]
    tourism_info = rag.get_context(query)

    query_lower = query.lower()
    sections = []

    planner_keywords = [
        "plan", "trip", "itinerary",
        "travel", "visit", "holiday"
    ]

    booking_keywords = [
        "hotel", "stay", "book",
        "transport", "accommodation"
    ]

    budget_keywords = [
        "budget", "cost", "price",
        "expense", "money"
    ]

    # Travel planner
    if any(word in query_lower for word in planner_keywords):
        sections.append(
            "# Travel Plan\n\n"
            + planner.create_plan(query, tourism_info)
        )

    # Booking assistant
    if any(word in query_lower for word in booking_keywords):
        sections.append(
            "# Accommodation & Transport\n\n"
            + booking.booking_help(query, tourism_info)
        )

    # Budget estimator
    if any(word in query_lower for word in budget_keywords):
        sections.append(
            "# Budget Estimate\n\n"
            + budget.estimate_budget(query, tourism_info)
        )

    # Default RAG response
    if not sections:
        sections.append(
            rag.answer_question(query)
        )

    final_answer = "\n\n---\n\n".join(sections)

    return {
        "user_input": query,
        "response": final_answer
    }


# Build LangGraph workflow
builder = StateGraph(AgentState)

builder.add_node("supervisor", supervisor)

builder.set_entry_point("supervisor")

builder.add_edge("supervisor", END)
# Compile the LangGraph workflow into an executable graph.
tourism_graph = builder.compile()