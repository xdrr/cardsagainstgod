# Cards Against Isolation Client

Achieve god mode with this dedicated client for the [cards agains
isolation game](https://github.com/dparrish/cards-against-isolation/).

Play the game [here](https://cards-against-isolation.web.app/footbal).

## Description

The cards against isolation game is an online take on the cards against
humanity card game. The game uses socket.io to provide an elegant message
exchange infrastructure. The server design allows all users to perform
some actions that allow cheating and other hilarities.

This client allows a user to join any game and promptly start messing
with game state by issuing accepted messages to the server.

## Accepted message

 - `play_card` - have a player select their card
 - `end_round` - end the current round and start winner selection
 - `set_player_name` - set any player's name
 - `choose_winner` - choose the winner when the game is at the winner selection phase
 - `start_vote` - start a vote modal with a chosen text message
 - `vote` - place a vote towards an ongoing vote

## LICENSE

See LICENSE.TXT
