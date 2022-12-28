import string
if __name__ == '__main__':
    s = 'Hello World.'
    s = s.translate(str.maketrans('', '', string.punctuation))
    print(s)