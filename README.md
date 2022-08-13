# Blackjack

This is a simple program that emulates the popular card game, Blackjack. I mainly created it for fun using my prior knowledge of how to play, but if something isn't right or a feature isn't working for some reason or another, feedback would be greatly appreciated. Thanks!

### The Objective

The premise of the game is to collect/hold onto "cards" that will add up to being as close as possible to 21. You are playing against the dealer who is attempting to achieve the same thing, and who ever can get closest to 21 first, without going over, wins. 

### How to Play 

When you run the program, you will be prompted with `Begin? (Y/N)`, and you may enter `Y` to play the game, or `N` to stop the program. _(At anytime when prompted for an input, the program will still accept a valid answer if the first letter is upper or lowercase.)_

After pressing `Y`, you will be shown both the dealer's and your two numbers. _(Normally, the dealer's second card would not be facing up, which that might be added to the program in the near future.)_ 

From there, you may type `Hit` or `Stand`. If `Hit` is inputed, you and the dealer will recieve an additional card. If `Stand` is inputed, you will not be given another card, but the dealer will, and the game will end. You may enter `Hit` as many times as you would like when prompted, however, if you go over 21, you will "bust", or automatically lose. 

### Win or Lose

There are many different ways you can win or lose a game in Blackjack; here is a list of how the program determines a win/loss.

- The person who has cards that go over 21 at any time will automatically lose. 
- If the sum of any person's cards at up to exactly 21 at any time, they automatically win.
- If you and the dealer both bust, the game will end and the result will be a loss for the player. 
- If the game is over, but both the player and the dealer's cards are under 21, who ever is closer to 21 will win that game. 
- If the game is over, but both the player and the dealer's cards are under 21 and are the same, the result will be a tie. 

### Creator's Notes

- I realize that this version of Blackjack is not on par with the traditional way of playing the card game, and I may make changes in the future in an attempt to make it more in line with the actual game in the way it is meant to be played. 
- Some examples of my program differing from the game in real life is that it gives the dealer another card when the player chooses to stand as well as revealing all of their cards throughout the game. Because of these differences, they could be used as an advantage for the player, which makes the game easier play and win. 
- In addition to those differences, I also know that when playing with cards, you may chose to 'Split', 'Double Down', and 'Surrender' at certain points in the game, and I have not added those features. As I mentioned earlier, this project mainly is for fun, but I might decide to challenge myself in the future to add these features and more. We shall see I suppose. 
- Either way, if you happen to be reading this, I appreciate you taking the time to do so and for showing interest in the game that I created. If you have any suggestions, comments, feedback, etc., I would love to hear it. Thank you!
