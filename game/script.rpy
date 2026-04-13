# The script of the game goes in this file.
image reggie = "images/reggie.png"
# Characters
define n = Character(None) # Narrator
define e = Character(None, what_italic=True, what_color="#58eafd") # Special events. Emphasis.
define m = Character("Me")
define r = Character(name="Reggie", color="#32f35c")
# TODO: Replace these names with the real names of the players. I forgot what their real tags are.
define p1 = Character(name="red dot", color="#ffe449")
define p2 = Character(name="SaggyMilkJug", color="#c7ffcf")
define p3 = Character(name="colorfulʚɞ", color="#ee89e0")
define p4 = Character(name="Blue Line", color="#f77c7c")
define p5 = Character(name="Nyramyss", color="#778af7")
define p6 = Character(name="Kitsch", color="#5ddbf1")
define p7 = Character(name="Ford", color="#f89451")
define p8 = Character(name="Pacil", color="#9cffbb") # Currently does not have an image

# Success and failure "characters"
define s = Character(None, what_italic=True, what_color="#0cff20")
define f = Character(None, what_italic=True, what_color="#ff0c0c")

# Setups
define setups = [Setup(1), Setup(2), Setup(3), Setup(4)]

# Make bracket
define wr1 = [BracketSet(p1, p2), BracketSet(p3, p4), BracketSet(p5, p6), BracketSet(p7, p8)] # winners round 1
define wr2 = [BracketSet(), BracketSet()]
define wf = [BracketSet()] # winners finals (wr3)
define gf = [BracketSet()] # grand finals
define lr1 =[BracketSet(), BracketSet()] # losers round 1
define lr2 = [BracketSet(), BracketSet()]
define lr3 = [BracketSet()]
define lf = [BracketSet()] # losers finals
define tf = [BracketSet()] # true finals / grand finals reset


# Style vars
style blue_button is button:
    
    idle_background Frame(Solid("#9dddf3"), 4, 4)
    hover_background Frame(Solid("#5db2ce"), 4, 4)
    padding (30, 30)
    background Frame(Solid("#c5c5c5"), 4, 4)

style blue_button_text:
    color "#000000"
    size 30

style set_button:
    color "#000000"
    idle_background Frame(Solid("#ffffff"), 4, 4)
    hover_background Frame(Solid("#ffffff"), 4, 4)
    padding (10, 10)
    background Frame(Solid("#ffffff"), 4, 4)
    xysize (215, 90)


# Match report screen vars
default player_a_active_button = None
default player_b_active_button = None
default a_selected_gamecount = None # User-selected player a gamecount
default b_selected_gamecount = None # User-selected player b gamecount
default a_correct_gamecount = None # The correct gamecount for player a
default b_correct_gamecount = None # The correct gamecount for player b
style game_count_button is button:
    xysize (60, 60)
    background Frame(Solid("#dbdbdb"), radius=30)
    hover_background Frame(Solid("#9e9e9e"), radius=30)
    selected_background Frame(Solid("#2727ec"), radius=30)
    align (0.5, 0.5)

style game_count_button_text:
    size 24
    align (0.5, 0.5)
    text_align 0.5
    color "#000000"
    selected_color "#ffffff"

style submit_result_button is button:
    xysize(700, 70)
    background Frame(Solid("#e2e2e2"))
    hover_background Frame(Solid("#2727ec"))
    align (0.5, 0.5)

style submit_result_button_text:
    size 30
    align (0.5, 0.5)
    color "#000000"
    hover_color "#ffffff"

style setup_box is frame:
    background Frame(Solid("#ffffff"), 0, 0)
    padding (10, 0)

# Speech bubble styles
style speech_bubble is frame:
    background Frame(Solid("#ffffff"), 0, 0)
    padding (40, 30)

style speech_bubble_text:
    color "#000000"
    size 28
    text_align 0.0

# Timer styles
style timer_frame is frame:
    background Frame(Solid("#1a1a1a"), 10, 10)
    padding (20, 15)

style timer_text:
    color "#ffffff"
    size 36
    text_align 0.5

style timer_bar is bar:
    xsize 500
    ysize 30
    left_bar Frame(Solid("#5db2ce"), 4, 4)
    right_bar Frame(Solid("#444444"), 4, 4)

style timer_control_button is button:
    idle_background Frame(Solid("#9dddf3"), 4, 4)
    hover_background Frame(Solid("#5db2ce"), 4, 4)
    padding (15, 10)

style timer_control_button_text:
    color "#000000"
    size 20


# Screens
screen room_screen():
    add "background 2"


screen room_screen_with_button():
    add "background 2"
    
    # Go to laptop view
    textbutton "Bracket":
        # Placement and styling
        align(0.7, 0.8)
        style "blue_button"
        
        # Logic
        action [
            Show("bracket_screen", transition=easeinbottom),
            Hide("room_screen")
        ]

screen laptop_screen():
    # For now, the laptop screen is just a black background with the laptop. 
    # TODO: Get a close-up picture of the lectern for the background of this screen.
    add Solid("#000")
    add "laptop_(transparent)":
        align (0.5, 0.5)

    # Go to venue view
    textbutton "Venue":
        # Placement and styling
        align(0.7, 0.8)
        style "blue_button"

        # Logic
        action [
            Show("room_screen", transition=easeintop), 
            Hide("laptop_screen")
        ]

# Speech bubble. Pass in the text and optionally the position and size.
# vpos: "top", "middle", "bottom" (default: "bottom")
# hpos: "left", "center", "right" (default: "center")
# size: "small", "medium", "large" (default: "medium")
screen speech_bubble(message, vpos="bottom", hpos="center", size="medium"):
    $ x_positions = {"left": 0.1, "center": 0.5, "right": 0.9}
    $ y_positions = {"top": 0.1, "middle": 0.5, "bottom": 0.85}
    $ sizes = {"small": 400, "medium": 700, "large": 1100}

    # Fall back to defaults if someone passes a bad value
    $ xa = x_positions.get(hpos, 0.5)
    $ ya = y_positions.get(vpos, 0.85)
    $ w = sizes.get(size, 700)

    frame:
        style "speech_bubble"
        align (xa, ya)
        xsize w
        text message style "speech_bubble_text"

# Timer screen, requires a TimerState object (note to self see classes.rpy).
# show_controls: whether to show start/pause/reset buttons for the player
# on_expire: action(s) to run when the timer finishes (countdown/countup only)
# Note/maybe thing to look at later: Function() calls restart_interaction() every 0.1s while this screen is showing. so renpy.pause(hard=True) won't work in the same interaction, need to use dialogue or screen timers to wait for time to pass instead. (renpy.pause() and timer_screen are incompatible for whatever reason)
screen timer_screen(timer_state, show_controls=False, on_expire=None, xalign=0.5, yalign=0.0):
    # Tick the timer every 0.1 seconds. Function() restarts the interaction each tick
    # so the display stays up to date.
    timer 0.1 repeat True action Function(timer_state.tick, 0.1)

    # Fire the on_expire action exactly once when the timer finishes
    if timer_state.just_expired and on_expire is not None:
        timer 0.01 action on_expire

    frame:
        style "timer_frame"
        align (xalign, yalign)
        vbox:
            spacing 10

            # Digital readout
            text timer_state.get_display_time():
                style "timer_text"
                xalign 0.5

            # Progress bar (not shown for stopwatch since there's no limit)
            if timer_state.mode != "stopwatch":
                $ frac = timer_state.get_fraction()
                if timer_state.mode == "countdown":
                    bar value StaticValue(1.0 - frac, 1.0):
                        style "timer_bar"
                else:
                    bar value StaticValue(frac, 1.0):
                        style "timer_bar"

            # Player controls (optional)
            if show_controls:
                hbox:
                    spacing 10
                    xalign 0.5
                    if not timer_state.running and not timer_state.finished:
                        textbutton "Start":
                            style "timer_control_button"
                            action Function(timer_state.start)
                    elif timer_state.running:
                        textbutton "Pause":
                            style "timer_control_button"
                            action Function(timer_state.pause)
                    textbutton "Reset":
                        style "timer_control_button"
                        action Function(timer_state.reset)

screen setup_screen():
    add Solid("#000000")

    # The setups and players
    $ alignments = [(0.15, 0.1), (0.85, 0.1), (0.15, 0.9), (0.85, 0.9)]
    for i in range(4):
        $ setup = setups[i]
        $ alignment = alignments[i]

        hbox:
            align alignment
            if i % 2 == 0:
                # Box that says "Setup X"
                frame:
                    style "setup_box"
                    vbox:
                        xsize 150
                        ysize 400
                        text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xsize 150
                    ysize 400
                    for name, picture in setup.get_player_names_and_pictures():
                        add picture:
                            xalign 0.5
                            xysize (150, 150)
                        text "{color=#ffffff}[name]{/color}":
                            xalign 0.5
            else:
                vbox:
                    xsize 150
                    ysize 400
                    for name, picture in setup.get_player_names_and_pictures():
                        add picture:
                            xalign 0.5
                            xysize (150, 150)
                        text "{color=#ffffff}[name]{/color}":
                            xalign 0.5
                frame:
                    style "setup_box"
                    vbox:
                        xsize 150
                        ysize 400
                        text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                            xalign 0.5
                            yalign 0.5


screen bracket_screen():
    # Set buttons should be (315, 130) pixels away from each other
    # For a sample 12-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-34/event/ultimate-singles/brackets/1868263/2751603
    # For a sample 8-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-44/event/ultimate-singles/brackets/1940157/2849091
    # This will be an 8-person bracket screen

    add Solid("#000000")

    # Winners Round 1
    for i, match in enumerate(wr1):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65, 20 + (130 * i))

            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 1, i, wr2, lr1)),
                    Hide("bracket_screen")
                ]
    
    
    # Winners Round 2
    for i, match in enumerate(wr2):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            # Y-position: Y-padding + Half the height of a set button + Half the height between set buttons
            # + (Height of set button + height between set buttons) * 2 * i
            pos (65 + (315 * 1), 20 + (90 // 2) + ((130 - 90) // 2) + (130 * 2 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 2, i, wf, lr2)),
                    Hide("bracket_screen")
                ]
    
    
    # Winners Finals
    for i, match in enumerate(wf):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 2), 20 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 4 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 3, i, gf, lf)),
                    Hide("bracket_screen")
                ]
    
    
    # Grand Finals
    for i, match in enumerate(gf):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 3), 20 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 8 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 4, i, tf, tf)),
                    Hide("bracket_screen")
                ]
    
    
    # True Finals
    for i, match in enumerate(tf):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 4), 20 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 16 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 5, i, None, None)),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Round 1
    for i, match in enumerate(lr1):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65, 20 + 60 + (130 * len(wr1)) + (130 * i))

            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 1, i, lr2, lr2)),
                    Hide("bracket_screen")
                ]
    
    # Losers Round 2
    for i, match in enumerate(lr2):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 1), 20 + 60 + (130 * len(wr1)) + (130 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 2, i, lr3, lr3)),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Round 3
    for i, match in enumerate(lr3):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 2), 20 + 60 + (130 // 2) + (130 * len(wr1)) + (130 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 3, i, lf, lf)),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Finals
    for i, match in enumerate(lf):
        textbutton "{size=26}{color=#000000}[match.get_p1_name()]\n{size=18}vs.{/size}\n[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (65 + (315 * 3), 20 + 60 + (130 // 2) + (130 * len(wr1)) + (130 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 4, i, gf, gf)),
                    Hide("bracket_screen")
                ]
    
    
    # Add a line separating the Winners and Losers brackets
    # (This doesn't work right now)
    # $ bracket_separator_line = Line(0, 20 + (130 * len(wr1)) + (60 // 2), 1920, 1080)
    # $ bracket_separator_line.render(5, 5, 5, 5)
    # # $ bracket_separator_line.event(0, 0, 0, 0)

# Screen for reporting the matches. Pass the players as arguments
screen match_report_screen(player_a, player_b, advancement_data):
    add "match_report":
        align(0.5, 0.5)

    text player_a.name:
        color "#000"
        align(0.33, 0.175)

    text player_b.name:
        color "#000"
        align(0.69, 0.175)

    text player_a.name:
        color "#000"
        align (0.15, 0.52)

    text player_b.name:
        color "#000"
        align (0.15, 0.61)

    # Game count buttons
    grid 4 2:
        align (0.745, 0.57)
        xspacing 30
        yspacing 40
        for i in range(8):
            $ cur = i % 4
            textbutton "[cur]":
                style "game_count_button"
                if i <= 3:
                    selected(player_a_active_button == i)
                    action [
                        SetVariable("player_a_active_button", i), 
                        SetVariable("a_selected_gamecount", cur),
                    ]

                else:
                    selected(player_b_active_button == i)
                    action [
                        SetVariable("player_b_active_button", i), 
                        SetVariable("b_selected_gamecount", cur),
                    ]

    # Back button
    textbutton "Go Back":
        style "submit_result_button" # it looks the same anyway
        align(1 - 0.87, 0.95)
        action [
            SetVariable("player_a_active_button", None),
            SetVariable("player_b_active_button", None),
            SetVariable("a_selected_gamecount", None),
            SetVariable("b_selected_gamecount", None),
            Show("bracket_screen"),
            Hide("match_report_screen")
        ]

    # Submit result button
    textbutton "Submit Result":
        style "submit_result_button"
        align(0.87, 0.95)
        action [
            SetVariable("player_a_active_button", None),
            SetVariable("player_b_active_button", None),
            SetVariable("a_selected_gamecount", None),
            SetVariable("b_selected_gamecount", None),
            Function(advance_in_bracket, player=determine_winner(player_a, player_b, a_selected_gamecount, b_selected_gamecount), advancement_data=advancement_data),
            Function(send_to_losers, player=determine_loser(player_a, player_b, a_selected_gamecount, b_selected_gamecount), advancement_data=advancement_data),
            Return((a_selected_gamecount, b_selected_gamecount, determine_winner(player_a, player_b, a_selected_gamecount, b_selected_gamecount))),
            Hide("match_report_screen")
        ]
        # action [
        #     Show("post_match_report_screen", selected_agmc=a_selected_gamecount, selected_bgmc=b_selected_gamecount, 
        #                                     agmc=a_correct_gamecount, bgmc=b_correct_gamecount), 
        #     Hide("match_report_screen")
        # ]


# Shown after the player submits the game score
# selected_agmc = The user-selected gamecount for player_a, selected_bgmc = The user_selected gamecount for player_b
# agmc = The correct gamecount for player_a, bgmc = The correct gamecount for player_b
screen post_match_report_screen(selected_agmc, selected_bgmc, agmc, bgmc):
    add "background 4":
        align(0.5, 0.5)

    # TODO: Add more robust success and failure states
    
    # Success!
    if selected_agmc == agmc and selected_bgmc == bgmc:
        timer 0.01 action Function(renpy.say, s, "Success! The score was recorded correctly.")

    # Failure
    else:
        timer 0.01 action Function(renpy.say, f, "Failure. That wasn't the correct score.")

    textbutton "Return to Venue":
        align (0.5, 0.8)
        style "blue_button"
        action [Hide("post_match_report_screen"), Show("room_screen_with_button")]



# The game starts here.

label start:
    # call screen bracket_screen
    $ setups[0].set_players(PlayerPicture(p1, "p1 cropped"), PlayerPicture(p2, "p2 cropped"))
    $ setups[1].set_players(PlayerPicture(p3, "p3 cropped"), PlayerPicture(p4, "p4 cropped"))
    $ setups[2].set_players(PlayerPicture(p5, "p5 cropped"), PlayerPicture(p6, "p6 cropped"))
    $ setups[3].set_players(PlayerPicture(p7, "p7 cropped"), PlayerPicture(p8, "p8 cropped"))
    call screen setup_screen
 
    # Previous code
    # scene black
    # m "Quit your friendlies!"

    # call screen room_screen

    # TEST for the match report screen.
    # player_a == "blah", player_b == "blahblah". 
    # If the user correctly enters the gamescore as 3-0, "Success!" will show, 
    # Otherwise, "Failure" will show.
    # $ a_correct_gamecount = 3
    # $ b_correct_gamecount = 0
    # call screen match_report_screen("blah", "blahblah")


    # Script
    n "Why did I come here again?"
    n "I was just supposed to be playing Super Smash Bros, and I ended up getting roped into coming to a tournament."
    scene background 2
    n "My friends told me this would be fun, but I haven't seen much happen yet."
    n "There's just a bunch of people playing and talking about things like \"frame data\" that I don't understand."
    n "Where's the tournament organizer anyways? Aren't they supposed to be here by now?"
    n "Wait, I feel like a new challenger is approaching..."
    show expression Solid("#fff") as flash
    with dissolve
    pause 0.1
    hide flash
    with dissolve
    show reggie at right with moveinright
    with vpunch
    r "My body is ready!"
    r "Hello! It's me, Reggie Fils-Aimé, former CEO of Nintendo, and also the tournament organizer of this competition, or TO for short."
    r "Thanks for showing up, we're going to make this the greatest tournament ever held for this children's party game."
    r "Hopefully you came prepared, as today's performance will determine the future of your gaming career."
    r "With that being said, let's get started. Good luck, have fun. Alright everyone, quit your fr-"
    hide reggie
    # TODO: Play phone ringing noise
    e "{cps=5}Ring... Ring... Ring...{nw}{/cps}"
    show reggie at left with moveinleft
    r "Hello? What's that, Mr. Sakurai? You need me back at Nintendo headquarters immediately in order to promote Mario Kart 14 featuring Shaquille O'Neal?"
    r "Well I suppose that does sound pretty important. I'll be there right away!"
    show reggie at center with move
    r "It seems I've been called away on very important business. I'll have to have someone else run this tournament for me."
    r "{cps=10}How about... you there?{/cps}"
    with hpunch
    m "Me?!"
    m "No way, this is my first tournament and I don't even know how to-"
    r "Perfect! I'm sure you'll do great. Ta-ta now!"
    hide reggie with moveoutleft

    n "Good grief, how did I get myself into this situation?"
    n "I could just leave, but that doesn't feel right. Didn't Reggie say that today would decide the future of my gaming career? That sounds pretty important."
    n "I think I've seen one of my friends do something like this before. How hard could it be?"
    n "Alright, I can make it through this. I can do this."
    with hpunch
    m "Everyone, quit your friendlies!"

    # TODO: Tutorial text. Tell the players how the game works

    hide background 2
    show screen room_screen_with_button

    # TODO: Show the bracket and have the player choose 2-3 1st round matches to start

    hide screen room_screen_with_button
    show screen room_screen
    
    n "Oh! It looks like someone's finished playing their set."
    # TODO: For now, this is just a random player. In the finished game, make sure the player shown is someone who was actually playing a set
    show p2 at left onlayer screens
    p2 "Hello, I beat [p1.name] 2-1. They got DESTROYED hahaha."
    n "Okay, I'll have to input that into the bracket"

    # Copyable logic for reporting a set. Use this format when you want the player to input a score after a set finishes
    $ a_correct_gamecount = 1
    $ b_correct_gamecount = 2
    call screen bracket_screen
    # call screen match_report_screen("player_2", "player_3")
    $ results = _return
    if results[0] == a_correct_gamecount and results[1] == b_correct_gamecount and results[2] == p2:
        scene background 4
        s "Success! The score was recorded correctly." 
    else:
        scene background 4
        f "Failure. That wasn't the correct score, or perhaps you reported the wrong set."

    hide p2
    show screen room_screen_with_button
    
    return
