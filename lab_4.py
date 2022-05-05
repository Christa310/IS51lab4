




"""
This program allows a user three tries to guess the correct answer to the question
question = "what is the captital of California". The answer is Sacramento.

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration, 
we ask the user for the answer (user input). Then based on the answer the user gives, we check
to see if the user  input matches the answer. If so, print "Correct!", then terminate the loop with
a break statement.

if the user could not guess the correct answer within the max_tries, then print
"You have used up all your allotment of guesses", then print "Thr correct answer is Sacramento".
"""

"""
Main
    Question = "What is the capital of California"
    Answer = "Sacramento"
    ask(question, answer)

Ask
    tries = 0
    loop tree times
        increment tries
        asker user input()
        check to see if user input is equal to the answer
            if so,  print "correct" then exit loop
    if not correct
        print to the user " you have used up your allotment of guesses."
        print the correct answer "The correct answer is 'Sacramento'"

Main
"""

def main():
    question = "What is the capital of California?:"
    answer = "Sacramento"
    ask(question, answer)

def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries = tries + 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")

main()


