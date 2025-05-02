import streamlit as st
from Predict_Sentiment import predict_sentiment  # Import your function

# Streamlit App UI
st.title("Sentiment Analysis App")

# Input box
user_input = st.text_area("Enter your review:")

# When button is clicked
if st.button("Predict Sentiment"):
    if user_input:
        result = predict_sentiment(user_input)

        if result.lower() == 'positive':
            st.success(f"✅ Positive Sentiment Detected!")
        elif result.lower() == 'negative':
            st.error(f"❌ Negative Sentiment Detected!")
        else:
            st.info(f"ℹ️ Sentiment: {result}")
    else:
        st.warning("Please enter some text to analyze.")
