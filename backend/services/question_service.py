import re
def extract_callsign(question:str):
    words =question.upper().split()

    for word in words:
        clean_word= word.strip("?,.!']:;")
        if re.fullmatch(  r"[A-Z]{2,3}[0-9]{1,4}[A-Z]{0,2}",clean_word):
            return clean_word

    return None