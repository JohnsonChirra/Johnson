import random
import math
i = random.randint(50, 80)

if (i < 60):

    print(i,  "is less than 60")

elif(i > 60):

    print(i,  "is greater than 60")

    # TODO: Write a conditional that prints the color of the picked Animal
picked_Animal = random.choice(['Elephant', 'Lion', 'Tiger'])

if (picked_Animal == "Elephant"):

    print("Elephant")

elif (picked_Animal == "Lion"):

    print("Lion")

elif (picked_Animal == "Tiger"):

    print("Tiger")

# TODO: Write a function that multiplies two numbers and returns the result

# Define the function here.
def mul(num1, num2):

    result  = num1 * num2

    return result

 # TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", mul(12, 96))

print("48 x 17 =", mul(48, 17))

print("196523 x 87323 =", mul(196523, 87323))

         
         
  