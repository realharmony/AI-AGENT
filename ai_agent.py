{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNslwQutxHvPdMMP5Yz3qyv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/realharmony/AI-AGENT/blob/main/ai_agent.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "79c1c62f",
        "outputId": "3ccfe420-e70e-471f-bb91-27a375699032"
      },
      "source": [
        "# Install necessary libraries\n",
        "!pip install streamlit google-generativeai"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.58.0)\n",
            "Requirement already satisfied: google-generativeai in /usr/local/lib/python3.12/dist-packages (0.8.6)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.4.1)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.50)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.2)\n",
            "Requirement already satisfied: pandas<4,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.2)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.52.1)\n",
            "Requirement already satisfied: uvicorn>=0.30.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.49.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.8.0)\n",
            "Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: python-multipart>=0.0.10 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.0.32)\n",
            "Requirement already satisfied: websockets>=12.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (15.0.1)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: google-ai-generativelanguage==0.6.15 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (0.6.15)\n",
            "Requirement already satisfied: google-api-core in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.30.3)\n",
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.197.0)\n",
            "Requirement already satisfied: google-auth>=2.15.0 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.47.0)\n",
            "Requirement already satisfied: pydantic in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.12.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (4.67.3)\n",
            "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /usr/local/lib/python3.12/dist-packages (from google-ai-generativelanguage==0.6.15->google-generativeai) (1.28.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.22.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio>=4.0.0->streamlit) (3.18)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.63.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core->google-generativeai) (1.75.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (4.9.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2026.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.5.20)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.12/dist-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)\n",
            "Requirement already satisfied: httplib2<1.0.0,>=0.19.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.31.2)\n",
            "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.4.0)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (4.2.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.41.4 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (2.41.4)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.81.1)\n",
            "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.71.2)\n",
            "Requirement already satisfied: pyparsing<4,>=3.1 in /usr/local/lib/python3.12/dist-packages (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai) (3.3.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2026.5.1)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.12/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=2.15.0->google-generativeai) (0.6.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f37c760b"
      },
      "source": [
        "### 1. Set up your API Keys and WhatsApp Contact\n",
        "\n",
        "To use the Gemini API, you'll need an API key. If you don't already have one, create a key in Google AI Studio. Add this key to Colab's Secrets manager under the \"🔑\" in the left panel, named `GOOGLE_API_KEY`.\n",
        "\n",
        "Also, define the `WHATSAPP_CONTACT_NUMBER` which the AI will use to refer users to a live person."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "feb337c5",
        "outputId": "6cad0893-07fd-4bcc-e683-dbeb4e9bce1b"
      },
      "source": [
        "import streamlit as st\n",
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "\n",
        "# --- Configuration and Secrets ---\n",
        "GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')\n",
        "genai.configure(api_key=GOOGLE_API_KEY)\n",
        "\n",
        "# Your WhatsApp-enabled phone number for live support (include country code)\n",
        "WHATSAPP_CONTACT_NUMBER = \"+2348024541916\" # Replace with your actual WhatsApp number\n",
        "\n",
        "# --- Gemini Model Initialization ---\n",
        "# The system instruction guides the AI's behavior and ensures it refers to a human when needed.\n",
        "SYSTEM_INSTRUCTION = f\"\"\"You are an AI assistant for a coding academy. Your primary goal is to answer questions related to our courses, enrollment process, coding concepts, and general academy information.\n",
        "\n",
        "If a question is outside your knowledge domain, is too complex for you to answer accurately, or if the user explicitly asks to speak to a human, you MUST respond with a specific phrase indicating the need for live support. Use the exact phrase: 'I'm sorry, but that's a bit beyond my current capabilities. Please contact our support team directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER} for personalized assistance.'\n",
        "\n",
        "Be dynamic, friendly, and helpful. Keep responses concise and to the point.\n",
        "\"\"\"\n",
        "\n",
        "model = genai.GenerativeModel(\n",
        "    model_name='gemini-1.5-flash-latest',\n",
        "    system_instruction=SYSTEM_INSTRUCTION\n",
        ")\n",
        "\n",
        "# --- Streamlit App Setup ---\n",
        "st.set_page_config(\n",
        "    page_title=\"🤖 Coding Academy AI Chat\",\n",
        "    page_icon=\"💬\",\n",
        "    layout=\"centered\",\n",
        "    initial_sidebar_state=\"auto\"\n",
        ")\n",
        "\n",
        "# Custom CSS for a sweeter design (minimal example)\n",
        "st.markdown(\"\"\"\n",
        "<style>\n",
        ".main {{ background-color: #f0f2f6; }}\n",
        ".stApp {{ max-width: 800px; margin: auto; padding-top: 2rem; }}\n",
        ".stButton>button {{ background-color: #4CAF50; color: white; font-weight: bold; border-radius: 5px; }}\n",
        ".stTextInput>div>div>input {{ border-radius: 5px; }}\n",
        ".chat-message {{ padding: 10px; border-radius: 10px; margin-bottom: 10px; }}\n",
        ".user-message {{ background-color: #e6f7ff; text-align: right; }}\n",
        ".ai-message {{ background-color: #f0f0f0; text-align: left; }}\n",
        ".whatsapp-link {{ text-align: center; margin-top: 20px; }}\n",
        "</style>\n",
        "\"\"\", unsafe_allow_html=True)\n",
        "\n",
        "st.title(\"🤖 Coding Academy AI Assistant\")\n",
        "st.markdown(\"#### Your smart helper for all things coding academy!\")\n",
        "\n",
        "# Initialize chat history in session state\n",
        "if 'chat_history' not in st.session_state:\n",
        "    st.session_state.chat_history = []\n",
        "\n",
        "# --- Display Chat Messages ---\n",
        "for role, text in st.session_state.chat_history:\n",
        "    if role == \"user\":\n",
        "        st.markdown(f\"<div class='chat-message user-message'>**You:** {text}</div>\", unsafe_allow_html=True)\n",
        "    else:\n",
        "        st.markdown(f\"<div class='chat-message ai-message'>**AI:** {text}</div>\", unsafe_allow_html=True)\n",
        "\n",
        "# --- User Input and AI Response ---\n",
        "user_query = st.chat_input(\"Ask me anything about the coding academy...\")\n",
        "\n",
        "if user_query:\n",
        "    st.session_state.chat_history.append((\"user\", user_query))\n",
        "    st.markdown(f\"<div class='chat-message user-message'>**You:** {user_query}</div>\", unsafe_allow_html=True)\n",
        "\n",
        "    # Generate AI response\n",
        "    try:\n",
        "        response = model.generate_content(user_query)\n",
        "        ai_response_text = response.text\n",
        "\n",
        "        # Check if AI suggests contacting human\n",
        "        if f\"contact our support team directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER}\" in ai_response_text:\n",
        "            st.session_state.chat_history.append((\"ai\", ai_response_text))\n",
        "            st.markdown(f\"<div class='chat-message ai-message'>**AI:** {ai_response_text}</div>\", unsafe_allow_html=True)\n",
        "            st.markdown(f\"<div class='whatsapp-link'><a href='https://wa.me/{WHATSAPP_CONTACT_NUMBER.replace('+', '')}' target='_blank'>➡️ **Click here to chat with us on WhatsApp!** ⬅️</a></div>\", unsafe_allow_html=True)\n",
        "        else:\n",
        "            st.session_state.chat_history.append((\"ai\", ai_response_text))\n",
        "            st.markdown(f\"<div class='chat-message ai-message'>**AI:** {ai_response_text}</div>\", unsafe_allow_html=True)\n",
        "\n",
        "    except Exception as e:\n",
        "        error_message = f\"AI assistant is currently unavailable. Please try again later or contact support directly via WhatsApp at {WHATSAPP_CONTACT_NUMBER}.\"\n",
        "        st.session_state.chat_history.append((\"ai\", error_message))\n",
        "        st.markdown(f\"<div class='chat-message ai-message' style='color: red;'>**AI:** {error_message}</div>\", unsafe_allow_html=True)\n",
        "        st.markdown(f\"<div class='whatsapp-link'><a href='https://wa.me/{WHATSAPP_CONTACT_NUMBER.replace('+', '')}' target='_blank'>➡️ **Click here to chat with us on WhatsApp!** ⬅️</a></div>\", unsafe_allow_html=True)\n",
        "\n",
        "\n",
        "# Instructions for deployment\n",
        "st.markdown(\"\"\"\n",
        "---\n",
        "### How to Run and Deploy This App:\n",
        "1.  **Replace Placeholders:** Update `WHATSAPP_CONTACT_NUMBER` with your actual WhatsApp number.\n",
        "2.  **API Key:** Ensure `GOOGLE_API_KEY` is securely stored in Colab Secrets.\n",
        "3.  **Run this cell** in your Colab notebook.\n",
        "4.  Streamlit will provide a **public URL**. Click on it to open your interactive chatbot in a new browser tab.\n",
        "5.  For **web deployment**, you would typically host this `streamlit run your_app.py` on platforms like Streamlit Community Cloud, Heroku, Render, or your own server.\n",
        "\n",
        "**Note:** The system instruction for the Gemini model is crucial for handling referrals. Make sure the model's response for human contact matches the phrase used in the code for detection.\n",
        "\"\"\")"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-06-24 16:10:09.112 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.113 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.298 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-06-24 16:10:09.299 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.302 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.304 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.305 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.307 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.309 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.312 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.312 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.313 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.314 Session state does not function when running a script without `streamlit run`\n",
            "2026-06-24 16:10:09.315 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.315 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.317 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.317 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.318 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.319 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.320 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.321 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.321 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.323 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.324 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-06-24 16:10:09.325 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    }
  ]
}
