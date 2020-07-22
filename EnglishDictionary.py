import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif len(get_close_matches(word, data.keys())) > 0:
        confirmationMessage = input(f"Did you mean {get_close_matches(word, data.keys())[0]} insteed? Enter Y if yes, N if no: ") 
        if confirmationMessage == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirmationMessage == "N":
            return "This word does not exist, please check again."
        else:
            return "We did not understand your query.   "
    else:
        return "Word you typed, does not exist, please check your word"
inputWord = input("Enter the word: ")

outputList = translate(inputWord)

if type(outputList) == list:
    for output in outputList:
        print(output)
else:
    print(outputList)