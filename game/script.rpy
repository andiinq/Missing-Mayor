# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jeff = Character("Jeffery Adams", color="f44336")
define mar = Character('Margaret Adams', color="##a1eff8")
define cole = Character('Cole (You)', color="#da7a7a")
define luis = Character('Sherrif Luis', color="#ff9f3b")
define alex = Character('Alex', color = "b2ff87")
define n = Character('Narrator', color="#999999")

# The game starts here.

label start:

    play music "audio/intromusic.mp3"

    scene bg blacksmith

    show cole happy

    cole "{i}Phew.{/i} Another day working the iron."
    cole "I guess it's a little {i}hot{/i}... haha."
    n "Distant screams can be heard in the distance."

    show cole angry

    cole "Who on earth is disruptin' my peace and quiet on this fine afternoon?"

    hide cole angry

    scene bg town
    with fade

    n "Cole decides to venture into the town to see what's going on."

    show cole bored

    cole "{i}What's going on?{/i} Everyone's runnin' around like animals!"


    # This ends the game.

    return
