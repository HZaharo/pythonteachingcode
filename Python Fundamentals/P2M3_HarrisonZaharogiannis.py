# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
# [] Harrison Zaharogiannis
# [] This was incredibly tricky for me to solve.

def word_mixer(word_list):
    word_list.sort()
    
    mixed_list = []
    
    while len(word_list) > 5:
        mixed_list.append(word_list.pop(-5))
        mixed_list.append(word_list.pop(0))
        mixed_list.append(word_list.pop(-1))
    
    return mixed_list

print("Welcome, please enter your full name.")
name = input("Your name: ")

poem = input("Hello " + name + ", enter a saying or poem: ")

words = poem.split()

for i in range(len(words)):
    if len(words[i]) <= 3:
        words[i] = words[i].lower()
    elif len(words[i]) >= 7:
        words[i] = words[i].upper()

mixed_poem = word_mixer(words)

print("\nMixed Poem Output:\n")

for i in range(0, len(mixed_poem), 3):
    print(" ".join(mixed_poem[i:i+3]))