import string 
def word_count(s):
    s = s.lower()
    unwanted_chars = '":;.,-+=/\|[]{}()*^&'
    s = s.translate(str.maketrans({a:None for a in unwanted_chars})) 
    # Python Program to Count words in a String using Dictionary
    counts = dict()
    newWords = s.split()
    for s in newWords:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))