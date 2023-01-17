'''
1) a dictionary that stores questions and answers
2) have a variable that tracks the score of the player
3) loop through the dictionary using the key value pairs
4) display each question to the user and allow them to answer
5) tell them if they are right or wrong
6) show the final result when quiz is completed
'''

quiz = {
    "question 1": {
        "question": "What is the capital of France?",
        "answer": 'Paris'
    },
    "question 2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question 3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question 4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question 5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question 6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question 7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print(f'Your score is: {str(score)}')
        print("")
        print("")

    else:
        print("Wrong!")
        print(f'The answer is : {value["answer"]}')
        print(f'Your Score is: {str(score)}')
        print("")
        print("")

print(f'You got {str(score)} out of 7 questions correctly')
print(f'Your percentage is {str(int(score/7*100))}%')
