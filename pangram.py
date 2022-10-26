from string import ascii_lowercase


def pangram(word):
    if all(letter in word.lower() for letter in ascii_lowercase):
        return True
    return False


print(pangram('The quick brown fox jumps over the lazy dog'))
