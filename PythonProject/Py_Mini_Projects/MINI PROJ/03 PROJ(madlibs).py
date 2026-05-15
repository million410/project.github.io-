with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        if word not in words:
             words.append(word)

answers = {}

for word in words:
    answer = input('Enter a word for ' + word.lstrip('<').rstrip('>') + ': ')
    answers[word] = answer
    story = story.replace(word, answer)

print(story)



