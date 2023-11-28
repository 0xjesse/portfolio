import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# Add a title and a brief introduction
st.title("My Portfolio")
st.write("Welcome to my portfolio! Here are some of my projects:")

# Categorized project details
projects = {
    "Data Visualization": {
        "Google Fiber Data Analysis": {
            "url": "https://public.tableau.com/app/profile/jesse.guerrero/viz/GoogleFiberAnalysis_17005187635470/GoogleFiberAnalysis?publish=yes",
            "description": "Performed Data Analysis across a Google Fiber dataset and created dashboards on Tableau to visualize the findings."
        },
        "Sea Level Predictor": {
            "url": "https://sea-level-predictor.streamlit.app/",
            "description": "For a project from Free Code Camp, I used data from the US Environmental Protection Agency from 1880-2014 to create an interactive chart..."
        },
        # Add more Data Visualization projects here
    },
    "Machine Learning": {
        "Local Gems": {
            "url": "https://localgems.streamlit.app",
            "description": "Local Gems is a web application that provides recommendations for places based on user queries..."
        }
        # Add more Machine Learning projects here
    },
    # Add more categories if needed
}

# Loop through each category and its projects
for category_name, category_projects in projects.items():
    st.header(category_name)  # Add a header for each category

    # Loop through each project in the category
    for project_name, project_info in category_projects.items():
        with st.expander(project_name):
            st.write(project_info["description"])
            st.markdown(f"[Visit the project here]({project_info['url']})")
