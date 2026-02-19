import random
import time

# Store questions
quiz = [
    ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"),
    ("Which data type is immutable in Python?", ["List", "Set", "Tuple", "Dictionary"], "Tuple"),
    ("Which keyword is used to define a function in Python?", ["fun", "def", "function", "lambda"], "def"),
    ("Which collection stores unique items?", ["List", "Tuple", "Set", "Dict"], "Set"),
    ("What does 'HTTP' stand for?", [
        "Hyper Text Transfer Protocol",
        "Hyper Tool Test Program",
        "Home Transfer Text Protocol",
        "Host Transfer Total Program"
    ], "Hyper Text Transfer Protocol")
]

# Game state
running = True

# Store scores and time taken
scores = {}
time_taken = {}

# Store players
players = set()
completed_players = []


# Show leaderboard
def show_leaderboard():
    global scores, time_taken
    print("\n===== Leaderboard =====")
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], time_taken[x[0]]))  # Sort by score, then time
    for name, score in sorted_scores:
        print(f"{name}: Score = {score}, Time Taken = {time_taken.get(name, 0):.2f} sec")
    print("=======================")


# Quiz function with timer
def start_quiz(player_name):
    global quiz, completed_players

    print(f"\n{player_name} is now playing the quiz!")
    random.shuffle(quiz)

    if player_name not in completed_players:
        completed_players.append(player_name)
        scores[player_name] = 0  # Initialize score
        start_time = time.time()  # Start timer
        time_limit = 120  # 2 minutes

        for question in quiz:
            # Check time left
            elapsed = time.time() - start_time
            if elapsed >= time_limit:
                print("\nTime's up!")
                break

            remaining = int(time_limit - elapsed)
            print(f"\nTime left: {remaining} seconds")

            print("\n" + question[0])  # Print question
            print("Here are your possible options:")

            for option in question[1]:
                print(f"- {option}")

            player_answer = input("Enter your answer: ").strip()

            if player_answer.lower() == question[2].lower():
                scores[player_name] += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {question[2]}")

            print("-" * 20)

        end_time = time.time()
        total_time = end_time - start_time
        time_taken[player_name] = total_time

        print(f"\n{player_name}, your final score: {scores[player_name]}")
        print(f"Time Taken: {total_time:.2f} seconds\n")

        print("Leaderboard after your game:")
        show_leaderboard()


# Main loop
while running:
    print("\n==== QUIZ MENU ====")
    print("1 - Add Players")
    print("2 - Start Quiz Game")
    print("3 - Show Leaderboard")
    print("4 - Exit")

    choice = input("Enter your option: ").strip()

    if choice == "1":
        n = int(input("Enter number of players: "))
        for _ in range(n):
            player = input("Enter name of player: ").strip()
            players.add(player)
            if player not in scores:  # Initialize new player's score
                scores[player] = 0
                time_taken[player] = 0

    elif choice == "2":
        for player in players:
            if player not in completed_players:
                start_quiz(player)
            else:
                print(f"{player} has already played!")

    elif choice == "3":
        show_leaderboard()

    elif choice == "4":
        print("Exiting game. Goodbye!")
        running = False

    else:
        print("Invalid option, try again.")
