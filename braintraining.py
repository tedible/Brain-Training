import random
import time ## for timing question rounds

def math_question():

    operators = ["+","-","*","/"] #need to put back in divide option, but fix so integer answer only
    # good idea to expand if loop to set appropriate limits for different operations

    operation = random.choice(operators)

    if operation == "+":
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        correct = num1 + num2
    elif operation == "-":
        num1 = random.randint(1,90)
        num2 = random.randint(1,85)
        while num1 - num2 < 0:
            num2 = random.randint(1,85)
        correct = num1 - num2
    elif operation == "*":
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        while num1 * num2 > 160:
            num2 = random.randint(1,12)
        correct = num1 * num2
    else: #divide
        num1 = random.randint(1,160)#expand this to extend possible questions
        num2 = random.randint(1,12)
        while num1 % num2 != 0:
            num2 = random.randint(1,12)
        correct = num1 / num2
    
    answer = input("Q: {} {} {} = ".format(num1, operation, num2))

    if int(answer) == correct:
        print("Correct!")
        return True
    else:
        print("Incorrect! The answer was " + str(correct))
        return False


num_qs = int(input("How many questions do you want?\n"))
num_correct = 0

for i in range(num_qs):
    q = math_question()
    if q == True:
        num_correct += 1

print(num_correct)

## NOW WORK OUT HOW TO TIME A ROUND OF QUESTIONS