"""
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
"""

def ask():

    while True:
        try:
            n = int(input("Input an integer: "))
        except:
            print("An error occurred")
            continue
        else:
            break

    print("Thank you, your number squared is: ", n**2)

# Run
ask()