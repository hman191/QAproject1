# QAproject1

topTrumpsFlaskApp

# Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

## Solution
I decided to create a Top Trumps style app, which, using a database to store a list of cars and their respective statistic (out of 10), would allow users to store a deck of 5 cars they could then use to play against others.
The list of cars would only be able to be modified by a developer and not by users. As this is a game style application, this allows for fairness, as the stats would not be able to be changed.

# ERD
![ERD](https://github.com/hman191/QAproject1/blob/master/Documentation/Screen%20Shot%202020-03-07%20at%2016.24.52.png "Initial ERD")
My Initial ERD was as follows. This shows the one to one relationship between the decks and users. As this was designed as a game, it would be a good idea to make sure a user has to think carefully about what cars they use in their deck. This relationship ensures that. Each user can only have one deck, which is matced specifically to that user. This also includes a Deck for the computer controller deck which the user would be able to play against in order to earn points

