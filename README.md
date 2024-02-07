# Secret Santa
#### Video Demo:  <URL HERE>
#### Description:
![Secret Santa](https://img.freepik.com/free-vector/hand-drawn-secret-santa-illustration_23-2149162315.jpg)

For those unfamiliar with the term 'Secret Santa': This tradition involves giving a random person a gift during the Christmas period. The recipient won't know the name of their gift-giver (hence the name Secret Santa!) until they receive their gift! The nature of the gifts is usually symbolic, not particularly expensive, and should aim to reflect what the recipient loves (e.g., hobbies, TV series, pets, etc.). The tradition is divided into two parts: putting your name in a bowl and picking from it to see whose present you will buy, and the exchange of gifts, which is somewhat self-explanatory.

For the sake of this application, let me propose that it works in two different .py files:

The first allows anyone to update their preferences in a .db file called 'users', which will be used in the second .py. The best part is that you can add names and preferences, update those values, or delete them! I find it particularly useful in a corporate setting where someone may not want to participate, someone else joins the team, or someone wants somewhat specific gifts.

The second part is quite straightforward and lets us pair up the Secret Santa with their beneficiary!

To get technical, let's explain what each file does: The first thing I created was the database (database.db) using sqlite3 after setting it up in my Visual Studio Code. Using an SQL file and the extension from Visual Studio Code, I started initializing a table with this command:

"CREATE TABLE users( user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, preferences TEXT NOT NULL, budget INTEGER NOT NULL);

The entire idea of the application can be seen in what I just created: The primary key is the user ID, which will start at 1 and increase as more users join the Secret Santa. I will leverage this to actually pair up the participants. The name is text representing the person themselves and to distinguish them from others. We don't handle edge cases like identical names, and we will ask the user for both a name and a surname. It is based on an honor system since the scope of the project is for local use only. If we were to create a web app based on this, we should add a "surname" row. Preferences, again, are self-explanatory and indicate what topic the gift should cover. Budget is for future implementations based on how much money should be spent on the present. It will be global for everyone, so there's no need for user input (even though I would like a Tesla for my Secret Santa). After creating my database, we can start looking into the project itself.

Firstly, since it's a random raffle, I imported the random library from Python. In addition to that, the SQLite library will give me access to the database that I created and allow me to manipulate data inside it. I defined two simple functions to check if the number of people is odd or even. If the number is odd, one person will be short of a Santa, and to fix that, they will instead receive the Super Secret Santa, which will be a special prize from the entire office with double the budget. The person selected for this will be deceived into believing that someone else is the Super Secret Santa to avoid any suspicion. To summarize the rest of the code:

• It creates an infinite loop using while True.

• Inside the loop, it connects to the database and retrieves a list of existing names from the "users" table.

• It prompts the user for an action: to insert a new name, pick Secret Santa, or close the program. • If the user chooses to insert a name ("I"), it prompts for a name and checks if it already exists in the database. If it does, it gives the option to update or delete the existing entry. If it doesn't exist, it prompts for preferences and budget and inserts the new user into the database.

• The commented-out section (#Select the database only by names...) outlines the logic for picking a Secret Santa when the number of names is odd, but the implementation is missing.
Finally, the code reaches a part where it is intended to handle the case when the action is to pick a Secret Santa ("S"). The code first checks if the user action (action) is to pick Secret Santas (if action == "S":). If so, it proceeds to assign Secret Santas based on the number of names in the database. It executes an SQL query to count the number of names in the database (cursor.execute("SELECT COUNT(name) FROM users")) and fetches the result using fetchone(). If there are names in the database (if row:), it retrieves the count from the fetched row and checks if it's odd using the odd() function. If the count is odd, it selects a Super Secret Santa randomly from the list of names fetched from the database. If the count is odd, it selects a Super Secret Santa randomly from the list of names fetched from the database. If the count is even, it shuffles the list of names to ensure randomness and assigns Secret Santas to each person. It iterates through the shuffled list, assigning the next person in the list as the Secret Santa for the current person. After assigning Secret Santas, it asks the user if they want to close the application (end = input("Secret Santas are assigned! Do you want to close the application? (Y/N)").upper()). If the user inputs "Y", the loop is broken, and the application closes. Otherwise, the loop continues for further user interaction. This part of the code effectively assigns Secret Santas based on the number of names in the database and allows the user to choose whether to continue or close the application after the assignment is done. The choice of a dictionary is quite useful, since we have only two pieces of data and we need to assign to each key (The gifter) a value (The giftee). So after we initialize our dictionary as an empty one, we enumerate the key-value pair for each person in the table and since we are using a list we don't need to keep track of each person already assigned. The modulo operator, since the list is even (we already dealt with that issue with the Super Secret Santa, in case the number of people is odd), makes sure that the list wraps around in the beginning, else the last person will be left with no Santas :C

Hopefully that's all, and that was CS50.

Edoardo Buono
