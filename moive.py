#varaibles for movies

Documentary_movie = ["Paris is Burning", "Harlan County USA", "Minding the Gap", "Naza"]
Horror_movie = ["Perfect Blue", "Train to Busan", "Pearl", "The Conjuring", "The Thing"]
Romance_movie =["The Notebook", "But I'm a Cheerleader", "Juno", "Brokeback Mountain", "10 Things I Hate About You"]
Action_movie = ["Avatar", "John Wick", "Spiderman: Into the Spider-Verse", "Kill Bill", "The Hunger Games"]
Sci_fi_movie = ["Project Hail Mary", "Ex Machina", "I Origins","The Sacrifice", "The Martian"]

#user input, .lower() so capitalization will not be an issue
user_genre = input("What genere do you want to explore? (Documentary, Horror, Romance, Action, Sci-Fi):").lower()

if user_genre == "documentary":
    print("Here are some Documentary recommendations:")
    for index, movie in enumerate (Documentary_movie, start=1):
        print(f"{index}.) {movie}")
    
elif user_genre == "horror":
    print("Here are some Horror recommendations:")
    for index, movie in enumerate (Horror_movie, start=1):
        print(f"{index}.) {movie}")
elif user_genre == "romance":
    print("Here are some Romance recommendations:")
    for index, movie in enumerate (Romance_movie, start=1):
        print(f"{index}.) {movie}")
elif user_genre == "action":
    print("here are some Action movies:")
    for index, movie in enumerate (Action_movie, start=1):
        print(f"{index}.) {movie}")
elif user_genre == "sci-Fi" or user_genre == "sci fi ":
    print("Here are some Sci-Fi movies")
    for index, movie in enumerate (Sci_fi_movie, start=1):
        print(f"{index}.){movie}")
else:
    print("Sorry, that genre isn't in our list")
