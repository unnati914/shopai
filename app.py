import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    st.error("API key not found. Please set the GEMINI_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)
    
    st.title("Shop AI")
    st.subheader("Get recommendations for shopping online just with a click!")

    recipient_type = st.selectbox(
        "What is the occasion?",
        ["Wedding", "Party", "Birthday", "Office Gathering", "Family Function"]
    )

    absurdity_level = st.radio(
        "Choose the dress type:",
        ["Light", "Heavy"]
    )
    
    customer_name = st.radio(
        "Who are you?",
        ["Man", "Woman", "Kid"]
    )
    
    age_group = st.radio(
        "Select your age group:",
        ["Child", "Teen", "Adult", "Senior"]
    )
    
    if st.button("Generate Dress Recommendation"):
        prompt = f"""
        You are a fashion stylist creating personalized dress recommendations for users based on their input. Use the following details to craft tailored suggestions:
        
        - Occasion: {recipient_type}
        - Dress Type: {absurdity_level}
        - Gender: {customer_name}
        - Age Group: {age_group}

        Guidelines:
        1. For a Wedding: Recommend formal or traditional attire that suits the grandeur of the event. Ensure suggestions match the user’s gender and age group, with family-friendly outfit options if applicable.
        2. For a Party: Suggest trendy and stylish outfits that match the celebratory mood. Focus on playful, fun options for kids and modern, elegant styles for adults.
        3. For a Birthday: Provide cheerful, standout outfit ideas. For kids, include colorful, comfortable designs; for adults, offer options that are festive and unique.
        4. For an Office Gathering: Suggest professional yet stylish attire for adults and semi-formal, neat options for kids if included.
        5. For a Family Function: Recommend modest, comfortable, and elegant clothing for all age groups, with attention to practicality for kids and sophistication for adults.

        Include specific color, pattern, and accessory suggestions. Prioritize comfort for kids and seniors, while offering trendy options for teens and adults. Be culturally and seasonally relevant in your recommendations.
        """
        
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            recommendations = response.text.strip()
            
            st.success("Here are your dress recommendations:")
            st.write(recommendations)
        except Exception as e:
            st.error("An error occurred while generating the recommendation.")
            st.write(e)
