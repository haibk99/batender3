import random #for use in assigning ingredients

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
# Question and answers
def ask():
    answers = {}
    print ("Questions")
    for key in questions.keys():
        answers[key] = input(questions[key] + "(enter yes(y) or no(n)):")
    return answers

#match randomly with the ingredients
def match(answers):
    print('\n\nWe would like to have some recommendations:\n')
    for key in answers.keys():
        if answers[key] != "":
            if answers[key].lower()[0] == 'y':
                print(random.choice(ingredients[key]))
    print('\n\n')

if __name__ == '__main__':
    answers = ask()
    match(answers)