Shit_words = ['tangina', 'bobo', 'hayop','gago', 'ulol', 'putangina', 'pakyu', 'fuck',  ]

sentence = input('Enter your sentence: ')

new = [x for x in sentence.lower().split()]

text = ''
for word in new:
    if word in Shit_words:
        a = len(word)

        text += '*' * a + ' '

    else:
        text += word + ' '

print(text)
