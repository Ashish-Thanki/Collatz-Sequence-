"""This sequence is a spectacular exemplar of the mystery mathematics presents. The user inputs a number.
Following this if the number is even it divides it by 2. If the number is even it is placed into the function
3x +1, where x is the odd nummber. The sequence continues until...

it reaches 1 !!! Whatever the number, it always reaches 1.
No matter how big or small. Give it a go."""
23

def collatz():
    try:
        number = int(input(" Please enter your number: "))
        while number != 1:
            if number % 2 ==0:
                number = number // 2
                print(number)
            else:
                number = 3 * number + 1
                print(number)
    except ValueError:
        print("You must enter an integer not a string or decimal number.")

collatz()