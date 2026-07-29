import streamlit as st
from agents.graph import tourism_graph

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Sri Lanka Tourism AI",
    page_icon="🇱🇰",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#262e27;
}

h1,h2,h3{
    color:#00695C;
}

.block-container{
    padding-top:2rem;
}

div[data-testid="stSidebar"]{
    background-color:#1f2520;
}

.stButton>button{
    width:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.image("images/logo.jpeg", width=150)

    st.title("Sri Lanka Tourism AI")

    st.success("🌴 Welcome to Sri Lanka Tourism AI!")

    st.info("""
Plan your dream trip with AI.

• Tourism Information

• Smart Itineraries

• Hotel Suggestions

• Budget Estimation

• Local Travel Tips
""")

    st.markdown("---")

    model = st.selectbox(
        "AI Model",
        [
            "Groq",
            "OpenRouter"
        ]
    )

    traveler = st.selectbox(
        "Traveller Type",
        [
            "Solo",
            "Couple",
            "Family",
            "Friends"
        ]
    )

    budget = st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "Luxury"
        ]
    )

    days = st.slider(
        "Trip Days",
        1,
        14,
        5
    )

    st.markdown("---")

    st.markdown("""
### 🚀 Features

- 🇱🇰 Tourism Q&A
- 🗺 AI Trip Planner
- 🏨 Hotel Recommendations
- 💰 Budget Estimator
- 🚗 Transport Advice
- 🍛 Local Food Suggestions
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Version 1.0")

# --------------------------------
# HERO SECTION
# --------------------------------

st.image(
    "images/hero.jpeg",
    use_container_width=True
)

st.title(" Sri Lanka Tourism Micro-Business Assistant")

st.caption(
    "Plan your perfect Sri Lanka holiday using AI-powered travel planning."
)

st.success(
    "✨ Discover Sri Lanka with AI-powered travel planning."
)

st.markdown("""
### 🤖 What can I help you with?

Ask about:

- Tourist Attractions
- Hotels
- Transport
- Local Foods
- Travel Budgets
- Complete Travel Plans
""")

# --------------------------------
# QUICK ACTIONS
# --------------------------------

st.subheader("⚡ Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🗺 Plan Trip"):
        st.session_state.quick = "Plan a 5 day Sri Lanka trip"

with c2:
    if st.button("🏨 Hotels"):
        st.session_state.quick = "Recommend hotels in Sri Lanka"

with c3:
    if st.button("🍛 Foods"):
        st.session_state.quick = "Best local foods in Sri Lanka"

with c4:
    if st.button("💰 Budget"):
        st.session_state.quick = "Estimate travel budget"

st.divider()

# --------------------------------
# DESTINATIONS
# --------------------------------

st.subheader("🌴 Popular Destinations")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("images/sigiriya.jpeg")
    st.markdown("### Sigiriya")
    st.caption("UNESCO World Heritage Site")

with col2:
    st.image("images/ella.jpeg")
    st.markdown("### Ella")
    st.caption("Tea Country")

with col3:
    st.image("images/mirissa.jpeg")
    st.markdown("### Mirissa")
    st.caption("Whale Watching")

with col4:
    st.image("images/yala.jpeg")
    st.markdown("### Yala")
    st.caption("Wildlife Safari")

st.info(
    "📍 Explore beaches, mountains, wildlife parks, historical sites and cultural attractions across Sri Lanka."
)

st.divider()

# --------------------------------
# CHAT
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input(
    "Ask anything about Sri Lanka Tourism..."
)

if "quick" in st.session_state:
    prompt = st.session_state.quick
    del st.session_state.quick

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 Planning your journey..."):

        result = tourism_graph.invoke(
            {
                "user_input": prompt,
                "response": ""
            }
        )

        answer = result["response"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

st.markdown("---")

st.caption(
    " Sri Lanka Tourism Micro-Business Assistant | Powered by LangGraph • FAISS • Groq • OpenRouter • Streamlit"
)