import streamlit as st
import spacy
import pandas as pd
import typer
from pathlib import Path

# Load the trained textcat model
@st.cache(allow_output_mutation=True)
def load_model():
    # Construct the base path relative to the script's location
    script_dir = Path(__file__).parent
    base_path = script_dir / '..' / 'packages' / 'en_ClassificationML-0.0.0' / 'en_ClassificationML' / 'en_ClassificationML-0.0.0'
    nlp = spacy.load(base_path.resolve())
    return nlp

nlp = load_model()

def visualize_textcat(doc):
    """Visualizer for text categories."""
    st.header("Text Classification")
    st.markdown(f"> {doc.text}")
    df = pd.DataFrame(doc.cats.items(), columns=("Classification", "Score"))
    st.dataframe(df)

def main():
    st.title("Text Classification Model Visualizer")

    st.sidebar.header("Model Options")
    default_text = st.sidebar.text_area("Input Text", "Type your text here...")

    if st.sidebar.button("Analyze"):
        with st.spinner("Analyzing..."):
            doc = nlp(default_text)
            visualize_textcat(doc)
    
    st.sidebar.markdown("""<span style="font-size: 0.75em">&hearts; Built with [spaCy](https://spacy.io) & [Streamlit](https://streamlit.io)</span>""", unsafe_allow_html=True)

if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
