import random
# 1. The Range Riddle
# Objective:
# The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Code Correction
# The range() function is used to generate a sequence of numbers. However, the code snippet provided below does not work as intended. Your task is to identify why the loop might not be executing and correct the code so that it prints numbers from 5 down to 3.

# for i in range(5,2, -1):
#     print(i)

# Task 2: Your Mood Today
# Write a program that simulates different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.
moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

random.shuffle(moods)
random.shuffle(days)
print(f'today is {days[0]} and I am feeling {moods[0]}')

# Task 3: Going Backwards
# Create a countdown timer that starts from 10 and counts down to 1. Use the range() function to generate the countdown sequence. Each number should be printed on a new line. This task will help you understand how to generate a decreasing sequence with range().
for i in range(10, 0, -1):
    print(i)


# 2. Double Scoop with Nested Loops
# Objective:
# The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

# Task 1: Code Correction
# The code below is intended to print a 3x3 grid of asterisks. However, the current output is not as expected. Identify the logical errors in the nested loops and correct the code so that it prints the grid correctly, with each row of asterisks on a new line.

for i in range(3):
    for j in range(3):
        print("* ", end="")
    print()


# Task 2: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

time_of_day =['morning', 'afternoon', 'evening']
for day in days:
    for time in time_of_day:
        print(f"On {day} in the {time} I was feeling", random.choice(moods))


# Task 3: Multiplication Table
# Your task is to create a multiplication table for numbers 1 through 5. Use nested loops where the outer loop represents the multiplier and the inner loop represents the multiplicand. Print the results in a tabular format.
from tabulate import tabulate
num_one_through_five = [1, 2, 3, 4, 5]
multiplication_table = []
data = []
for multiplier in num_one_through_five:
    for multiplicand in num_one_through_five:
        data.append([f'{multiplier} x {multiplicand}', multiplier * multiplicand])
        
headers = ["Multiplicand x Multiplier", "Product"]
multiplication_table = tabulate(data, headers=headers, tablefmt="grid")
# print(multiplication_table)

# 3. Mastering Python's For Loop
# Objective:
# The aim of this assignment is to explore and practice the control statements within Python's for loop, such as break, continue, pass, and the else clause. You will correct a loop, simulate mood swings with loop control, and implement a search with an else clause.


# Task 1: Code Correction
# The loop below is meant to print all numbers from 1 to 10, but it stops prematurely due to a break statement. Correct the code so that it skips over the number 5 and continues to print the rest of the numbers.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Task 2: Your Mood Swings
# Write a program that represents your mood swings throughout a day. The program should loop over each hour of the day and assign a random mood from a list for each hour. However, at 'lunchtime' (which you can define as a specific hour), the program should not print the mood. Use the continue statement to achieve this behavior.
moods = ['Happy', 'Sad', 'Energetic', 'Calm', 'tired', "sleepy"]
random.shuffle(moods)
hour_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
def mood_swings():
    for hour in hour_of_day:
        if hour == 12:
            continue
        if hour <= 5 or hour >= 23:
            print(f"At {hour} O'clock I was sleeping")
        else:
            print(f"At {hour} O'clock I was feeling {random.choice(moods)}")
mood_swings()


# Task 3: The Persistent Loop
# Implement a for loop that searches for a specific number in a list of numbers. If the number is found, use break to exit the loop. If the loop completes without finding the number, an else clause should be used to print a message stating that the number was not found. This task will help you understand how to use the else clause in conjunction with the break statement in loops.

numbers = [1,2,3,4,5,6,7,8,9,10,]
for num in numbers:
    if num == 11:
        break
else:
    print("Number was not found")

# 4. The Marshmallow Increment Challenge
# Objective:
# The aim of this assignment is to understand the impact of increment placement within a while loop in Python. You will experiment with different placements of the increment operation and observe how it affects the loop's execution and logic.

# Task 1: Increment at the Start
# Given the following code snippet, predict the output and then run the code to verify your prediction. Explain why the output is what it is based on the placement of the increment operation.

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    
    #  based off the placement of the increment operation we get 1-5 instead of 0-4
    # because it executing before the print statement and each iteration
    
# Task 2: Increment at the End
# Modify the code from Task 1 by moving the increment operation to the end of the loop. Predict what the output will be and then run the code to check your prediction. Discuss the differences in the output and how the placement of the increment affects the loop's behavior.
marshmallows = 0
while marshmallows < 5:
    # marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

    # in this code the increment is being perfomed after each iteration which is
    # causing the off by one

# Task 3: Off-by-One Error Investigation
# Create a while loop where an off-by-one error could occur due to the placement of the increment operation. Your loop should aim to fill a bag with exactly 10 marshmallows, but due to the off-by-one error, it either has too few or too many. Correct the error and explain the importance of increment placement in preventing such errors.

marshmallows_counter = 0
while marshmallows_counter < 10:
    print(f" we have {marshmallows_counter}")
    marshmallows_counter +=1

    # here we end up with 9

#     marshmallows_counter = 0
# while marshmallows_counter < 10:
#     marshmallows_counter +=1
#     print(f" we have {marshmallows_counter}")

    # here we end up with 10.. increment placement is important because
    # we want the loop to execute the desired number of times

# 5. Loop Condition Logic
# Objective:
# The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations. Explain the role of the loop condition and the break statement in controlling the loop execution.

x = 0
while x > 0:
    print("will i print")
    if x == 5:
        break

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met. Discuss how the loop condition determines when the loop exits.

x = 0
while x < 10:
    x += 1
    print("will i print")

# Task 3: Loop with Multiple Conditions
# Create a while loop that continues to run as long as multiple conditions are true. Use the and or or operators to combine conditions. Describe how combining conditions can create more complex loop behaviors.
y = 0
while y < 10 and y < 5:
    y +=1
    print("its real low")

#  combining conditions creates more complex loop behaviors because it takes more
# things into account at once like ordering One perfect pizza for everyone at a party
    
# 6. The Art of Loop Control
# Objective:
# The aim of this assignment is to master the use of else, break, continue, and pass in conjunction with while loops. You will implement loops that utilize these control statements to manage loop execution flow.

# Task 1: Using else with while
# Write a while loop that attempts to find a specific value in a list. Use an else clause to print a message if the value is not found. Explain how the else clause works with the while loop.
primes = [2,3,5,7,11,13,17,19]
num_to_find = random.choice(primes)
i = 0
while i < len(primes):
    if primes[i] == num_to_find:
        print(f"{num_to_find} was found at index {i}")
        break
    i +=1
else:
    print(f"{num_to_find} is not in list")

    
# Task 2: Loop Interruption with break
# Create a while loop that runs indefinitely, printing out the current time. Use a break statement to exit the loop if a certain condition is met (e.g., if the current time matches a target time). Discuss how the break statement can be used to exit a loop based on a condition.
from datetime import datetime, timedelta
current_date = datetime.now()
delta = timedelta(hours=30)
hourPlus30 = current_date + delta
while True:
    print(current_date)
    current_date += timedelta(hours=1)
    if current_date >= hourPlus30:
        break



# Task 3: Skipping Iterations with continue
# Develop a while loop that iterates over a range of numbers. Use the continue statement to skip over specific numbers (e.g., multiples of 3) and print the rest. Explain the purpose of the continue statement and how it affects the loop's iteration.
numbers = [1,2,3,4,5,6,7,8,9,10,]
index = 0
while index < len(numbers):
    num = numbers[index]
    index +=1
    if num % 2 == 0:
        continue
    print("Index: ",num)

    # continue filters out information we dont want


# Task 4: The Placeholder pass
# Implement a while loop where you want to temporarily skip the implementation of a condition but plan to add more code later. Use the pass statement as a placeholder. Describe the use of pass in a loop and when it might be useful.
new_counter = 0
while new_counter < 100:
    new_counter += 1
    print("New Counter: ",new_counter)
    if 100 % new_counter == 0:
        pass

# pass lets us skip a conditial so we may come back to it

# 7. Python's Random Game Night
# Objective:
# The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs. You will simulate a dice-rolling game and extend it to include more complex game mechanics.

# Task 1: Dice Rolling Simulator
# Using the provided code snippet, simulate rolling a six-sided die 10 times. Extend the simulation to keep track of how many times each number is rolled. After the simulation, print out the frequency of each number.


# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
keys = list(roll_count.keys())
for key in keys:
   if key in roll_count:
      roll_count[key] += 1
print(roll_count)

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    print("Dice Roll: ", "You rolled a " + str(dice_roll) + "!")
    if dice_roll in roll_count:
        roll_count[dice_roll]+= 1
    print("Roll Count: ",roll_count)
# # Print out the frequency of each number
    for number, frequency in roll_count.items():
     print(f"Number {number} was rolled {frequency} times.")

# Task 2: Random Choice Game
# Create a game where a player has to guess the random item picked by the computer from a list. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
NBA_Teams = ["Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "LA Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"]
NFL_Teams = [ "Arizona Cardinals",
    "Atlanta Falcons",
    "Baltimore Ravens",
    "Buffalo Bills",
    "Carolina Panthers",
    "Chicago Bears",
    "Cincinnati Bengals",
    "Cleveland Browns",
    "Dallas Cowboys",
    "Denver Broncos",
    "Detroit Lions",
    "Green Bay Packers",
    "Houston Texans",
    "Indianapolis Colts",
    "Jacksonville Jaguars",
    "Kansas City Chiefs",
    "Las Vegas Raiders",
    "Los Angeles Chargers",
    "Los Angeles Rams",
    "Miami Dolphins",
    "Minnesota Vikings",
    "New England Patriots",
    "New Orleans Saints",
    "New York Giants",
    "New York Jets",
    "Philadelphia Eagles",
    "Pittsburgh Steelers",
    "San Francisco 49ers",
    "Seattle Seahawks",
    "Tampa Bay Buccaneers",
    "Tennessee Titans",
    "Washington Football Team"]
MLB_Teams = [ "Arizona Diamondbacks",
    "Atlanta Braves",
    "Baltimore Orioles",
    "Boston Red Sox",
    "Chicago White Sox",
    "Chicago Cubs",
    "Cincinnati Reds",
    "Cleveland Guardians",
    "Colorado Rockies",
    "Detroit Tigers",
    "Houston Astros",
    "Kansas City Royals",
    "Los Angeles Angels",
    "Los Angeles Dodgers",
    "Miami Marlins",
    "Milwaukee Brewers",
    "Minnesota Twins",
    "New York Yankees",
    "New York Mets",
    "Oakland Athletics",
    "Philadelphia Phillies",
    "Pittsburgh Pirates",
    "San Diego Padres",
    "San Francisco Giants",
    "Seattle Mariners",
    "St. Louis Cardinals",
    "Tampa Bay Rays",
    "Texas Rangers",
    "Toronto Blue Jays",
    "Washington Nationals"]
NHL_Teams = [  "Anaheim Ducks",
    "Arizona Coyotes",
    "Boston Bruins",
    "Buffalo Sabres",
    "Calgary Flames",
    "Carolina Hurricanes",
    "Chicago Blackhawks",
    "Colorado Avalanche",
    "Columbus Blue Jackets",
    "Dallas Stars",
    "Detroit Red Wings",
    "Edmonton Oilers",
    "Florida Panthers",
    "Los Angeles Kings",
    "Minnesota Wild",
    "Montreal Canadiens",
    "Nashville Predators",
    "New Jersey Devils",
    "New York Islanders",
    "New York Rangers",
    "Ottawa Senators",
    "Philadelphia Flyers",
    "Pittsburgh Penguins",
    "San Jose Sharks",
    "Seattle Kraken",
    "St. Louis Blues",
    "Tampa Bay Lightning",
    "Toronto Maple Leafs",
    "Vancouver Canucks",
    "Vegas Golden Knights",
    "Washington Capitals",
    "Winnipeg Jets"]
NBA = random.choice(NBA_Teams)
NFL = random.choice(NFL_Teams)
MLB = random.choice(MLB_Teams)
NHL = random.choice(NHL_Teams)
tries = 0
computerGuessList = [NBA, NFL, MLB, NHL]
def randomChoiceGame():
    print("Guess the team City/State and their nickname")
    whatLeague = input("From what league would you like to guess from?: MLB, NBA, NHL or NFL ")
    if whatLeague.lower() == "nba":
        tries = 5
        answer = computerGuessList[0]
        while tries > 0:
            print(f"you have {tries} left")
            guess = input("Guess a teams state/city and name proper grammar is needed: ex) the period on st. \n")
            if answer.lower() == guess.lower():
                print("YOU WIN!!!")
                break
            tries -= 1
        else:
            print(f" the answer was {answer} You have no more attempts. Game Over")
    
    if whatLeague.lower() == "nfl":
        tries = 5
        answer = computerGuessList[1]
        while tries > 0:
            print(f"you have {tries} left")
            guess = input("Guess a teams state/city and name proper grammar is needed: ex) the period on st. \n")
            if answer.lower() == guess.lower():
                print("YOU WIN!!!")
                break
            tries -= 1
        else:
            print(f" the answer was {answer} You have no more attempts. Game Over")


    if whatLeague.lower() == "mlb":
        tries = 5
        answer = computerGuessList[2]
        while tries > 0:
            print(f"you have {tries} left")
            guess = input("Guess a teams state/city and name proper grammar is needed: ex) the period on st. \n")
            if answer.lower() == guess.lower():
                print("YOU WIN!!!")
                break
            tries -= 1
        else:
            print(f" the answer was {answer} You have no more attempts. Game Over")
    
    if whatLeague.lower() == "nhl":
        tries = 5
        answer = computerGuessList[3]
        while tries > 0:
            print(f"you have {tries} left")
            guess = input("Guess a teams state/city and name proper grammar is needed: ex) the period on st. \n")
            if answer.lower() == guess.lower():
                print("YOU WIN!!!")
                break
            tries -= 1
        else:
            print(f" the answer was {answer} You have no more attempts. Game Over")

    


randomChoiceGame()

# Task 3: Shuffling a Deck
# Simulate shuffling a deck of cards using random.shuffle(). Create a list representing a deck of cards, then shuffle it and print the shuffled deck. Discuss how random.shuffle() can be used in game development or other applications.

type = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
random.shuffle(suits)
random.shuffle(type)
deck = []
for suit in suits:
    for value in type:
        shuffled = f"{value} of {suit}"
        deck.append(shuffled)
print(deck)

# 8. The Random Challenge Course
# Objective:
# The aim of this assignment is to challenge your understanding of the random package by creating a series of mini-games that require different aspects of randomness. You will create three mini-games, each focusing on a different function from the random package.




# Task 1: The Guessing Game
# Implement a number guessing game where the computer randomly selects a number within a range, and the player has to guess it. Use random.randint() to generate the number and give the player a hint after each incorrect guess whether their guess was too high or too low.

def numGuessingGame():
    answer = random.randint(1,20)
    while True:
        guess = input("Guess a number between 1 and 20 \n")
        if int(guess) < answer:
            print("guessed too Low")
        elif int(guess) > answer:
            print("guessed too high")
        else:
            print(f"your guess {guess} matches the answer {answer}")
            break
numGuessingGame()



# Task 2: The Magic 8-Ball
# Create a Magic 8-Ball program that provides random advice. Use random.choice() to select a random response from a list of possible answers every time the user asks a question.
def magicBall():
    responses =[  "Yes",
    "No",
    "It is certain",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Cannot predict now",
    "Don't count on it",
    "My sources say no",
    "Outlook not so good"]
    while True:
        askQuestion = input("What would you like to know? ")
        random_answer = random.choice(responses)
        print("8-Ball says:", random_answer)
        satisfied = input("Would you like to ask another question? (yes/no) ")
        if satisfied.lower() != "yes":
            break
magicBall()
        

# Task 3: The Card Picker
# Develop a game where the computer randomly picks a card from a deck, and the player has to guess the suit or the rank. Use random.choice() to select the card, and then check if the player's guess matches the suit or rank of the chosen card.
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
def cardPicker():
    rankOrSuit = input("what do you want to guess enter Rank or Suit ")
    if rankOrSuit.lower() == "rank":
        tries = 3
        answer = random.choice(rank)
        while tries > 0:
            print(f"you have {tries} tries left")
            guessRank = input("guess a rank ")
            if answer.lower() == guessRank.lower():
                print(f"answer {answer} matches guess {guessRank}")
                break
            tries -=1
        else:
            print(f"tough luck {answer} was the answer")

    if rankOrSuit.lower() == "suit":
        tries = 2
        answer = random.choice(suits)
        while tries > 0:
            print(f"you have {tries} tries left ")
            guessSuit = input("Guess a suit ")
            if answer.lower() == guessSuit.lower():
                print(f"answer {answer} matches guess {guessSuit}")
                break
            tries -= 1
        else:
            print(f"ran out of tries, answer was {answer}")
cardPicker()


# 9. Looping Lists - The Rhythm of Repetition
# Objective:
# Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose. By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track number
track_number = 1

# Spinning through the genres
for genre in genres:
    if genre == "Jazz":
        print(f"Now playing Track {track_number}, {genre}: 'music's soulful conversation.'")
    if genre == "Rock":
        print(f"Now playing Track {track_number}, {genre}:  'rebellion in rhythm, freedom in sound.'")
    if genre == "Hip-hop":
        print(f"Now playing Track {track_number}, {genre}: 'Hip-hop: beats, rhymes, life.'")
    if genre == "Classical":
        print(f"Now playing Track {track_number}, {genre}: 'timeless elegance in every note.'")
    track_number += 1
            

# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played.

# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track



# # Task 3: Light Show Technician Loop
# # Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show.

# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")
    


# 10. Advanced Looping Techniques
# Objective:
# Advance your looping skills by exploring more complex list manipulations. You will learn to selectively loop through parts of a list, use list comprehensions for concise code, and generate numerical lists with Python's range function.

# Task 1: The Selective DJ
# Loop through a slice of the genres list and print only the selected genres. Use slicing to create a sublist of genres from the second to the fourth track.

# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)



# Task 2: The One-Liner Band with List Comprehensions
# Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.

# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genres]
print(music_genres)
    
# Task 3: Numerical Beats with range
# Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".

# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!") 