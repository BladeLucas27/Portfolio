import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)
def css():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        [data-testid="stHeader"] {visibility: hidden;}

        .stApp {
            background-color: #2d2b47;
            background-size: cover;
        }

        h1, h2, h3, p, .stMarkdown, li {
            color: #ffddab !important;
        }

        [data-testid="stTable"] {
            background-color: transparent;
        }
        
        [data-testid="stTable"] th {
            background-color: #3a3858 !important;
            color: #ffddab !important;
            border-bottom: 2px solid #ffddab !important;
        }
        
        [data-testid="stTable"] td {
            background-color: transparent !important;
            color: #ffddab !important;
            border-bottom: 1px solid rgba(255, 221, 171, 0.2) !important;
        }
                
        [data-testid="stTable"] th {
            background-color: #3a3858 !important;
            color: #ffddab !important;
            text-align: center !important;
            font-weight: bold !important;
            border-bottom: 2px solid #ffddab !important;
        }

        /* 3. Style Links */
        [data-testid="stTable"] a, .stMarkdown a {
            color: #78cee1 !important;
            text-decoration: none;
            font-weight: bold;
        }

        [data-testid="stTable"] a:hover, .stMarkdown a:hover {
            color: #ffffff !important;
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)
#css()

col1, col2 = st.columns([1, 4], gap="large")

project_data = {
    "Project Name": [
        "🔢 Basic Number Sorter Visualizer",
        "🏫 UBelongWithMe",
        "🔍 DBSCAN Clustering and Apriori Data Analysis",
        "🖼️ Basic Image Processor",
        "🧘 CalmCode - Meditation App"
    ],
    "Short Description": [
        "Application demonstrating different methods of array number sorting.",
        "Centralized school club and organization event planning and social media platform.",
        "Analysis and visualization of a ‘customer purchasing patterns’ dataset using multiple data analysis techniques.",
        "Takes images and applies basic image processing techniques such as grayscale conversion, reverse, and greenscreen subtraction.",
        "Start of a meditation application that helps users relax and focus through chosen musical genres and related articles."
    ],
    "Role": [
        "Sole Developer",
        "Backend, Frontend, and Database Developer (Team of 5)",
        "Frontend Developer (Team of 4)",
        "Sole Developer",
        "Backend and Frontend Developer (Team of 2)"
    ],
    "Links": [
        "https://github.com/BladeLucas27/Number-Sorter-Visualizer.git",
        "https://github.com/BladeLucas27/UBelongWithMe.git",
        "https://github.com/BladeLucas27/StreamlitDataAnalysis.git",
        "https://github.com/BladeLucas27/ImageProcessingAct.git",
        "https://github.com/BladeLucas27/CalmCode.git"
    ]
}

with col1:
    st.image("pfp.png", width=300)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("""
    - Name: Raymond Gerard Tio
    - Age: 21
    - Location: Cebu, Philippines
    - Course: Bachelor of Science in Computer Science
    - Hobbies and Interests: Video Games, Discovering Cafés, Anime, Flowers, and Collecting Plushies
    """)

with col2:
    st.title("Hello! This is a brief portfolio all about me!")
    st.markdown("---")

    st.subheader("About Me")
    st.write("""
    Hi! I'm currently a third-year Computer Science student studying at Cebu Institute of Technology - University. 
    As someone who loves problem-solving, I have always been drawn to the world of programming and game development.      
               
    I still think I have a long way to go in terms of learning and improving my skills, but I'm excited about the journey ahead.
    Someday I hope to fulfill my dream of becoming a game developer and creating games that people will love to play, and hopefully enjoy them as much as I did playing games when I was a kid.
    """)

    st.subheader("Sample Projects")
    st.table(project_data, border="horizontal")

    st.subheader("Contact Me")
    st.write("""
    - 🧑‍💻 **GitHub:** [BladeLucas27](https://github.com/BladeLucas27)  
    - ✉️ **Gmail:** [raymondgtio@gmail.com](mailto:raymondgtio@gmail.com)  
    - 💬 **Facebook:** [Raymond Gerard Tio](https://www.facebook.com/raymondgerard.tio)
    - 💼 **Linkedin:** [Raymond Gerard Tio](https://www.linkedin.com/in/raymond-gerard-tio-3933a13ba/)
    """)
st.markdown("---")