# Scoring Assistant
# This program helps you assign scores to the entertainment you consume!

descriptions = {0: "Insufferable", 1: "Awful", 2: "Very Bad", 3: "Bad", 4: "Weak", 5: "Average / Mediocre",
                 6: "Decent", 7: "Good", 8: "Great", 9: "Fantastic", 10: "Superb"}

def start_assistant():
    options = ["A movie", "A TV show", "Music", "A book", "A video game"]
    
    print("Welcome to the Scoring Assistant!\nBecause it's up to you what you like or not.")
    print("What would you like to evaluate? Type the corresponding number:")
    for item in range(len(options)):
        print("{} - {}".format(item + 1, options[item]))
    user_choice = input("Your choice: ")
    
    if user_choice == "1":
        rate_a_movie()
    elif user_choice == "2":
        rate_tv()
    elif user_choice == "3":
        print("Alright, we're rating some music!")
    elif user_choice == "4":
        print("Alright, we're rating a book!")
    elif user_choice == "5":
        print("Alright, we're rating a video game!")
    else:
        print("Sorry, that's not a valid option. Please try running the program again.")

def rate_a_movie():
    movie_title = input("\nType the title of the movie you want to rate: ")
    movie_title_capitalized = movie_title.title()

    score = 0
    
    print("\nWould you like to give the movie an overall score or would you rather rate individual aspects and let us calculate the score?")
    user_preference = input("Type 1 to give a general score or 2 to evaluate individual parts separately: ")

    if user_preference == "1":

        # Asking the user to rate the movie directly
        print("\nWhat's your score for the movie {}?".format(movie_title_capitalized))
        for rating in descriptions.keys():
            print("{}: {}".format(rating, descriptions[rating]))
        score = float(input("Your score between 0 and 10 (with one decimal place): "))
        score = round(score, 1)
        if score == 10.0:
            score = int(score)
        print("You have rated the movie {} a {} out of 10. Thanks for using the Scoring Assistant!".format(movie_title_capitalized, score))

    elif user_preference == "2":
        
        # Showing the user what the criteria are
        print("\nThese are the criteria you'll be evaluating:")
        criteria = {"Plot": 0, "Acting": 0, "Directing": 0}
        for criterion in criteria.keys():
            print(criterion)
        
        # Asking if the user wants to add something to the list
        will_add = input("Would you like to add another criterion to the list? Type Y or N: ")
        if will_add.upper() == "Y":
            new_criterion = input("Type your additional criterion: ")
            criteria[new_criterion] = 0
        elif will_add.upper() != "N":
            print("Sorry, we didn't catch that. We'll assume you're OK with those criteria and continue the process.")
        
        # Getting the user's rating for each individual criterion
        print("\nThese descriptions will help you assign a score:")
        for rating in descriptions.keys():
            print("{}: {}".format(rating, descriptions[rating]))
        for criterion in criteria.keys():
            user_rating = input("How do you rate the {} of the movie {}? Type S to skip. ".format(criterion.lower(), movie_title_capitalized))
            if user_rating.upper() == "S":
                criteria[criterion] = False
            else:
                criteria[criterion] = int(user_rating)
        
        # Getting the average
        used_criteria = 0
        for criterion in criteria.keys():
            if criteria[criterion] != False:
                score += criteria[criterion]
                used_criteria += 1
        score = score / used_criteria
        score = round(score, 1)
        if score == 10.0:
            score = int(score)
        
        print("You have rated the movie {} a {} out of 10. Thanks for using the Scoring Assistant!".format(movie_title_capitalized, score))

def rate_tv():
    show_title = input("\nType the title of the TV show you want to rate: ")
    show_title_capitalized = show_title.title()

    score = 0

    print("\nWould you like to rate the whole show, a particular season or a particular episode?")
    what_to_rate = input("Type 1 for the whole show, 2 for a particular season or 3 for a particular episode: ")
    if what_to_rate == "1":
        print("Nice! Let's go!")
    elif what_to_rate == "2":
        season = input("\nOkay, which season are we evaluating? Type the number: ")
    elif what_to_rate == "3":
        episode_title = input("\nType the title of the episode: ").title()
        season = input("Which season is this episode? Type the number: ")
        episode = input("What's the number of the episode in the season? ")
    else:
        print("Sorry, that's not a valid option. Please try running the program again.")
        return

    print("\nWould you like to give it an overall score or would you rather rate individual aspects and let us calculate the score?")
    user_preference = input("Type 1 to give a general score or 2 to evaluate individual parts separately: ")

    if user_preference == "1":

        # Asking the user to rate the show directly
        if what_to_rate == "1":
            print("\nWhat's your score for the show {}?".format(show_title_capitalized))
        elif what_to_rate == "2":
            print("\nWhat's your score for season {} of {}?".format(season, show_title_capitalized))
        elif what_to_rate == "3":
            print("\nWhat's your score for {} {}x{} - {}?".format(show_title_capitalized, season, episode, episode_title))
        
        for rating in descriptions.keys():
            print("{}: {}".format(rating, descriptions[rating]))
        score = float(input("Your score between 0 and 10 (with one decimal place): "))
        score = round(score, 1)
        if score == 10.0:
            score = int(score)
        
        if what_to_rate == "1":
            print("You have rated {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, score))
        elif what_to_rate == "2":
            print("You have rated {} season {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, season, score))
        elif what_to_rate == "3":
            print("You have rated {} {}x{} - {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, season, episode, episode_title, score))

    elif user_preference == "2":
        
        # Showing the user what the criteria are
        print("\nThese are the criteria you'll be evaluating:")
        criteria = {"Plot": 0, "Acting": 0, "Directing": 0}
        for criterion in criteria.keys():
            print(criterion)
        
        # Asking if the user wants to add something to the list
        will_add = input("Would you like to add another criterion to the list? Type Y or N: ")
        if will_add.upper() == "Y":
            new_criterion = input("Type your additional criterion: ")
            criteria[new_criterion] = 0
        elif will_add.upper() != "N":
            print("Sorry, we didn't catch that. We'll assume you're OK with those criteria and continue the process.")
        
        # Getting the user's rating for each individual criterion
        print("\nThese descriptions will help you assign a score:")
        for rating in descriptions.keys():
            print("{}: {}".format(rating, descriptions[rating]))
        for criterion in criteria.keys():
            
            if what_to_rate == "1":
                user_rating = input("How do you rate the {} of {}? Type S to skip. ".format(criterion.lower(), show_title_capitalized))
            elif what_to_rate == "2":
                user_rating = input("How do you rate the {} of {} season {}? Type S to skip. ".format(criterion.lower(), show_title_capitalized, season))
            else:
                user_rating = input("How do you rate the {} of {} {}x{} - {}? Type S to skip. ".format(criterion.lower(), show_title_capitalized, season, episode, episode_title))

            if user_rating.upper() == "S":
                criteria[criterion] = False
            else:
                criteria[criterion] = int(user_rating)
        
        # Getting the average
        used_criteria = 0
        for criterion in criteria.keys():
            if criteria[criterion] != False:
                score += criteria[criterion]
                used_criteria += 1
        score = score / used_criteria
        score = round(score, 1)
        if score == 10.0:
            score = int(score)
        
        if what_to_rate == "1":
            print("You have rated {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, score))
        elif what_to_rate == "2":
            print("You have rated {} season {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, season, score))
        elif what_to_rate == "3":
            print("You have rated {} {}x{} - {} a {} out of 10. Thanks for using the Scoring Assistant!".format(show_title_capitalized, season, episode, episode_title, score))

start_assistant()