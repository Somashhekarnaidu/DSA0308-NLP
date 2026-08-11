vowels = "aeiou"

def is_vowel(word, i):
    return word[i] in vowels

def measure(stem):
    m = 0
    prev_vowel = False

    for i in range(len(stem)):
        if is_vowel(stem, i):
            prev_vowel = True
        else:
            if prev_vowel:
                m += 1
            prev_vowel = False

    return m

def step2(word):
    if word.endswith("ization"):
        stem = word[:-7]
        if measure(stem) > 0:
            return stem + "ize"
    return word

word = input("Enter a word: ").lower()

print("Original Word :", word)
print("After Step 2  :", step2(word))