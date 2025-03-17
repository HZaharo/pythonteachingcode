# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# Harrison Zaharogiannis

def words_after_g():
    
    user_name = input("Enter your name: ")
    print("Welcome,", user_name + ". Enter a 1 sentence quote, non-alpha separate words:")

    quote = input("Enter a 1 sentence quote, non-alpha separate words:")

    word = ""

    for char in quote:
        if char.isalpha():
            word += char
        else:
            if word:
                if word[0].lower() >= 'h':
                    print(word.upper())
                word = ""
    if word and word[0].lower() >= 'h':
        print(word.upper())


words_after_g()