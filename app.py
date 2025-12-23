import streamlit as st

# Page configuration
st.set_page_config(
    page_title="🩺 AI Health FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #84fab0, #8fd3f4);
}
.chat-box {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.bot {
    color: #0b5394;
    font-weight: bold;
}
.user {
    color: #38761d;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🩺 AI Health FAQ Chatbot")
st.write("Ask basic health-related questions 👇")

# Health FAQ database
health_faq = {
    "fever": "Fever is a temporary increase in body temperature. Drink fluids and rest. Consult a doctor if it lasts more than 2 days.",
    "cold": "Common cold causes sneezing and runny nose. Rest, warm fluids, and steam inhalation can help.",
    "headache": "Headache can be caused by stress or dehydration. Drink water and take rest.",
    "diabetes": "Diabetes is a condition where blood sugar levels are high. It requires proper diet, exercise, and medication.",
    "blood pressure": "High blood pressure can increase heart risk. Reduce salt intake and exercise regularly.",
    "covid": "COVID-19 is a viral infection. Wear masks, maintain hygiene, and consult a doctor if symptoms appear."
}

# Chat input
user_input = st.text_input("💬 Enter your health question:")

if user_input:
    st.markdown(f"<div class='chat-box'><span class='user'>You:</span> {user_input}</div>", unsafe_allow_html=True)

    response = "Sorry, I can answer only basic health FAQs. Please consult a doctor."

    for key in health_faq:
        if key in user_input.lower():
            response = health_faq[key]
            break

    st.markdown(f"<div class='chat-box'><span class='bot'>Bot:</span> {response}</div>", unsafe_allow_html=True)

st.info("⚠️ This chatbot provides general health information only.")
