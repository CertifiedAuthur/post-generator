import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post
from preprocess import process_post
import json
import datetime
import os


length_options = ["Short", "Medium", "Long"]
language_options = ["English"]


def main():
    st.title("LinkedIn Post Generator")


    # Ask user if they have a processed file or raw file
    file_type = st.selectbox("Do you have a:", ["Processed JSON file", "Raw JSON file"])


    if file_type == "Processed JSON file":
        processed_file = st.file_uploader("Upload processed JSON file")
        if processed_file:
            processed_file_content = processed_file.read().decode("utf-8")
            fs = FewShotPosts(processed_file_content)
            tags = fs.get_tags()


            col1, col2, col3 = st.columns(3)
            with col1:
                selected_tag = st.selectbox("Topic", options=tags)


            with col2:
                selected_length = st.selectbox("Length", options=length_options)


            with col3:
                selected_language = st.selectbox("Language", options=language_options)


            if st.button("Generate"):
                with st.spinner("Generating LinkedIn Post..."):
                    post = generate_post(selected_length, selected_language, selected_tag, processed_file_content)
                    st.success("LinkedIn post generation done!")
                    st.write(post)


    elif file_type == "Raw JSON file":
        raw_file = st.file_uploader("Upload raw JSON file")
        if raw_file:
            raw_file_content = raw_file.read().decode("utf-8")
            processed_posts = process_post(raw_file_content, None)


            # Generate dynamic filename for processed posts
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processed_posts_{current_time}.json"


            # Save processed posts to local file
            with open(filename, 'w') as f:
                json.dump(json.loads(processed_posts), f, indent=4)


            st.success(f"Raw posts processing done! Saved as '{filename}'")


            # Load saved processed file
            with open(filename, 'r') as f:
                processed_file_content = f.read()


            fs = FewShotPosts(processed_file_content)
            tags = fs.get_tags()


            col1, col2, col3 = st.columns(3)
            with col1:
                selected_tag = st.selectbox("Topic", options=tags)


            with col2:
                selected_length = st.selectbox("Length", options=length_options)


            with col3:
                selected_language = st.selectbox("Language", options=language_options)


            if st.button("Generate"):
                with st.spinner("Generating LinkedIn Post..."):
                    post = generate_post(selected_length, selected_language, selected_tag, processed_file_content)
                    st.success("LinkedIn post generation done!")
                    st.write(post)


if __name__ == "__main__":
    main()