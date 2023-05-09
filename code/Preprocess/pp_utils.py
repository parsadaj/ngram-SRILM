import json
from pp_cleaning import *

def get_text(message):
    text_sections = message['text']
    if type(text_sections) == str:
        text_sections = [text_sections]
    
    if type(text_sections) == dict:
        raise "message[text] is a dictionary."

    text = ''
    for section in text_sections:
        text = text + process_section(section)
    return text

def process_section(section):
    if type(section) == str:
        return clean_text(section)
    
    if type(section) == dict:
        return clean_text(section['text'])

    raise "unexpected section in message."

def manual_correction(text):
    return text

def append_to_file(text, file_path):
    with open(file_path, 'a+') as f:
        f.write(text)

def open_json(path):
    with open(path) as json_file:
        return json.load(json_file)