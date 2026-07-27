from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_openrouter_llm


class PlannerAgent:
    """
    Planner Agent

    Generates personalised Sri Lankan travel itineraries
    using tourism information retrieved from the RAG system.
    """

    def __init__(self):

        # Load OpenRouter LLM
        self.llm = get_openrouter_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert Sri Lanka Travel Planner.

Your responsibilities are:

- Create realistic travel itineraries.
- Use ONLY the tourism information provided.
- Never invent destinations or activities.
- Recommend efficient travel routes.
- Suggest suitable attractions based on the user's request.
- Include useful travel tips.
- Keep recommendations practical and well organised.

Tourism Information:
{tourism_info}

User Request:
{request}

Prepare a travel plan including:

1. Day-by-day itinerary
2. Places to visit
3. Estimated travel time
4. Recommended transport
5. Best visiting hours
6. Local travel tips

Present the itinerary in a clear and professional format.
"""
        )

    def create_plan(self, request, tourism_info):

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "request": request,
                "tourism_info": tourism_info
            }
        )

        return response.content