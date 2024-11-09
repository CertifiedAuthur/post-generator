import json
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_post(raw_file_content, processed_file_content):
    enriched_posts = []
    posts = json.loads(raw_file_content)
    for post in posts:
        metadata = extract_metadata(post['text'])
        post_with_metadata = post | metadata
        enriched_posts.append(post_with_metadata)
        
    unified_tags = get_unified_tags(enriched_posts)
    
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post['tags'] = list(new_tags)
        
    return json.dumps(enriched_posts, indent=4)
    
def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
        
    unique_tags_list = ', '.join(unique_tags)
    
    template = """
    I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list.
        Example 1: "Jobseekers", "Job Hunting" can all be merged unti a single tag "Job Search".
        Example 2: "Motivation", "Inspiration", "Drive", can be mapped to "Motivation"
        Example 3: "Personal Growth", "Personal Development", "Self Improvement", can be mapped to "Self Improvement"
        Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    4. Output should have mapping of original tag and the unified tag.
        For example: {{"Jobseekers": "Job Search", "Job Hunting": "Job Search", "Motivation": "Motivation}}
        
    Here is the list of tags:
    {tags}
    """
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'tags':str(unique_tags_list)})
    
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res
            
def extract_metadata(post):
    template = """
    You are given a LinkedIn post. You need to extract number of lines, language of the post, and tags. 
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language and tags.
    3. tag is an array of text tags. Extract maximum two tags.
    4. Language should be english
    
    Here is the actual post on which you need to perform this task:
    {post}
    """
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post':post})
    
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res