import streamlit as st
import google.generativeai as genai
from google.colab import userdata

# --- Configuration and Secrets ---
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Your WhatsApp-enabled phone number for live support (include country code)
WHATSAPP_CONTACT_NUMBER = "+2348024541916" # Replace with your actual WhatsApp number

# --- Gemini Model Initialization ---
# The system instruction guides the AI's behavior and ensures it refers to a human when needed.
SYSTEM_INSTRUCTION = f"""You are an AI assistant for a coding academy. Your primary goal is to answer questions related to our courses, enrollment process, coding concepts, and general academy information. 

If a question is outside your knowledge domain, is too complex for you to answer accurately, or if the user explicitly asks to speak to a human, you MUST respond with a specific phrase indicating the need for live support. Use the exact phrase: 'I'm sorry, but that's a bit beyond my current capabilities. Please contact our support team directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER} for personalized assistance.'

Be dynamic, friendly, and helpful. Keep responses concise and to the point.
"""

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    system_instruction=SYSTEM_INSTRUCTION
)

# --- Streamlit App Setup ---
st.set_page_config(
    page_title="🤖 Coding Academy AI Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS for a sweeter design (minimal example)
st.markdown("""
<style>
.main {{ background-color: #f0f2f6; }}
.stApp {{ max-width: 800px; margin: auto; padding-top: 2rem; }}
.stButton>button {{ background-color: #4CAF50; color: white; font-weight: bold; border-radius: 5px; }}
.stTextInput>div>div>input {{ border-radius: 5px; }}
.chat-message {{ padding: 10px; border-radius: 10px; margin-bottom: 10px; }}
.user-message {{ background-color: #e6f7ff; text-align: right; }}
.ai-message {{ background-color: #f0f0f0; text-align: left; }}
.whatsapp-link {{ text-align: center; margin-top: 20px; }}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Coding Academy AI Assistant")
st.markdown("#### Your smart helper for all things coding academy!")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- Display Chat Messages ---
for role, text in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='chat-message user-message'>**You:** {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-message ai-message'>**AI:** {text}</div>", unsafe_allow_html=True)

# --- User Input and AI Response ---
user_query = st.chat_input("Ask me anything about the coding academy...")

if user_query:
    st.session_state.chat_history.append(("user", user_query))
    st.markdown(f"<div class='chat-message user-message'>**You:** {user_query}</div>", unsafe_allow_html=True)

    # Generate AI response
    try:
        response = model.generate_content(user_query)
        ai_response_text = response.text
        
        # Check if AI suggests contacting human
        if f"contact our support team directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER}" in ai_response_text:
            st.session_state.chat_history.append(("ai", ai_response_text))
            st.markdown(f"<div class='chat-message ai-message'>**AI:** {ai_response_text}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='whatsapp-link'><a href='https://wa.me/{WHATSAPP_CONTACT_NUMBER.replace('+', '')}' target='_blank'>➡️ **Click here to chat with us on WhatsApp!** ⬅️</a></div>", unsafe_allow_html=True)
        else:
            st.session_state.chat_history.append(("ai", ai_response_text))
            st.markdown(f"<div class='chat-message ai-message'>**AI:** {ai_response_text}</div>", unsafe_allow_html=True)

    except Exception as e:
        error_message = f"AI assistant is currently unavailable. Please try again later or contact support directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER}."
        st.session_state.chat_history.append(("ai", error_message))
        st.markdown(f"<div class='chat-message ai-message' style='color: red;'>**AI:** {error_message}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='whatsapp-link'><a href='https://wa.me/{WHATSAPP_CONTACT_NUMBER.replace('+', '')}' target='_blank'>➡️ **Click here to chat with us on WhatsApp!** ⬅️</a></div>", unsafe_allow_html=True)


# Instructions for deployment
st.markdown("""
---
### How to Run and Deploy This App:
1.  **Replace Placeholders:** Update `WHATSAPP_CONTACT_NUMBER` with your actual WhatsApp number.
2.  **API Key:** Ensure `GOOGLE_API_KEY` is securely stored in Colab Secrets.
3.  **Run this cell** in your Colab notebook.
4.  Streamlit will provide a **public URL**. Click on it to open your interactive chatbot in a new browser tab.
5.  For **web deployment**, you would typically host this `streamlit run your_app.py` on platforms like Streamlit Community Cloud, Heroku, Render, or your own server.

**Note:** The system instruction for the Gemini model is crucial for handling referrals. Make sure the model's response for human contact matches the phrase used in the code for detection.
""")
