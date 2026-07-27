from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_openrouter_llm


class BudgetAgent:

    def __init__(self):

        self.llm = get_openrouter_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are a Sri Lanka Tourism Budget Advisor.

Use the tourism information below when preparing the budget.

Tourism Information:
{tourism_info}

User Request:
{request}

Prepare an estimated budget including:

- Accommodation
- Food
- Local transport
- Attractions
- Miscellaneous expenses
- Total Estimated Cost

Important:

- Mention that prices are estimates.
- Use Sri Lankan Rupees (LKR).
- Suggest cost-saving tips where possible.
"""
        )

    def estimate_budget(self, request, tourism_info):

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "request": request,
                "tourism_info": tourism_info
            }
        )

        return response.content