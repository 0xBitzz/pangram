from string import ascii_lowercase


def pangram(sentence):
    if all(letter in sentence.lower() for letter in ascii_lowercase):
        return True
    return False


print(pangram('The quick brown fox jumps over the lazy dog'))
