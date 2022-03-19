from spellchecker import SpellChecker

spell = SpellChecker()

user_input=input('Enter the text: ')

user_input=user_input.split()

# find those words that may be misspelled

misspelled = spell.unknown(user_input)

#print(misspelled)

for word in misspelled:

    print('%s is wrong'%word)

    print('Probably you meant:  ',spell.correction(word)) #Get the one most likely answer

    candidate_words=(spell.candidates(word))

    lencheck=spell.candidates(word)

    print(spell.candidates(word)) # Get a list of likely options

    if len(lencheck)>1:

        q=input(' Did you mean any of the above words? If yes,enter the desired word from the above set: ')

        if q in candidate_words:

            user_input.insert(user_input.index(word),q)

            user_input.remove(word)

joint_words=' '.join(user_input)

print(joint_words)


   

