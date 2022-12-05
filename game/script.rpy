# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jeff = Character("Jeffery Adams", color="f44336")
define mar = Character('Margaret Adams', color="#ff71b6")
define cole = Character('Cole (You)', color="#da7a7a")
define luis = Character('Sherrif Luis', color="#ff9f3b")
define alex = Character('Alex', color= "b2ff87")
define amy = Character('Amy', color= "b58adf")
define n = Character('Narrator', color="#999999")
define morg = Character('Morgan', color= "bcd5ed")
define jes = Character("Jesse", color="c49f35")

default reputation = 0

# The game starts here.

label start:

    play music "audio/intromusic.mp3"

    scene bg blacksmith

    n "Just on the outside of town lives and works a lonely blacksmith, Cole."

    show cole

    cole "{i}Phew.{/i} Another day working the iron."
    cole "I guess it's a little {i}hot{/i}... haha."
    n "Distant screams can be heard in the distance."

    show cole sad

    cole "Who on earth is disruptin' my peace and quiet on this fine afternoon?"

    hide cole sad

    scene bg town
    with fade

    n "Cole decides to venture into the town to see what's going on."

    show cole

    cole "{i}What's going on?{/i} Everyone's runnin' around like animals!"

    show cole at left
    with move
    show amy angry

    amy "\"HELP! HELP! THE MAYOR'S GONE MISSING!\""
    cole "\"Woaaah, calm down there, ma'am.\""
    amy "\"HOW DO YOU EXPECT ME TO STAY CALM. PEOPLE DON'T JUST DISAPPEAR.\""
    cole "\"I'm sure there's a perfectly wonderful explanation for ya ma'am.\""

    show amy

    amy "*panting* \"Mayor Adams walks around town every day and asks everyone how they're doin', it just ain't like him to go missing.\""

    menu:
        "What should I say?"

        "Offer to Help":
            show cole at left

            cole "\"I'll help look for 'em if it'll keep you quiet.\""
            jump .offerHelp

        "Tell her to stop whining.":
            jump .stopWhining


    return

label .offerHelp:

    show amy

    amy "\"Oh you will! Oh me oh my! Thank the heavens for sendin' you down to me!\""

    cole "No prob, what can I do?"

    amy "\"We should go ask Margaret, she is my best friend and the wife of the mayor! She should have some answers!\""

    hide cole
    with moveoutright
    hide amy
    with moveoutright

    jump .meetMargaret

label .stopWhining:

    $ reputation = reputation - 1
    show cole sad at left
    cole "\"Would you quit your whinin'? I'm startin' to get real sick of it!\""

    show amy angry
    amy "\"You're a horrible man there, Mister Cole.\""

    amy "\"Won't you please help me find em'?\""

    show cole at left

    cole "\"Okay, okay, I'll help you out if you just calm down for a second there ma'am!\""

    hide amy angry

    jump .offerHelp

label .badReputation:

    scene bg blacksmith
    with fade

    show cole at right
    with easeinright

    n "\"Cole decides to go back to his blacksmithing shop and ignore the ruckus going on within the town.\""

    show jeff
    show cole sad at right

    cole "{i}GASP{\i} \"What is this!?\""

    show amy angry at left
    with easeinleft

    amy "\"Look y’all, our mayor is missing ‘cause of this man!\""

    n "Everyone in the town gathers around to see what's going on."

    show mar sad
    with easeinleft

    mar "\"HOW COULD YOU! OH MY DEAR!\""

    show luis angry at left
    with easeinleft

    luis "\"Hands up you!\""

    scene black

    n "Cole was arrested by Sheriff Luis for the murder of Mayor Adams. It seems Cole had such a poor reputation in town that the murderer easily framed Cole."
    n "It might be worth trying again to see if you can achieve a more satisfying ending."
    n "Thanks for playing!"


label .meetMargaret:

    scene bg margaret house
    with fade

    show mar sad at left
    with easeinleft
    show amy
    with moveinleft
    show cole at right
    with moveinleft

    amy "\"Oh Margaret! I heard o’ the bad news!\""

    mar "\"Oh yes! My dear Jeffery did not come home from his meeting last night! He always come home so early, but I saw no sign of him.\""

    amy "\"We should go around and ask for help! Margaret, you and Cole go around town and ask some townsfolk!\""
    amy "\"Hurry, go go!\""

    mar "\"Where should we go?\""

    menu:
        "Where do you want to go?"

        "Go see Alex and Morgan":
            jump .meetAlexAndMorgan

        "Walk around the town":
            jump .walkAroundTown

label .meetAlexAndMorgan:

    cole "\"Alex and Morgan just moved into town, they are close to me. I’ll talk to them.\""
    mar "\"Okay, I trust you now. I'll stay here with Amy.\""

    scene bg house
    with fade

    n "Cole walks to Alex and Morgan's house."

    show cole at left
    with moveinleft
    show alex
    with easeinright
    show morg at right
    with easeinright

    cole "\"Howdy, have you seen Mayor Jeffery around here?\""

    alex "\"Not that I’ve seen ‘mate.\""

    morg "\"Hmm, actually I think I saw him last night walking into some random farm and that’s about it. I still need to learn more about this area, haha.\""

    cole "\"Farm? Where?\""

    morg "\"Not sure actually, but the farm near the tavern.\""

    cole "\"Amy’s house? Her house is a farm.\""

    morg "\"Oh hm, yeah I think so.\""

    alex "\"Is there something serious going on bud?\""

    cole "\"Well, ya see, don’t panic but the mayor gone missing…\""

    show alex shocked
    show morg shocked at right

    morg "{i}gasping{\i} \"Uh- what now?!\""

    cole "\"SSHHHH!!!\""

    cole "\"I’m trying to find him, but you guys don’t tell anyone about this. Just be on the lookout and tell me if you see him. I’m going to go check on Amy.\""

    show alex

    alex "\"Alrighty now, we’ll tell you if we catch him.\""

    scene bg margaret house
    with fade

    show mar sad at left
    with easeinleft
    show cole
    with moveinright

    cole "\"We’ll go check up on Amy, Alex and Morgan said Mayor Jefferey walked into her farm or some farm near her house last night.\""

    mar "\"Okay\" {i}sniffs{\i}"

    hide mar at left
    with moveoutleft
    hide cole bored
    with moveoutleft

    scene bg amy farm
    with fade
    show mar
    with moveinright
    show cole sad at right
    with moveinright

    cole "\"Her house is always so quiet for some’ reason now.\""

    mar "\"Oh, don’t mind her now dear, she is just like that.\""

    n "{i}Cole loudly knocks twice on Amy's door.{\i}"

    n "{i}Several loud noises arise from inside the farmhouse{\i}"

    show amy angry at left
    with easeinleft

    amy "\"Oh- oh hi, what brings you here? Why are you here all of a sudden? Did you find the mayor?\""

    cole "\"No, but Alex and Morgan said they saw mayor Jeffery walk into some nearby farmhouse in this area last night. You remember anything like that, Amy?\""

    amy "\"No. Nope, I don’t.\""

    amy "\"Well, come on now let’s go. Let’s go check up on other farmhouses and maybe search for him now y’all.\""

    show mar sad

    cole "\"Yeah alrighty then.\""

    hide mar sad
    with easeoutleft
    hide amy angry at left
    with easeoutleft
    hide cole angry at right
    with easeoutleft

    scene bg field
    with fade

    show mar
    with easeinright
    show cole at right
    with easeinright
    show amy at left
    with easeinleft

    cole "\"Mayor! O’ Mayor!\""

    amy "\"Come on, let’s go into the houses and search.\""

    mar "\"I think I have a good idea. Let’s get sheriff Luis involved. It’ll speed things up now\""

    show amy angry at left

    amy "\"Hmm no, I think we’ll be okay, let’s keep looking!\""

    menu:
        "What should we do?"

        "Continue looking.":
            jump .continueLooking

        "Go see Sheriff Luis":
            jump .meetSheriff

        "Ignore both of them. Just leave":
            jump .ignore
    return


label .continueLooking:

    cole "\"Yeah, let’s keep looking around first.\""

    mar "\"No! We can’t waste no more time! Let’s go see sheriff now!\""

    menu:
        "What should we do?"

        "Continue looking.":
            jump .continueLooking

        "Go see Sheriff Luis":
            jump .meetSheriff

        "Ignore both of them. Just leave":
            jump .ignore
    return

label .meetSheriff:

    show amy angry at left

    cole "\"Alrighty, where is sheriff Luis’s office?\""

    mar "\"Follow me now, it is near my home.\""

    amy "\"Hey wait! How about you guys go, I- I’ll stay here! Just to keep an eye and to search more at this area! I’ll report to you if I see anything suspicious!\""

    mar "\"Why thank ya dear. You are such a blessing!\""

    hide mar
    with easeoutright
    hide cole bored at right
    with easeoutright
    hide amy
    with easeoutleft

    scene bg sheriff
    with fade


    show mar at right
    with easeinright
    show cole
    with easeinright

    mar "\"Here we are at the sheriff's office.\""

    mar "\"Ohhh Luis!\""

    show luis at left
    with easeinleft

    luis "\"Hey hey! What’s the business here?\""

    show mar sad at right

    mar "\"Oh my, my husband, he was supposed to come home from his meeting last night but he has not returned!\""

    mar "\"Oh I am worried oh my, where he could he be? We searchin’ everywhere but no sign!\""

    luis "\"Mayor J’s missing?!\""

    mar "\"Oh he has! I- I am just too sad to talk about it…\""


    show cole

    cole "\"Good mornin’ sir, what happened was…\""

    scene bg sheriff
    with pixellate

    n "Cole spends the next few minutes discussing with Sheriff Luis about everything going on."

    show mar at right
    show cole
    show luis at left

    luis "\"I see, I see. Now, Alex and Morgan said they saw him at a farm near the tavern…\""

    luis "\"Ah, this be tricky my friend. A lot of stuff and animals go missing in that area. Let’s go have a talk at Alex and Morgan’s place, eh?\""

    cole "\"Alrighty.\""

    luis "\"Alrighty, stay here for a bit while I go have a talk with Alex and Morgan.\""

    hide luis at left
    with easeoutleft

    scene bg sheriff
    with pixellate

    show cole
    show mar at right

    pause 1.0

    show luis at left
    with easeinleft

    luis "\"Alrighty then, we got some clues in our hands folks. But let me ask you this, did you happen to see if Amy might have some clues?\""

    cole "\"Hmm, we visited her house earlier today and she found nothing.\""

    luis "\"Let me go there then.\""

    hide mar
    with easeoutright
    hide cole bored at right
    with easeoutright
    hide luis at left
    with easeoutright

    scene bg amy farm
    with fade

    show cole at right
    with easeinright
    show luis
    with easeinright
    show amy at left
    with easeinleft

    cole "\"Mornin’ Amy, you mind if I take a look inside your house real quick? I just want to make sure and double check everythin’ is good.\""

    show amy angry

    amy "\"Uh well I mean sure, but really I told them there is nothing.\""

    hide luis
    with easeoutright

    show mar
    with easeinright

    amy "\"I don’t know why he is taking so long, but also I found nothing. Maybe Mayor Jefferey is somewhere else and not even in town.\""

    cole "{i}Hmm she sounds really suspicious right now, could she be…?{\i}"

    mar "\"No, I know my dear, he would never leave me like that!\""

    show mar sad

    hide cole
    with easeoutright

    show luis at right
    with easeinright

    luis "\"Yeah, everythin’ is good, sorry Amy I just wanted to make sure, ya know?\""

    amy "\"I told you, I am just very worried about our mayor, but I don’t think he is in this area.\""

    return

label .ignore:
    $ reputation = reputation - 1

    cole "\"Shut your traps! I'm sick of this. I'm not helping anymore\""

    mar "\"Cmon Cole! We're so close, please help me find my husband!\""

    cole "\"Alright alright, but calm down, you're drivin' me crazy!\""

    jump .continueLooking


label .walkAroundTown:

    scene bg town
    with fade

    show cole at left
    with moveinleft
    show mar
    with moveinleft

    cole "\"Town seems kinda empty today.\""

    mar "\"Look, there’s Jesse, let’s ask her without causing panic...\""

    cole "\"Good idea.\""

    show jes at right
    with moveinright

    cole "\"Heya Jesse, we jus’ walkin’ around town and trying to see if you saw Mayor Jeffery walking around here.\""

    show jes shocked at right

    jes "\"Hmm no, now why you ask?\""

    cole "\"We jus’ wondering ‘cause uh.. um... He was walking with us and he walked off.\""

    jes "\"Nope, you want me to go around and look?\""

    menu:
        "Do you want Jesse to look around?"

        "Say Yes":
            call .jesseYes

        "Say No":
            call .jesseNo

    if reputation < 0:
        "Your reputation is bad."
    else:
        "Your reputation is fine."

    jump .meetAlexAndMorgan

label .jesseYes:

    jes "\"Yeah yeah, I’ll come back to tell you if I see him.\""

    mar "\"Oh goodness! Thank you my dear!\""

    return

label .jesseNo:

    jes "\"Alrighty then, take care folks!\""

    cole "\"Kay, let’s go see my new friends, Alex and Morgan, maybe they can help us.\""

    return
