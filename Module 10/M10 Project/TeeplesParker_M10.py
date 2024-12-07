#Name: First Name Last Name
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section number
#Professor: Sharp
#Date:
#Project #: M10
#By submitting this assignment, I declare that the source code contained in this assignment was written s
#olely by me, unless specifically provided in the assignment. I attest that no part of this assignment, i
#n whole or in part, was generated by Generative Artificial Intelligence (e.g., ChatGPT, Gemini, Copilot, 
#Claude, etc.) nor obtained from a paid solution service (e.g., Chegg, Course Hero, Bartleby, etc.). I un
#derstand that copying any source code, in whole or in part, constitutes cheating, and that I will receiv
#e a zero on this project if I am found in violation of this policy.

import csv # imports csv

FILENAME = "contacts.csv" # assaignes the name of the file we are using to FILENAME

def display_title(): # define the display_title function
    print("Parker Teeples Contact Manager App") # prints "Parker Teeples Contact Manager App"
    print() # print blank line
    
def display_menu(): # defines the diplay_menu function
    print("COMMAND MENU") # prints "COMMAND MENU"
    print() # prints blank line
    print("list - Display all contacts") # prints "list - Display all contacts"
    print("view - View a contact") # prints "view - View a contact"
    print("add - Add a contact") # prints "add - Add a contact"
    print("del - Delete a contact") # prints "del - Delete a contact"
    print("exit - Exit program") # prints "exit - Exit program"
    print() # prints a blank line

def main(): # define the main function
    contacts = []
    contacts = read_contacts() # assaignes the variable contacts to the result of the function read_contacts
    display_title() # call the display_title function
    display_menu() # call the display_menu function
    while True: # while true loop
        command = input("Command: ") # command is set to the input of the user
        if command == "list": # if command is "list"
            display(contacts) # call the display function with the argument contacts
        elif command == "view": # if command is "view"
            view(contacts) # call the view function with the argument contacts
        elif command == "add": # if command is "add"
            add(contacts) # call the add function with the argument contacts
        elif command == "del": # if command is "del"
            delete(contacts) # call the delete function with the argument contacts
        elif command == "exit": # if command is "exit"
            break # break while loop
        else: # if none of the above
            print("Not a valid command. Please try again.\n") # print "Not a valid command. Please try again.\n"
    print("Bye!")

def read_contacts(): # define the read_contacts function
    contacts = [] # assaign contacts to an empty array
    try: # try following for errors
        with open(FILENAME, newline="") as file: # open the file and start a new line, as file
            reader = csv.reader(file) # set reader to file
            for row in reader: # for every row in file being read
                contacts.append(row) # append row to contacts
        return contacts # return contacts
    except FileNotFoundError: # if there is a FileNotFoundError
        print("Could not find contacts file! Starting new contacts file...") # print "Could not find contacts file! Starting new contacts file..."

def display(contacts): # define the function contacts with the parameter contacts
    if not contacts: # if the length of contacts is 0
        print("There are no contacts in the list") # print "There are no contacts in the list"
    else: # else
        for i, row in enumerate(contacts, start=1): # for i and row in the enumerate of contacts starting with 1
            print(f"{i}. {row[0]}") # print i and row[0]
        print() # print blank line

def view(contacts): # define the view function with the parameter contacts
    number = get_contact_number(contacts) # set number to the result of the get_contact_number with the argument contacts
    if number > 0: # if number is bigger than zero
        contact = contacts[number-1] # set contact to contacts place of number - 1
        print("Name:", contact[0]) # print "Name:", contact[0]
        print("Email:", contact[1]) # print "Email:", contact[1]
        print("Phone:", contact[2]) # print "Phone:", contact[2]
        print() # print blank line

def get_contact_number(contacts): # define the get_contact_number with the parameter contacts
    while True: # while True
        try: # try for error
            number = int(input("Number: ")) # set number to the input from the user
        except ValueError: # if a ValueError is raised
            print("Invalid integer.\n") # print "Invalid integer.\n"
            return -1 # return -1
            
        if number < 1 or number > len(contacts): # if number is less than one or number is bigger than the length of contacts
            print("Invalid contact number.\n") # print "Invalid contact number.\n"
            return -1 # return -1
        else: # else
            return number # return number

def add(contacts): # define the add function with the parameter contacts
    name = input("Name: ") # assaign name to the users input
    email = input("Email: ") # assaign email to the users input
    phone = input("Phone: ") # assaign phone to the users input
    contact = [] # assaign contacts an empty list
    contact.append(name) # append name to the list contact
    contact.append(email) # append email to the list contact
    contact.append(phone) # append phone to the list contact
    contacts.append(contact) # append contacts to the list contact
    write_contacts(contacts) # call the function write_contacts with the argument contacts
    print(f"{contact[0]} was added.") # print "{contact[0]} was added."
    print() # print blank line

def write_contacts(contacts): # define the write_contacts function with the parameter contacts
    with open(FILENAME, "w", newline="") as file: # opeb FILENAME as write as file
        writer = csv.writer(file) # set writer to the writer of file
        writer.writerows(contacts) # write rows from contacts

def delete(contacts): # define the delete function with the parameter contacts
    number = get_contact_number(contacts) # set number to the result of get_contact_number with the argument contacts
    if number > 0: # if number is bigger than 0
        contact = contacts.pop(number-1) # set contact to contacts removed of number - 1
        print(f"{contact[0]} was deleted.\n") # print "{contact[0]} was deleted.\n"
    write_contacts(contacts) # call the function write_contacts with the argument contacts

if __name__ == "__main__":  main() # if name is main call main