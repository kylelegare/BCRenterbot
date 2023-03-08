from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import streamlit as st
import openai

#set openai API
openai_api_key = st.secrets['OPENAI_API_KEY']
openai.api_key = openai_api_key

#Page Config For Streamlit
st.set_page_config(page_title='Ask the BC Tenancy Act')

# Load the CSS styles from file
with open("style.css") as f:
    styles = f.read()

# Display the CSS styles
st.markdown(f"<style>{styles}</style>", unsafe_allow_html=True)

# Set the page title and headline

st.markdown('<h1 class="Ask The BC Residential Tenancy Act</h1>', unsafe_allow_html=True)

def ask_benefits():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    query = st.text_input("The BC Residential Tenancy Act has been converted into a document that can be read by OpenAI allowing you to ask any questions related to renting", value='')
    if st.button("Ask Away"):
        response = index.query(query)
        response_lines = response.response.splitlines()
        st.write("\n\nThe Benefit Booklet Says:\n")
        for line in response_lines:
            st.write("\n" + line)
        st.write("\n\n")
        

# Call the function
ask_benefits()

# Define the footer text
footer_text = 'Built by '
footer_text += '<a href="mailto:kyle@example.com">Kyle Legare</a>'
footer_text += ' with a little help from OpenAI'

# Create a footer div with the HTML content and center it
st.markdown(
    f"""
    <div style='text-align: center;'>
        {footer_text}
    </div>
    """,
    unsafe_allow_html=True
)