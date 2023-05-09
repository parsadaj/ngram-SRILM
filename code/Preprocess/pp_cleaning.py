#import socket
#import validators
import re

URL = r" <URL> "
NUM = r" <NUM> "
USER = r" <USERNAME> "

SEP = ' '
NEWLINE = '\n'

def clean_text(text):
    text = re.sub("\.[\.]+|[()\[\]{}<>\"\']", '', text)

    text = re.sub("ك", 'ک', text)
    text = re.sub('ي', 'ی', text)
    text = re.sub('ؤ', 'و', text)
    text = re.sub('[أآ]', 'ا', text)
    text = re.sub('ة', 'ه', text)

    url_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    text = re.sub(url_pattern, URL, text)

    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(:(\d)+)?'
    text = re.sub(ip_pattern, URL, text)

    email_pattern = '\S+@\S+'
    text = re.sub(email_pattern, URL, text)

    username_pattern = '(?<=\s)@\S+'
    text = re.sub(username_pattern, USER, text)

    username_pattern = '(?<=^)@\S+'
    text = re.sub(username_pattern, USER, text)

    legal_farsi = 'ا-ی'
    legal_arabic = 'ئ'
    legal_english = 'a-zA-z'
    legal_number = '0-9۰-۹'
    legal_other = '\s<>\n'

    illegal_pattern = "[^{}]".format(legal_arabic + legal_english + legal_farsi + legal_number + legal_other)

    text = re.sub(illegal_pattern, ' ', text)

    text = re.sub("(?<=[a-zئA-Zا-ی])(?=\d)", ' ', text)
    text = re.sub("(?<=\d)(?=[a-zئA-Zا-ی])", ' ', text)

    num_pattern = r"\b\d+\b"
    text = re.sub(num_pattern, NUM, text)
    

    sentences = re.split("[.!?.؟!]", text)
    sentences = [s.split() for s in sentences]


    # for sentence in sentences:
    #     for i, word in enumerate(sentence):
    #         if is_ip(word):
    #             sentence[i] = IP
    #         if is_email(word):
    #             sentence[i] = MAIL
    #         if is_url(word):
    #             sentence[i] = URL

    result_text = ''
    for sentence in sentences:
        if len(sentence) > 1:
            result_text = result_text + SEP.join(sentence) + NEWLINE
    
    return result_text

    

# def is_ip(word):
#     return validators.ip_address.ipv4(word) or validators.ip_address.ipv6(word) or validators.mac_address(word)

# def is_url(word):
#     return validators.domain(word) or validators.url(word)

# def is_email(word):
#     return validators.email(word)