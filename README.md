Secret Santa Application!

Description: To everyone who are unfamiliar with the term 'Secret Santa': This tradition refers to giving at a random person a gift during christmas period. The receiver won't know the name of its gifter (hence the name Secret Santa!) until he/she receive from him/her! The nature of what anyone receive is rather symbolic, not particularly expensive and should aim to what the receiver loves (eg. hobbies, tv series, pets etc etc.). The tradition is split in two different parts: Put your name in a bowl and pick from it to see whose person will get your present and the exchange of gifts which is kinda self-explanatory.

For the sake of this application, let me propose that this application works in two different .py's:

 The first let anyone update their preferences in a .db file called ('users'), which will be used in the second .py . The best part of it is that you can add names and preferences, update those values or delete them! I find it particulary usefull in a corporate setting where someone doesn't want to partecipate, someone else joins the team or wants somewhat specific gifts. 

 The second part is quite straightforward and let us pair up the Secret Santa with its beneficiary!

 To get technical lets explain which file does what:
 The first thing that I created was the database (database.db) using sqlite3 after setting it up on my visual studio code. Using a sql file and the extension from visual studio code, I started initializing a table with this command:
 
  "CREATE TABLE users(
                    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                    name TEXT NOT NULL,
                    preferences TEXT NOT NULL,
                    budget INTEGER NOT NULL);
                    

The entire idea of the application can be seen inside what I just created: The primary key is the user id which will start at 1 and going up the more users will join the secret santa. I will leverage this to actually pair up the couples. The name is a text representing the human itself and to distinguish it from others. We dont add edge cases like equals name and we will ask the user for a name and a surname. Is based on an honor system since the scope of the project is to be used on a local level only. If we were to create a web app based on this we should be adding a "surname" row. Preferences, again, is self-explanatory and indicates what topic the gift should cover. Budget is for some future implementations based on how much money should be spent for the present. It will be global for everyone so no need for a user input (Even though I would like a Tesla myself for my secret santa). After creating my database we can start to look into the project itself.

First since is a random raffle, I imported the random library from python. In addition to that the sqlite library will give me access to the database that I created and start to manipulate datas inside of it. I defined to simple functions to see if the number of people are odd or even. If the number is odd, one person will be short of a Santa and to fix that he/she will instead win the Super Secret Santa which will be a special prize from the entire office with the double amount of budget. Someone that is selected as this person will be deceived into believing that someone else is the super secret santa to avoid any kind of suspect. To summarize the rest of the code: 
    • It creates an infinite loop using while True.
    • Inside the loop, it connects to the database and retrieves a list of existing names from the "users" table.
    • It prompts the user for an action: to insert a new name, pick Secret Santa, or close the program.
    • If the user chooses to insert a name ("I"), it prompts for a name and checks if it already exists in the database. If it does, it gives the option to update or delete the existing entry. If it doesn't exist, it prompts for preferences and budget and inserts the new user into the database.
    • The commented-out section (#Select the database only by names...)  outline the logic for picking a Secret Santa when the number of names is odd, but the implementation is missing.
    • Finally, the code reaches a part where is to be intended to handle the case when the action is to pick a Secret Santa ("S")


