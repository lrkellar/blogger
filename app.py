import streamlit as st
import os
st.set_page_config(layout="wide")
# Folder containing Markdown files
MARKDOWN_FOLDER = "library"

# Ensure the folder exists
if not os.path.exists(MARKDOWN_FOLDER):
    os.makedirs(MARKDOWN_FOLDER)

# Get a list of markdown files in the folder
markdown_files = [f for f in os.listdir(MARKDOWN_FOLDER) if f.endswith(".md")]

# Streamlit UI
st.title("Markdown Report Viewer")

# Dropdown to select a file
if markdown_files:
    selected_file = st.selectbox("Select a Markdown file:", markdown_files)

    # Load and display the selected Markdown file
    file_path = os.path.join(MARKDOWN_FOLDER, selected_file)
    with open(file_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Display Markdown
    st.markdown(markdown_content, unsafe_allow_html=True)

    # Option to download the file
    st.download_button(
        label="Download this report",
        data=markdown_content,
        file_name=selected_file,
        mime="text/markdown"
    )
else:
    st.warning("No markdown files found in the folder.")
