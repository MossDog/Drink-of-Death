# Drink-of-Death
This is a sim of the Korean game, "Drink of Death"

# Rules
1. A leader is randomly picked in the group.
2. The group shouts "drink of death" and then each person points randomly at someone else.
3. The leader then calls out a number.
4. The leader then says the number 1.
5. The person the leader is pointing to says the next number.
6. The person the second person is pointing to then says the next number.
7. Steps 5 & 6 repeat until someone calls out the number picked by the leader, this person then takes a drink!.
8. The game is then finished

# Implementation
1. No. of participants is supplied via command line arguments.
2. Leader can be chosen manually or randomly
3. Each participant points to another person before the game begins (they cannot point at themselves)
4. Number of steps the game will take to complete can be chosen manually or randomly
5. The game should be printed out as it runs

# Additional requirements
Add a way of detecting when the game enters a loop and how long it takes for the game to enter a loop.
Add a way to count how many loops emerge in a game and find the largest loop (ie. the loop with the most players in it).