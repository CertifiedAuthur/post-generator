from llm_helper import llm
from few_shots import FewShotPosts


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    

def get_prompt(length, language, tag, few_shot):
    length_str = get_length_str(length)
    prompt = f"""
    Generate a LinkedIn post using the below information. No preamble.
    
    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    """
    
    examples = few_shot.get_filtered_posts(length, language, tag)
    
    if len(examples) >= 0:
        prompt += "4) Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example {i+1} \n\n {post_text}"
            
            if i == 1:
                break
    return prompt
            
def generate_post(length, language, tag, processed_file_content):
    few_shot = FewShotPosts(processed_file_content)
    prompt = get_prompt(length, language, tag, few_shot)
    response = llm.invoke(prompt)
    return response.content