# fabcards

A simple Flesh and Blood TCG card displayer, for use in streams.

Type in any card from Flesh and Blood TCG and the program will show it to you in a window!

Can be used with OBS. Simply capture the window and cut out the window borders if you want.

# Requirements

- Python 3
- PIL
- tkinter
- An Internet connection

# How to use

Run using the following command:

    python3 fabcards.py

Wait for it to load the cards data from https://fabdb.net (takes a couple of seconds). An empty window appears that is used to display the card. You may reposition the window however you like; note, however, that the window size is exactly the size of the card rendered, so it's best if you do not resize the window. When ready, type any card name in the console from which you launched the script and the corresponding card gets shown in the window! You can quit the program by typing in "exit".

NOTE: this app is dependent on the FaBDB.net API. If something happens to it, this app will not work, until the API connection is fixed. If required, please create a ticket under this GitHub and the connection will be fixed.
