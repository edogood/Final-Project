#Importing SQL library and random library
import sqlite3
import random
connection = sqlite3.connect("secretsanta.db")

def even(number):
    return number % 2 == 0

def odd(number):
    return number % 2 != 0

#Ask to input name, if already in database ask if it wants to update or delete
print("Made By Edoardo Buono as CS50 Final Project Class of '24")
while True:
    #Open the database and select a variable named users.
    
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users")
    existing_names = [row[0] for row in cursor.fetchall()]

    action = input("Do you want to Insert a Name (I), Pick Secret Santa (S) or Close the program (C)? ").upper()
    if action == "C":
        break
    if action == "I":
        username = input("Enter a Name and a Surname:")
        #Ask user for name, if already present ask if it wants to update it or delete it
        if username in existing_names:
            action = input("User already exists. Do you want to update (U) or delete (D) the entry? ").upper()
            if action == "U":
                new_preferences = input("Enter new preferences: ")
                cursor.execute("UPDATE users SET preferences = ? WHERE name = ?", (new_preferences, username))
                connection.commit()
                print("User preferences updated successfully!")
            elif action == "D":
                cursor.execute("DELETE FROM users WHERE name = ?", (username,))
                connection.commit()
                print("User deleted successfully!")
            else:
                print("Invalid action. Please enter 'U' to update or 'D' to delete.")
        else:
                preferences = input("Enter preferences: ")
                budget = input("Enter Budget: ")
                cursor.execute("INSERT INTO users (name, preferences, budget) VALUES (?, ?, ?)", (username, preferences, budget))
                connection.commit()
                print("User added successfully!")
    #Select the database only by names and check if the number of names is odd or even. If the number of names is odd, pick a random name and give it the title of SUPER SECRET SANTA
    #Super Secret Santa receive a special prize from the whole office                        
    if action == "S":

                
