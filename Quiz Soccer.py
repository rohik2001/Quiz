# Welcome Message
print("⚽ Welcome to the Simple Soccer Program! ⚽\n")

# Step 1: Create a Soccer Team
print("--- Create Your Dream Soccer Team ---")
team_name = input("Enter your dream team's name: ")

# Collect player details
player1 = input("Enter the name of your first player: ")
player2 = input("Enter the name of your second player: ")
player3 = input("Enter the name of your third player: ")

# Display the team
print(f"\nYour Dream Team '{team_name}' has been created!")
print(f"1. {player1}")
print(f"2. {player2}")
print(f"3. {player3}")

# Step 2: Player Stats Calculator
print("\n--- Player Stats Calculator ---")
player_name = input("Enter the name of the player to calculate stats for: ")

# Check if the player is in the team
if player_name == player1 or player_name == player2 or player_name == player3:
    player_goals = int(input(f"How many goals has {player_name} scored in their career? "))
    player_years = int(input(f"How many years has {player_name} been playing professionally? "))
    
    # Calculating average goals per year
    if player_years > 0:
        avg_goals = player_goals / player_years
        print(f"\n{player_name} scores an average of {avg_goals:.2f} goals per year!")
    else:
        print(f"Invalid input for years. {player_name}'s average goals cannot be calculated.")
else:
    print(f"{player_name} is not in your dream team. Please try again.")

# Step 3: Soccer Quiz
print("\n--- Soccer Quiz ---")
score = 0

# Question 1
print("\n1. How many players are there on a soccer team during a match?")
answer1 = input("Your answer: ")
if answer1.strip() == "11":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 11.")

# Question 2
print("\n2. Which country has won the most FIFA World Cups?")
answer2 = input("Your answer: ").strip().lower()
if answer2 == "brazil":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Brazil.")

# Question 3
print("\n3. What is the name of the international trophy awarded to the FIFA World Cup winner?")
answer3 = input("Your answer: ").strip().lower()
if answer3 == "fifa world cup trophy":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'FIFA World Cup Trophy'.")

# Display Quiz Results
print(f"\n--- Quiz Results ---")
print(f"Your total score: {score}/3")
if score == 3:
    print("Amazing! You're a soccer genius!")
elif score == 2:
    print("Great job! You know your soccer pretty well.")
else:
    print("Keep practicing! Soccer trivia can be tricky.")

# Farewell Message
print(f"\nThanks for playing! Enjoy managing your dream team '{team_name}' and keep cheering for the beautiful game! ⚽")
