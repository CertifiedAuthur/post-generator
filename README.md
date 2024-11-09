## LinkedIn Post Generator

##### Table of Contents
###### Introduction
LinkedIn Post Generator is an AI-powered tool designed to help users generate high-quality LinkedIn posts. This project leverages natural language processing (NLP) and machine learning algorithms to create engaging and relevant content.

###### Features
1. Generate LinkedIn posts based on user-input topics, lengths, and languages
2. Preprocess raw JSON data to extract relevant information
3. Save processed data for future use
4. User-friendly interface built with Streamlit
   
###### Requirements
1. Python 3.8+
2. Streamlit
3. langchain_core
4. llm_helper
5. JSON
   
###### Installation

Clone the repository: git clone 

```
https://github.com/certifiedauthur/linkedIn-post-generator.git
```

Install dependencies: 

```
pip install -r requirements.txt
```

Run the application: 

```
streamlit run main.py
```

###### Usage
1. Select whether you have a processed JSON file or raw JSON file
2. Upload your file
3. Choose topic, length, and language
4. Click "Generate" to create your LinkedIn post
   
###### How it Works
1. User uploads raw or processed JSON file
2. Application preprocesses raw data (if necessary)
3. User selects topic, length, and language
4. AI model generates LinkedIn post based on user input
5. Post is displayed in the application

###### Contributing
Contributions are welcome! Please submit a pull request with your changes.

###### License
This project is licensed under the MIT License.

###### Acknowledgments
Special thanks to the langchain_core and llm_helper libraries for their NLP capabilities.
