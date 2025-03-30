import time
import random
import requests
import json
from replacements import replacements_list
import re

print("""
                   ███     ██████    █████  █████ █████ ███████████
                  ░░░    ███░░░░███ ░░███  ░░███ ░░███ ░█░░░░░░███ 
  █████   ██████  ████  ███    ░░███ ░███   ░███  ░███ ░     ███░  
 ███░░   ███░░███░░███ ░███     ░███ ░███   ░███  ░███      ███    
░░█████ ░███ ░░░  ░███ ░███   ██░███ ░███   ░███  ░███     ███     
 ░░░░███░███  ███ ░███ ░░███ ░░████  ░███   ░███  ░███   ████     █
 ██████ ░░██████  █████ ░░░██████░██ ░░████████   █████ ███████████
░░░░░░   ░░░░░░  ░░░░░    ░░░░░░ ░░   ░░░░░░░░   ░░░░░ ░░░░░░░░░░░ 
""")

print("""
Welcome to sciQUIZ! This is a general science quiz game to test your knowledge.  

How to Play?  

- Answer the question displayed on the terminal.  
- Your score will be shown after each question.  
- Scoring system:  
    Correct Answer  : +1 point  
    Wrong Answer    : -0.5 points
- Also if you don't know answer to any question. You can skip it.
  (Enter "skip" to skip questions.)

Ranking System:  

Your final score determines your ranking:  
  Below 50%   : You need improvement.  
  50% - 74%   : You are good.
  75% & above : You are excellent.

you can stop this enter "stop" word among test.
      
Play, test your knowledge, and have fun!  
--------------------------------------------------
""")

def exitWant(word):
    if word == "stop":
        print("Okay, you left!")
        exit(1)

def requestor(amount, difficulty):
    try:
        response = requests.get(f"https://opentdb.com/api.php?amount={amount}&category=17&difficulty={difficulty}", stream=True)
        return response
    except Exception as e:
        print("\nWe have some network problem. Try again later.")
        print("Goodbye and have a nice day!")
        exit(4)
    
def wordReplacementCheacker(text):
    pattern = r"&[a-zA-Z0-9#]+;"
    match = re.search(pattern, text)
    return bool(match)

def wordReplacer(word, replacement=replacements_list):
    for i in replacement:
        word = word.replace(f"{i[0]}", f"{i[1]}")

    return word


game_status = True
while game_status:
    start_stage = True
    while start_stage:
        try:
            q_count = input(f"\nHow many questions would you like to start this game with? (Minimum is 10): ")
            if q_count.isdigit():

                questionsCount = int(q_count)
                if questionsCount < 10:
                    print("Minimum questions count is 10! Try again.")
                    continue

                print(f"\nWhat difficulty level questions do you want?")
                print("""
0. Any
1. Easy
2. Medium
3. Hard
                """)
                d_level = input(": ").lower()
                print("")

                d_levelList = ["0", "easy", "medium", "hard", "any"]

                if d_level.isdigit() and (int(d_level) >= 0 and int(d_level) <= 3):
                    data = requestor(questionsCount, d_levelList[int(d_level)])
                elif d_level in d_levelList:
                    if d_level == "any":
                        data = requestor(questionsCount, 0)
                    else:
                        data = requestor(questionsCount, d_level)
                else:
                    print("Invalid input! Try again.")
                    continue

                questionsDic = data.json()
                maxQuestions = len(questionsDic["results"])
        
                # with open("questions.json", "w") as qfile:  # This is not necessary. I'm just using it to get a visual representation of the question.
                #     json.dump(questionsDic, qfile, indent=4)

            else:
                exitWant(q_count)
                print("Invalid input! Try again.")
                continue
        except Exception as e:
            print("Invalid input! Try again.")
            continue

        print("Perfect. Let's go...")

        time.sleep(1.5)
        start_stage = False
        print("")


    program_state = True
    score, count = 0, 1
    while program_state:

        maxQuestions = len(questionsDic["results"])
        if count > maxQuestions:
            break

        question_dict = questionsDic["results"][count-1]

        replacements = replacements_list

        question = question_dict["question"]
        correct_answer = question_dict["correct_answer"]
        incorrect_answers = question_dict["incorrect_answers"]

        if wordReplacementCheacker(question):
            question = wordReplacer(question)
        if wordReplacementCheacker(correct_answer):
            correct_answer = wordReplacer(correct_answer)

        for inc_Ans in incorrect_answers:
            if wordReplacementCheacker(inc_Ans):
                replaceWord = wordReplacer(inc_Ans)
                incorrect_answers[incorrect_answers.index(inc_Ans)] = replaceWord

        answers = [correct_answer]
        for i in incorrect_answers:
            answers.append(i)

        random.shuffle(answers)

        print(f"\nQ{count}. {question}")
        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")
        
        try:
            userAnswer = input(": ").lower()

            if userAnswer.isspace() or userAnswer == "":
                print("Empty input! Try again.")
                continue
            elif userAnswer == "skip":
                count += 1
                print("It's skipped!")
                continue
            elif userAnswer == "stop":
                exitWant(userAnswer)
            else:
                pass
        except Exception as e:
            print("Invalid input! Try again.")
            continue

        if userAnswer == str(correct_answer).lower():
            score += 1
            if score <= 0:
                score = 0
            print("You're correct!")
            print(f"Your score is : {score}")
        else:
            score -= 0.5
            if score <= 0:
                score = 0
            print("You're wrong!")
            print(f"Correct answer is : {correct_answer}")
            print(f"Your score is : {score}")

        count += 1

    print("\nPerfect. You're done!\n")
    time.sleep(1.5)

    scorePerc = (score/(len(questionsDic))*100)

    print(f"[+] Your score is : {score}")
    print(f"[+] Your score as percentage : {scorePerc}%")

    if scorePerc < 50:
        print("\nYou need improvement.")
    elif scorePerc >= 50 and scorePerc < 75:
        print("\nYou are good.")
    elif scorePerc >= 75 and scorePerc <= 100:
        print("\nYou are excellent!")
    else:
        pass

    playAgain = input("\nDo you want to play again? (yes/no): ").lower()
    if playAgain == "yes" or playAgain == "y":
        print("\n")
        continue
    elif playAgain == "no" or playAgain == "n":
        print("\nOk, Goodbye and have a nice day!")
        exit(2)
    else:
        print("\nInvalid input!")
        print("You Leaning now...")
        print("Goodbye and have a nice day!")
        exit(3)
