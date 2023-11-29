import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# Add a title and a brief introduction
st.title("My Portfolio")
st.write("Welcome to my portfolio! Here are some of my projects that highlight different types of charts and visualizations:")

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
        "Medical Data Visualizer": {
            "url": "https://medical-data-visualizer.streamlit.app/",
            "description": "I used data gathered from medical examinations to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.",
        },
        "Page View Time Series Visualizer": {
            "url": "https://page-series-visualizer.streamlit.app/",
            "description": "Using page-views data gathered from 2016-2019, I created several charts to identify patterns in visits and growth"
        }
        # Add more Data Visualization projects here
    },
    "Machine Learning": {
        "Local Gems": {
            "url": "https://localgems.streamlit.app",
            "description": "Local Gems is a web application that provides recommendations for places based on user queries."
        }
        # Add more Machine Learning projects here
    },
    "Page Actively Updated (11/29/2023)": {
        "Come back to see more projects": {
            "url": "https://www.linkedin.com/in/stably-jesse/",
            "description": "To see more of my projects, know more about me, or simply want to connect, hit the link to view my LinkedIn"
        }
    }
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

