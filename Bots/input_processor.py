import re

def process_input(user_input):
    cleaned_input = re.sub(r'[^\w\s]', '', user_input).lower()
    return cleaned_input