"""
    Student Name: Naseem Badran

    This is a python code for MMN11
"""

#Qustion 1!!
def game(player_1,player_2):
    """
        Determines the winner of the Rock-Paper-Scissors game.
        :param player_1: Choice of player 1 (R, P, or S)
        :param player_2: Choice of player 2 (R, P, or S)
        :return: the function return 1 if player_1 wins,2 if player_2 wins,0 if a tie
    """
    if player_1==player_2:
        return 0
    elif (player_1=='R' and player_2=='S') or (player_1=='S' and player_2=='P') or (player_1=='P' and player_2=='R'):
        return 1
    else:
        return 2

def tournament():
    """
        Simulates a Rock-Paper-Scissors tournament between two players.
        The tournament consists of a maximum of 5 rounds, and a player
        wins if they achieve 3 victories before the other. In case of a tie in scores after 5 rounds, the tournament ends in a draw.

        :prints: the winner with the score
    """
    player1_score = 0
    player2_score = 0
    player1_name=input("enter player 1 name:")
    player2_name=input("enter player 2 name:")
    game_round=1

    while game_round <= 5:
        print(f"Round {game_round} Starts now!!!")

        # Get player choices
        player1_pick=input(f"{player1_name}, enter your choice (R/P/S): ")
        player2_pick = input(f"{player2_name}, enter your choice (R/P/S): ")

        # Validate choices
        valid_choices = {'R', 'P', 'S'}
        if player1_pick not in valid_choices or player2_pick not in valid_choices:
            print("Invalid input! Please enter R, P, or S only.")
            continue
        # Calling the function game(player_1,player_2)
        score=game(player1_pick,player2_pick)
        if score==1:
            player1_score+=1
            print(f"{player1_name} Won this round!")
            print(f"{player1_name}:{player1_score} & {player2_name}:{player2_score}")
            game_round+=1
        elif score==2:
            player2_score += 1
            print(f"{player2_name} Won this round!")
            print(f"{player1_name}:{player1_score} & {player2_name}:{player2_score}")
            game_round += 1
        elif score==0:
            print(f"Round ended with a tie!")
            print(f"{player1_name}:{player1_score} & {player2_name}:{player2_score}")
            print(f"Replaying Round : {game_round}")
        if (player1_score==3 and player2_score==0) or (player1_score==0 and player2_score==3):
            break
    # Determine round winner
    if player1_score > player2_score:
        print(f"{player1_name} won the tournament!")
    elif player2_score > player1_score:
        print(f"{player2_name} won the tournament!")
    else:
        print("Tournament ended with a tie!")

#Qustion 2#
def sum_digits(num):
    """
    Calculates the sum of the digits of a given number.

    :param: num (int): A positive integer.

    :return: int: The sum of the digits of the number.
    """
    total = 0
    while num > 0:
        total += num % 10  # Add the last digit
        num //= 10         # Remove the last digit
    return total

def close_to_ten(num):
    """
    Rounds a number up to the nearest multiple of 10.

    :param: num (int): A positive integer.

    :return: int: The nearest multiple of 10.
    """
    if num % 10 == 0:  # If already a multiple of 10, return it
        return num
    return (num // 10 + 1) * 10  # Round up to the nearest 10


def valid_id(id_num):
    """
    Validates an Israeli ID number using a checksum algorithm.

    :param: id_num (int): A positive integer representing the ID number.

    :prints: str: "OK" if the ID is valid, "ERROR" if the ID is invalid.

    """
    id_str = str(id_num).zfill(9)  # Ensure the ID has 9 digits
    if len(id_str) != 9 or not id_str.isdigit():
        print("ERROR")   # Invalid format

    total = 0
    for i, digit in enumerate(id_str):
        num = int(digit) * (1 if i % 2 == 0 else 2)  # Multiply by 1 or 2 based on position
        total += sum_digits(num)  # Sum the digits of the result

    # Check if total is divisible by 10
    if total % 10 == 0:
        print("OK")
    else:
        print("ERROR")

#Qustion 3#
def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    The GCD is the largest number that evenly divides both input numbers. This function repeatedly
    replaces the larger number by the remainder when divided by the smaller number, until the remainder
    is zero. The GCD is the last non-zero remainder.

    :param:a (int): First number.
    :param:b (int): Second number.

    :return: int: The GCD of the two input numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def max_prime_divider(n):
    """
    Find the largest prime factor of a given number.

    This function finds the largest prime number that divides the input number without leaving a remainder.

    :param: n (int): The number to find the largest prime factor for.

    :return: int: The largest prime factor of the number.
    """
    i = 2
    largest = 1
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 1
    if n > 1:
        largest = n
    return largest

def max_common_prime_divider(num1, num2):
    """
    Find the largest Common Prime Divisor of two numbers.

    The Max Common Prime of two numbers is the largest number that divides both of them without leaving a remainder.

    :param: a (int): First number.
    :param: b (int): Second number.

    :return: int: The GCD of the two numbers.
    """
    common_divisor = gcd(num1, num2)
    return max_prime_divider(common_divisor)

#Qustion 4#
def is_perfect(n):
    """
    Checks if a given number is a perfect number.

    A perfect number is a number that is equal to the sum of its proper divisors
    (excluding itself). For example, 6 is a perfect number because 1 + 2 + 3 = 6.

    :param: n (int): The number to check.

    :return: bool: True if the number is perfect, False otherwise.
    """
    # Find the sum of all divisors of n (excluding n itself)
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:  # Check if i is a divisor of n
            divisors_sum += i
    return divisors_sum == n  # Check if the sum equals n

# Function to find all perfect numbers up to a given number
def perfect_numbers(num):
    """
    Finds all perfect numbers up to a given number.

    A perfect number is a number that is equal to the sum of its proper divisors
    (excluding itself). This function generates all such numbers from 1 to num.

    :param: num (int): The upper limit for finding perfect numbers.

    :return: nothing

    :prints: list: A list of all perfect numbers up to num.
    """

    perfects = []
    for n in range(1, num + 1):  # Check every number from 1 to num
        if is_perfect(n):
            perfects.append(n)  # Add perfect numbers to the list
    print("Perfect numbers are:",perfects)


#TESTER#
def main_tester():
    print("Check game function")
    print(game("R","S"))
    print(game("S", "R"))
    print(game("P", "R"))
    print(game("R", "P"))
    print(game("S", "S"))

    # tournament()

    print("\n\nCheck sum_digit function:")
    print(sum_digits(5))
    print(sum_digits(14))
    print(sum_digits(12345))


    print("\n\nCheck close_to_ten function:")
    print(close_to_ten(9))
    print(close_to_ten(10))
    print(close_to_ten(22))
    print(close_to_ten(141))


    print("\n\nCheck valid_id function:")
    valid_id("543700421")
    valid_id("543700422")
    valid_id("206264541")
    valid_id("206264551")


    print("\n\nCheck max_common_prime_divider function:")
    print(max_common_prime_divider(14,21))
    print(max_common_prime_divider(17,101))
    print(max_common_prime_divider(4,4))
    print(max_common_prime_divider(50,25))
    print(max_common_prime_divider(21,1))
    print(max_common_prime_divider(21,2))

    print("\n\nCheck max_prime_divider function:")
    print(max_prime_divider(21))
    print(max_prime_divider(8))
    print(max_prime_divider(5))
    print(max_prime_divider(1981))
    print(max_prime_divider(399))
    print(max_prime_divider(11935))
    print(max_prime_divider(106))


    print("\n\nCheck is_perfect function:")
    print(is_perfect(6))
    print(is_perfect(20))
    print(is_perfect(28))
    print(is_perfect(8128))
    print(is_perfect(17))

    print("\n\nCheck perfect_numbers function:")
    perfect_numbers(5)
    perfect_numbers(6)
    perfect_numbers(29)
    perfect_numbers(10000)


main_tester()
