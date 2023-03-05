# verification-with-emoji-for-a-discord-server
verification with emoji for a discord server
First, create a role named "Unverified" and assign it to all new members joining your server.

Next, create a channel named "verification" or any name of your preference, where the verification process will take place.

In the "verification" channel, create a message with instructions on how to verify with an emoji.

Then, create an emoji that will serve as the verification symbol.

Finally, create a script using a Discord bot that listens for reactions to the message in the "verification" channel. When a user reacts with the emoji, the bot will remove the "Unverified" role from the user and grant them access to the rest of the server.


This script listens for the "👍" emoji reaction in the "verification" channel. Once detected, it finds the "Unverified" role and removes it from the user who reacted with the emoji. This grants the user full access to the server.
