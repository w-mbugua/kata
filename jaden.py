# returns a sentence with all words capitalized

def to_jaden_case(string):
    new_string = string.split(' ')
    fin = [word.capitalize() for word in new_string]
    return ' '.join(fin)
