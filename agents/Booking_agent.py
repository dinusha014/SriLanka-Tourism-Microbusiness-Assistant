from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_groq_llm


class BookingAgent:
    """
    Booking Agent

    Provides accommodation and travel booking recommendations
    using tourism information retrieved from the RAG system.
    """

    def __init__(self):

        # Load Groq LLM
        self.llm = get_groq_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are a Sri Lanka Tourism Booking Assistant.

Your responsibilities are:

- Recommend suitable accommodation based ONLY on the tourism information.
- Suggest the best area to stay.
- Recommend suitable transport options.
- Provide useful booking advice.
- Offer practical travel tips.
- Never invent hotel names, prices or unavailable services.
- If booking information is unavailable, clearly mention that only general guidance can be provided.

Tourism Information:
{tourism_info}

User Request:
{request}

Prepare your response using the following sections:

1. Recommended Accommodation
2. Best Area to Stay
3. Transport Suggestions
4. Booking Advice
5. Helpful Travel Tips

Keep the response clear, concise and professional.
"""
        )

    def booking_help(self, request, tourism_info):
        """
        Generate booking recommendations.
        """

        if not tourism_info.strip():
            return (
                "I couldn't find enough tourism information "
                "to provide booking recommendations."
            )

        chain = self.prompt | self.llm

        # Handle unexpected runtime errors gracefully.
        try:

            response = chain.invoke(
                {
                    "request": request,
                    "tourism_info": tourism_info
                }
            )

            return response.content

        except Exception as e:

            return (
                f"Unable to generate booking recommendations: {str(e)}"
            )