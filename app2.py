import streamlit as st
import requests
import json

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "0abaaafb-f2e8-4bf8-8c1e-c9e92a9763e7"
FLOW_ID = "ffc00a42-6dc1-4f3e-a68d-3a91de92b738"
APPLICATION_TOKEN = "AstraCS:kxfwcaOJFYcGzrIpYIFrYZFA:9e139cbacebde92a975123d64709b2f73a464da91fb1c71947f28066146dc781"  # Replace with your actual token

# Function to interact with LangFlow API
def run_flow(message: str, endpoint: str = FLOW_ID, output_type: str = "chat", input_type: str = "chat", tweaks: dict = None, application_token: str = APPLICATION_TOKEN) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }

    if tweaks:
        payload["tweaks"] = tweaks

    headers = {
        "Authorization": f"Bearer {application_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an HTTPError if the status is 4xx or 5xx
    return response.json()

# Function to format the response
def format_response(response: dict) -> str:
    analysis = response.get("outputs", [])[0].get("outputs", [])[0].get("results", {}).get("message", {}).get("text", "")
    return analysis

# Streamlit UI
st.title("LangFlow For Social Media Analytics (Facebook)")
st.markdown("### Send a message to the and get a response.")

# Input for the message to send to the flow
message = st.text_input("Enter your message:")

# Submit button
if st.button("Submit"):
    if message:
        try:
            response = run_flow(message)
            analysis = format_response(response)
            st.subheader("Response from LangFlow API:")
            st.markdown(analysis)  # Displays the response in a formatted way

        except requests.exceptions.RequestException as e:
            st.error(f"Request Error: {e}")
        except json.JSONDecodeError:
            st.error("Error parsing the API response. The response might not be in JSON format.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a message.")

# Add some styling for better user experience
st.markdown(
    """
    <style>
    .stAlert {
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
