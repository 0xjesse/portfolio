import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# Add a title and a brief introduction
st.title("My Portfolio")
st.write("Welcome to my portfolio! Here are some of my projects:")

# Project details
projects = {
    "Local Gems": {
        "url": "https://localgems.streamlit.app",
        "description": "Local Gems is a web application that provides recommendations for places based on user queries. Utilizing natural language processing and location-based search, the app allows users to find top-rated spots like restaurants, clubs, or bakeries (and more) in any specified area. Built with Python, the app integrates large language models for query understanding and leverages the Google Places API for accurate, real-time data. Deployed on Streamlit Cloud, Local Gems offers an intuitive interface with features like dynamic sorting and filtering, enhancing user experience in discovering local gems."
        # Add more details if needed
    },
    "Google Fiber Data Analysis": {
        "url": "https://public.tableau.com/app/profile/jesse.guerrero/viz/GoogleFiberAnalysis_17005187635470/GoogleFiberAnalysis?publish=yes",
        "description": "Performed Data Analysis across a Google Fiber dataset and created dashboards on Tableau to visualize the findings."
        # Add more details if needed
    },
    "More Projects Coming Soon": {
        "url": "https://www.linkedin.com/in/stably-jesse/",
        "description": "More projects are in development and will be coming soon! Some projects I am working on projects including chatbots, sentiment analysis tools, and more. Hit the link and navigate to the projects section in my Linkedin to see other projects. (Last updated 11/20)"
        # Add more details if needed
    },
    # Add more projects here
}

# Generate expanders for each project
for project_name, project_info in projects.items():
    with st.expander(project_name):
        st.write(project_info["description"])
        st.markdown(f"[Visit the project here]({project_info['url']})")

