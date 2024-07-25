import random


# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    return random.choice(word_list) + str(random.randint(0, 20)) + random.choice(word_list) + str(random.randint(0, 20)) + random.choice(word_list)


print(generate_password())