import random

# List of the cities in the game
cities = ['', 'yogyakarta', 'Busan', 'Jakarta', 'Seoul', 'Travel', 'Solo', 'Gwangju', 'Semarang', 'Gangnam',
          'Trash', 'Surabaya', 'Jeju', 'Bandung', 'Incheon', 'Bonus', 'Aceh', 'Daejeon', 'Palembang', 'Daegu']

# define function for rolling the dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)  # generate random number between 1-6

# define function for checking prime number
def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:  # checking if the remainder is equal to 0
            return False  # if function applied, it is not a prime number
    return True  # if function denied, it is return to true

# define function for simulating dice roll
def simulate_dice_rolls(n):  # rolls the dice n times
    counts = [0] * 13  # Index 0 and 1 are not used (sums range from 2 to 12)
    for _ in range(n):
        roll_sum = roll_dice()
        if 2 <= roll_sum <= 12:  # Only count sums between 2 and 12
            counts[roll_sum] += 1
    return counts  # return the list of counts

# define main function containing all the functions that are already defined to run the game
def main():
    rounds = 10
    accumulated_sum = 0
    skip_next = False  # Flag to skip two cities

    while rounds > 0:
        print(f"Round {rounds}")
        n = int(input("Enter the number of times to simulate rolling the dice: "))

        # simulate dice rolls using a for loop by calling the function
        counts = simulate_dice_rolls(n)

        # finding highest sum and its probability using a while loop
        max_sum = 2
        max_count = counts[max_sum]
        i = 3 # It starts at 3 because we have already initialized max_sum and max_count with the values for the sum 2
        while i <= 12:
            if counts[i] > max_count:
                max_sum = i
                max_count = counts[i]
            i += 1

        probability = max_count / n

        current_max_sum = max_sum  # save the current max_sum for output
        accumulated_sum += current_max_sum

        print(f"The highest sum of two dice rolled {n} times is {current_max_sum}.")
        print(f"It occurred {max_count} times with a probability of {probability:.4f}.")

        # get the corresponding city based on the dice sum
        city_index = accumulated_sum

        # ensure city index stays within the range of cities
        if city_index >= len(cities):
            city_index = len(cities) - 1  # set city index to the last city index if exceeded

        city = cities[city_index]

        # check if the highest sum is prime, if prime will got bonus, if not will be charged
        if prime(current_max_sum):
            print(f"Congratulations! It is {current_max_sum}, you got {city}, and it is a prime number. You win money!")
        elif city == 'Trash':
            print("Game over! You got Trash.")  # if got trash, game is over
            break
        elif city == 'Plane':
            print(f"You got {city}. Skipping the next two cities.") # if got plan, skip two cities
            skip_next = True
        else:
            print(f"Sorry! {current_max_sum}, you got {city}, but it is not a prime number. You need to pay!")

        # Skip two cities logic
        if skip_next:
            accumulated_sum += 2
            skip_next = False

        # if the accumulated sum reaches or exceeds the index of 'Daegu', game will be over
        if city_index >= cities.index('Daegu'):
            print("Game over!. Start over!")
            break

        rounds -= 1

    # if rounds left equals to 0, game will be over
    if rounds == 0:
        print("Game over! You completed all rounds without finishing the game.")

main()
