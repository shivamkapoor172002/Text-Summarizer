import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def main():
    st.title("Text Summarizer")

    # Load the summarization model and tokenizer
    model_name = "pszemraj/led-base-book-summary"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Input text
    text = st.text_area("Enter the text to summarize", height=300)

    if st.button("Summarize"):
        if text.strip() != "":
            # Preprocess the input text
            inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

            # Generate the summary
            summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=150, early_stopping=True)
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Display the summary
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()
