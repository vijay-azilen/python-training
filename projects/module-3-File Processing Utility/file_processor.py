def read_text_file(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            return file.read()
        
    except FileNotFoundError:
        print("File not found.")
        return None
    
def count_lines(content):
    return len(content.splitlines())

def count_words(content):
    return len(content.split())

def count_characters(content):
    return len(content)

def search_word(content, word):
    return word.lower() in content.lower()