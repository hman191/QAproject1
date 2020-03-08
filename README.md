# QAproject1

Top Trumps Flask App

# Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

## Solution
I decided to create a Top Trumps style app, which, using a database to store a list of cars and their respective statistics (out of 10), would allow users to store a deck of 5 cars they could then use to play against others.
The list of cars would only be able to be modified by a developer and not by users. As this is a game style application, this allows for fairness, as the stats would not be able to be changed.

# CI Pipeline
![CI Pipeline](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-08%20at%2012.07.12.png "CI Pipeline")

## Technologies
* [Trello](https://trello.com/b/moiNF5ka/top-trumps-project)
* Git
* Azure
* Flask
* Azure MYSQL database server
* Jenkins
* Python
* Pytest

# Initial ERD
![ERD](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2016.28.00.png "Initial ERD")
My Initial ERD was as follows. This shows the one to one relationship between the decks and users. As this was designed as a game, it would be a good idea to make sure a user has to think carefully about what cars they use in their deck. This relationship ensures that. Each user can only have one deck, which is matced specifically to that user. This also includes a Deck for the computer controller deck which the user would be able to play against in order to earn points. Both decks are connected to the car list table with a many to one relationship, as one deck can store many cars.

# MVP ERD
![ERD](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2016.42.44.png "MVP ERD")
This is the ERD for my final product. The changes were made to fit my MVP in the time alotted. As you can see, the Computer deck is now removed, which removes the ability to play a game against a random deck. The credit system for the user is also removed. However the relationships are still maintained. The layout of the deck table is also different. This is after encountering an issue when trying to update the table with new cars for the user.

# Risk Assessment
![Risk Assessment](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2021.37.24.png "Risk Assessment")
# Wireframes
![login wireframe](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2017.11.08.png "Login Wireframe")
![Deck wireframe](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2017.18.21.png "Deck Wireframe")

# Issues and Improvements
On the Deck page, typing in the full name of a car is needed in order to update the deck, additionally, every entry needs to be filled in even if the user would like to keep the car the same. In the future I would like to add a drop-down list for each field, as well as a pre-popoulated field with the current car, to allow the user to only change what they want to.
Also, I would have liked to have a drop down list of cars next to the user's deck so they can check the stats of a specific car to help them make their decision without switching to the cars page.

In the future, to develop the project, I would add the functionality from my initial ERD. So I would add the abaility to play against a randomly generate computer controlled deck with a similar average score to the user's deck, or even against other players online, as well as a credits system so the user would have to "buy" cars from a shop in order to add an element of progression.
Finally I would like to add user groups, so that an admin would just need to login to gain access to add cars to the database for users to then add to their deck

# Acknowledgements
Everyone in the room :)

