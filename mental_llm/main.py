import streamlit as st
from groq import Groq

def predict_depression_level(input_text):
    groq_api_key = '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'  # Groq API key
    client = Groq(api_key=groq_api_key)
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {   
                "role": "system",
                "content": "You are a mental health prediction system designed to assess and categorize the level of depression based on the given text input. You will categorize depression into four levels: minimum, mild, moderate, and severe. Additionally, you will rate the depression on a scale of 1 to 10, with 1 being the least or no depression and 10 being the highest level of depression."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    prediction = ""
    for chunk in completion:
        prediction += chunk.choices[0].delta.content or ""
    return prediction

def main():
    st.title("🧠Mental LLM")
    input_text = st.text_area("Enter your text here:")
    if st.button("Predict"):
        prediction = predict_depression_level(input_text)
        st.write("Prediction:")
        st.write(prediction)

if __name__ == "__main__":
    main()