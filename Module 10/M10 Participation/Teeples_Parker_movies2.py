import csv # import csv
import sys # import sys

FILENAME = "movies_two.csv" # FILENAME is set to 'movies.csv'

def exit_program(): # define the exit_program function
    print("Terminating program.") # print "Terminating program."
    sys.exit() # exit the program

def read_movies(): # define the read_movies function
    try: # try following for errors
        movies = [] # movies is made as a list
        # raise FileNotFoundErrorr
        with open(FILENAME, newline="") as file: # open the file and start a new line, as file
            reader = csv.reader(file) # set reader to file
            for row in reader: # for every row in file being read
                movies.append(row) # append row to movie
        return movies # return movies
    except FileNotFoundError as e: # if there is a FileNotFoundError set as e
        print(f"Could not find {FILENAME} file. Making new one") # print "Could not find {FILENAME} file. Making new one"
        return [] # return []
    except Exception as e: # if any other error set as e
        print(type(e), e) # print type(e), e
        exit_program() # call the exit_program function

def write_movies(movies): # define the write_movies function with the parameter movies
    try: # try for errors
        # raise BlockingIOError('test BlockingIOError')
        with open(FILENAME, "w", newline="") as file: # open file as write starting newline
            writer = csv.writer(file) # writer is set to file
            writer.writerows(movies) # writer writes rows from movies
    except OSError as e: # if OSError found, set as e
        print('OSError Found') # print 'OSError Found'
        print(type(e), e) # print type(e), e
        exit_program() # call the exit_program function
    except Exception as e:
        print(type(e), e) # print type(e), e
        exit_program() # call the exit_program function

def list_movies(movies): # define the function list_movies with the parameter movies
    for i, movie in enumerate(movies, start=1): # for i and movie in enumerate of movies starting at 1
        print(f"{i}. {movie[0]} ({movie[1]})") # print "{i}. {movie[0]} ({movie[1]})"
    print() # print blank line
    
def add_movie(movies): # define the add_movie function
    name = input("Name: ") # set name to the users input
    while True: # while true
        try: # try for error
            year = int(input("Year: ")) # year is set to the int of the users input
            if year <= 0: # if year is smaller or equal to 0
                raise ValueError # raise a value erorr
            movie = [name, year] # set the movie list to name, year
            movies.append(movie) # append movie to movies
            write_movies(movies) # call the function write_movies with the argument movies
            print(f"{name} was added.\n") # print "{name} was added.\n"
            return # return
        except ValueError: # if a value error
            print('Please enter valid year (greater than 0)') # print 'Please enter valid year (greater than 0)'

def delete_movie(movies): # define the delete_movies function with the parameter movies
    while True: # while true
        try: # try for error
            number = int(input("Number: ")) # set number to the int of the users input
        except ValueError: # if a value error is raised
            print("Invalid integer. Please try again.") # print "Invalid integer. Please try again."
            continue # continue program
        if number < 1 or number > len(movies): # if number is smaller than one or bigger than the length of movies
            print("There is no movie with that number. Please try again.") # print "There is no movie with that number. Please try again."
        else: # else
            break # break
    movie = movies.pop(number - 1) # movie is set to movies with number - 1 popped out
    write_movies(movies) # call the function write_movie with the argumnet movies
    print(f"{movie[0]} was deleted.\n") # print "{movie[0]} was deleted.\n"

def display_menu(): # define the display_menu function
    print("The Movie List program") # print "The Movie List program"
    print() # print blank line
    print("COMMAND MENU") # print "COMMAND MENU"
    print("list - List all movies") # print "list - List all movies"
    print("add -  Add a movie") # print "add -  Add a movie"
    print("del -  Delete a movie") # print "del -  Delete a movie"
    print("exit - Exit program") # print "exit - Exit program"
    print() # print blank line

def main(): # define the main function
    display_menu() # call the display_menu function
    movies = read_movies() # set movies to the result of calling the read_movies function
    while True: # while true 
        command = input("Command: ") # set command to the input of the user
        if command.lower() in ["list", 'ls']: # if command is the lower case of list or ls
            list_movies(movies) # call the list_movies function with the argument movies
        elif command.lower() == "add": # if the lowercase of command is add
            add_movie(movies) # call the add_movies function with the argument movies
        elif command.lower() == "del": # if the lowercase of command is del
            delete_movie(movies) # call the delete_movies function with the argument movies
        elif command.lower() == "exit": # if the lowercase of command is exit
            break # break loop
        else: # else
            print("Not a valid command. Please try again.\n") # print "Not a valid command. Please try again.\n"
    print("Bye!") # print "Bye!"

if __name__ == "__main__": # if name is main
    main() # call main
