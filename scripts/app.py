import streamlit as st
import spacy_streamlit
from visualize_model import main as visualize_main

def run_app():
    st.title("SpaCy Model Visualizer")

    # Get user inputs
    models = st.text_input("Enter the model names (comma-separated):", "en_core_web_sm")
    default_text = st.text_area("Enter the default text:", "This is a sample text for visualization.")

    if st.button("Visualize"):
        if models and default_text:
            # Call the visualize function directly
            visualize_main(models, default_text)
        else:
            st.error("Please provide both models and default text.")

if __name__ == "__main__":
    run_app()
