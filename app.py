import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEndpoint

# Streamlit page setup
st.set_page_config(page_title="Website Text Summarizer", page_icon="📰")
st.title("📰 Summarize Website Content")
st.subheader("Paste a valid website URL to summarize its content")

# Sidebar for Hugging Face API input
with st.sidebar:
    hf_api_key = st.text_input("Hugging Face API Token", value="", type="password")

# URL input
website_url = st.text_input("Enter Website URL", label_visibility="visible")

# Define LLM
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.7,
    huggingfacehub_api_token=hf_api_key
)

# Prompt template
prompt_template = """
Provide a concise summary (within 300 words) of the following website content:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Button to trigger summarization
if st.button("Summarize Website Content"):
    if not hf_api_key.strip() or not website_url.strip():
        st.error("Please provide both the Hugging Face token and a valid website URL.")
    elif not validators.url(website_url):
        st.error("The input is not a valid URL.")
    else:
        try:
            with st.spinner("Loading and summarizing content..."):
                # Load website content
                loader = UnstructuredURLLoader(
                    urls=[website_url],
                    ssl_verify=False,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/114.0.0.0 Safari/537.36"
                    }
                )
                docs = loader.load()

                # Summarize using LangChain
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                summary = chain.run(docs)

                st.success("Summary generated successfully!")
                st.write(summary)

        except Exception as e:
            st.error("An error occurred while summarizing the website.")
            st.exception(e)
