# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Jeffery = Character("Jeffery Adams")
define Margaret = Character('Margaret Adams', color="#da7a7a")
define Cole = Character('Cole (You)', color="#da7a7a")
define Luis = Character('Sherrif Luis', color="#da7a7a")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg town

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    Margaret "My name will show up as test in game"

    # This ends the game.

    return
