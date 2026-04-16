# The script of the game goes in this file.
image reggie = "images/reggie.png"
image bracketTemplate = "images/bracketTemplate.png"
default tutorial_active = True
default matches_started = 0
# Characters
define n = Character(None) # Narrator
define e = Character(None, what_italic=True, what_color="#58eafd") # Special events. Emphasis.
define m = Character("Me")
define r = Character(name="Reggie", color="#32f35c")
define p1 = Character(name="red dot", color="#ffe449")
define p2 = Character(name="SaggyMilkJug", color="#c7ffcf")
define p3 = Character(name="colorfulʚɞ", color="#ee89e0")
define p4 = Character(name="Blue Line", color="#f77c7c")
define p5 = Character(name="Nyramyss", color="#778af7")
define p6 = Character(name="Kitsch", color="#5ddbf1")
define p7 = Character(name="Ford", color="#f89451")
define p8 = Character(name="Pacil", color="#9cffbb") # Currently does not have an image

# Give each character a profile picture
define player_pictures = {p1: "p1 cropped", p2: "p2 cropped", p3: "p3 cropped", p4: "p4 cropped", p5: "p5 cropped", p6: "p6 cropped", p7: "p7 cropped", p8: "p8 cropped"}

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
style venue_button is button:
    idle_background Frame(Solid("#9dddf3"), 4, 4)
    hover_background Frame(Solid("#5db2ce"), 4, 4)
    padding (30, 30)
    background Frame(Solid("#9dddf3"), 4, 4)

style venue_button_text:
    align (0.5, 0.5)

style setups_button is button:
    idle_background Frame(Solid("#ddf39d"), 4, 4)
    hover_background Frame(Solid("#b2ce5d"), 4, 4)
    padding (30, 30)
    background Frame(Solid("#ddf39d"), 4, 4)

style setups_button_text:
    align (0.5, 0.5)

style bracket_button is button:
    idle_background Frame(Solid("#f39ddd"), 4, 4)
    hover_background Frame(Solid("#ce5db2"), 4, 4)
    padding (30, 30)
    background Frame(Solid("#f39ddd"), 4, 4)

style bracket_button_text:
    align (0.5, 0.5)

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

style start_set_button is button:
    xysize(700, 70)
    background Frame(Solid("#3870e0"))
    hover_background Frame(Solid("#3366cd"))
    align (0.5, 0.5)

style start_set_button_text:
    align (0.5, 0.5)
    color "#ffffff"

style start_set_button_disabled is button:
    xysize(700, 70)
    background Frame(Solid("#cecece"))
    align (0.5, 0.5)

style start_set_button_disabled_text:
    align (0.5, 0.5)
    color "#ffffff"

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

screen venue_screen():
    add "background 2"
    # Buttons to transition to the bracket and setups screens
    textbutton "{color=#000000}Bracket{/color}":
        style "bracket_button"
        align (0.95, 0.825)
        text_align 1.0
        xsize 200

        action [
            Show("bracket_screen"),
            Hide("venue_screen")
        ]
    textbutton "{color=#000000}Setups{/color}":
        style "setups_button"
        align (0.95, 0.95)
        text_align 1.0
        xsize 200

        action [
            Hide("venue_screen"),
            Show("setups_screen")
        ]

screen setups_screen():
    add Solid("#000000")

    if not tutorial_active:
        key "mouseup_1" action NullAction()

    # Buttons to transition to the venue and bracket screens
    textbutton "{color=#000000}Venue{/color}":
        style "venue_button"
        align (0.95, 0.825)
        text_align 1.0
        xsize 200

        action [
            Hide("setups_screen"),
            Show("venue_screen")
        ]
    textbutton "{color=#000000}Bracket{/color}":
        style "bracket_button"
        align (0.95, 0.95)
        text_align 1.0
        xsize 200

        action [
            Show("bracket_screen"),
            Hide("setups_screen")
        ]

    # The setups and players
    $ alignments = [(0.25, 0.1), (0.75, 0.1), (0.25, 0.9), (0.75, 0.9)]
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

    add "bracketTemplate"
    key "mouseup_1" action NullAction()

    # Buttons to transition to the venue and setups screens
    textbutton "{color=#000000}Venue{/color}":
        style "venue_button"
        align (0.95, 0.825)
        text_align 0.5
        xsize 200

        action [
            Hide("bracket_screen"),
            Show("venue_screen")
        ]
    textbutton "{color=#000000}Setups{/color}":
        style "setups_button"
        align (0.95, 0.95)
        text_align 0.5
        xsize 200

        action [
            Show("setups_screen"),
            Hide("bracket_screen")
        ]
    
    # Winners Round 1
    for i, match in enumerate(wr1):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (87, 115 + (115 * i) + (i * 3))

            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 1, i, wr2, lr1), current_match=match), 
                    Hide("bracket_screen")
                ]
    
    
    # Winners Round 2
    for i, match in enumerate(wr2):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            # Y-position: Y-padding + Half the height of a set button + Half the height between set buttons
            # + (Height of set button + height between set buttons) * 2 * i
            pos (75 + (315 * 1), 100 + (90 // 2) + ((130 - 90) // 2) + (120 * 2 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 2, i, wf, lr2), current_match=match), 
                    Hide("bracket_screen")
                ]
    
    
    # Winners Finals
    for i, match in enumerate(wf):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (45 + (315 * 2), 90 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 4 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 3, i, gf, lf), current_match=match),
                    Hide("bracket_screen")
                ]
    
    
    # Grand Finals
    for i, match in enumerate(gf):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (10 + (315 * 3), 90 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 8 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 4, i, tf, tf), current_match=match),
                    Hide("bracket_screen")
                ]
    
    
    # True Finals
    for i, match in enumerate(tf):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (-20 + (315 * 4), 90 + ((90 // 2) + ((130 - 90) // 2)) * 3 + (130 * 16 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(True, 5, i, None, None), current_match=match),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Round 1
    for i, match in enumerate(lr1):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (95, 50 + 60 + (130 * len(wr1)) + (120 * i))

            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 1, i, lr2, lr2), current_match=match),
                    Hide("bracket_screen")
                ]
    
    # Losers Round 2
    for i, match in enumerate(lr2):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (75 + (315 * 1), 50 + 60 + (130 * len(wr1)) + (120 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 2, i, lr3, lr3), current_match=match),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Round 3
    for i, match in enumerate(lr3):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (45 + (315 * 2), 50 + 60 + (130 // 2) + (130 * len(wr1)) + (130 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 3, i, lf, lf), current_match=match),
                    Hide("bracket_screen")
                ]
    
    
    # Losers Finals
    for i, match in enumerate(lf):
        $ p1_color = match.get_player_color(match.get_p1())
        $ p2_color = match.get_player_color(match.get_p2())
        textbutton "{size=23}{color=[p1_color]}[match.get_p1_name()]{/color}\n{size=15}{color=#000}vs.{/color}{/size}\n{color=[p2_color]}[match.get_p2_name()]{/color}{/size}":
            style "set_button"
            pos (5 + (315 * 3), 50 + 60 + (130 // 2) + (130 * len(wr1)) + (130 * i))
            if match.is_callable():
                action [
                    Show("match_report_screen", player_a=match.get_p1(), player_b=match.get_p2(),
                    advancement_data=BracketAdvancementDataHolder(False, 4, i, gf, gf), current_match=match),
                    Hide("bracket_screen")
                ]

# Screen for reporting the matches. Pass the players as arguments
screen match_report_screen(player_a, player_b, advancement_data, current_match):
    key "mouseup_1" action NullAction()
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

    # Start a set button
    # Once started, a set cannot be stopped
    if find_setup(setups, player_a, player_b) is not None:
        textbutton "{color=#ffffff}Match Started{/color}":
            align(0.5, 0.75)
            style "start_set_button_disabled"
    elif find_open_setup(setups) is not None:
        textbutton "{color=#ffffff}Start Match{/color}":
            align(0.5, 0.75)        
            style "start_set_button"
            action [
                Function(call_set, setups=setups, p1=PlayerPicture(player_a, player_pictures[player_a]), p2=PlayerPicture(player_b, player_pictures[player_b])),
                SetVariable("matches_started", matches_started + 1),
                SetVariable("player_a_active_button", None),
                SetVariable("player_b_active_button", None),
                SetVariable("a_selected_gamecount", None),
                SetVariable("b_selected_gamecount", None),
                Show("bracket_screen"),
                Hide("match_report_screen"), 
                Return()
            ]
    else:
        textbutton "{color=#ffffff}Cannot Start Match{/color}":
            align(0.5, 0.75)
            style "start_set_button_disabled"

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
            Function(current_match.report, 
                    winner=determine_winner(player_a, player_b, a_selected_gamecount, b_selected_gamecount)),
            Function(clear_setup, setups=setups, p1=player_a, p2=player_b),
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
    # $ setups[0].set_players(PlayerPicture(p1, "p1 cropped"), PlayerPicture(p2, "p2 cropped"))
    # $ setups[1].set_players(PlayerPicture(p3, "p3 cropped"), PlayerPicture(p4, "p4 cropped"))
    # $ setups[2].set_players(PlayerPicture(p5, "p5 cropped"), PlayerPicture(p6, "p6 cropped"))
    # $ setups[3].set_players(PlayerPicture(p7, "p7 cropped"), PlayerPicture(p8, "p8 cropped"))
    # call screen setups_screen


    # Script
    # n "Why did I come here again?"
    # n "I was just supposed to be playing Super Smash Bros, and I ended up getting roped into coming to a tournament."
    # scene background 2
    # n "My friends told me this would be fun, but I haven't seen much happen yet."
    # n "There's just a bunch of people playing and talking about things like \"frame data\" that I don't understand."
    # n "Where's the tournament organizer anyways? Aren't they supposed to be here by now?"
    # n "Wait, I feel like a new challenger is approaching..."
    # show expression Solid("#fff") as flash
    # with dissolve
    # pause 0.1
    # hide flash
    # with dissolve
    # show reggie at right with moveinright
    # with vpunch
    # r "My body is ready!"
    # r "Hello! It's me, Reggie Fils-Aimé, former CEO of Nintendo, and also the tournament organizer of this competition, or TO for short."
    # r "Thanks for showing up, we're going to make this the greatest tournament ever held for this children's party game."
    # r "Hopefully you came prepared, as today's performance will determine the future of your gaming career."
    # r "With that being said, let's get started. Good luck, have fun. Alright everyone, quit your friendlies!"
    # r "I'm gonna have [p1.name] and [p2.name] on setup 1, [p3.name] and [p4.name] on setup 2,..."
    # r "...[p5.name] and [p6.name] on setup 3, and [p7.name] and [p8.name] on setup 4. Okay everyone, good luck and have f—"
    # # REMOVED FOR NOW
    # # $ call_set(setups, PlayerPicture(p1, player_pictures[p1]), PlayerPicture(p2, player_pictures[p2]))
    # # $ call_set(setups, PlayerPicture(p3, player_pictures[p3]), PlayerPicture(p4, player_pictures[p4]))
    # # $ call_set(setups, PlayerPicture(p5, player_pictures[p5]), PlayerPicture(p6, player_pictures[p6]))
    # # $ call_set(setups, PlayerPicture(p7, player_pictures[p7]), PlayerPicture(p8, player_pictures[p8]))
    # hide reggie
    # # TODO: Play phone ringing noise
    # e "{cps=5}Ring... Ring... Ring...{nw}{/cps}"
    # show reggie at left with moveinleft
    # r "Hello? What's that, Mr. Sakurai? You need me back at Nintendo headquarters immediately in order to promote Mario Kart 14 featuring Shaquille O'Neal?"
    # r "Well I suppose that does sound pretty important. I'll be there right away!"
    # show reggie at center with move
    # r "It seems I've been called away on very important business. I'll have to have someone else run this tournament for me."
    # r "{cps=10}How about... you there?{/cps}"
    # with hpunch
    # m "Me?!"
    # m "No way, this is my first tournament and I don't even know how to-"
    # r "Perfect! I'm sure you'll do great. Ta-ta now!"
    # hide reggie with moveoutleft

    # n "Good grief, how did I get myself into this situation?"
    # n "I could just leave, but that doesn't feel right. Didn't Reggie say that today would decide the future of my gaming career? That sounds pretty important."
    # n "I think I've seen one of my friends do something like this before. How hard could it be?"
    # n "Alright, I can make it through this. I can do this."
    # with hpunch
    # m "Everyone, quit your friendlies!"

    # # Tutorial
    # scene black with fade
    # e "Welcome to the TO's Chair. Since Reggie is off promoting Mario Kart 14, you're in charge of the bracket."
    # e "Here is how a Smash Tournament works:"
    # show screen venue_screen with dissolve
    # e "From the {b}Venue{/b}, you'll access the core of the tournament."
    # e "The buttons on the right allow you to jump between the {b}Bracket{/b} and the {b}Setups{/b}."
    # hide screen venue_screen
    # show screen setups_screen with dissolve
    # e "{b}Assigning Setups{/b}: When players approach you to start a set, you'll need to find them an open setup in the room."

    # e "A 'setup' is just a TV and a console ready for a match."
    # e "You'll be able to see who is playing at what setup on this screen. During the tournament, you'll need to assign players to open setups so that players can start their sets."
    # e "You can start matches from the bracket screen by clicking on a set and then clicking the \"Start Match\" button."
    # hide screen setups_screen with dissolve
    # e "{b}Double Elimination{/b}: Most Smash events are 'Double Elimination'. Lose once, and you go to the Losers Bracket. Lose twice, and you're out! In a tournament bracket, it'll look like this."
    # show bracketTemplate at truecenter with dissolve
    # e "{b}The Bracket{/b}: This is the map of the tournament. This will be shown at appropriate times throoughout the game, and those white boxes will be filled in with players' names."
    # e "Players are paired in 'Sets'. Clicking a set button will let you report the outcome."
    # hide bracketTemplate with dissolve
    # show match_report at truecenter with dissolve
    # e "{b}Reporting Scores{/b}: When a set finishes, a player will come to you with their score." 
    # e "You'll use this screen to input the games won by each player. Accuracy is key!"
    # e "This is also where you'll start sets."
    # hide match_report with dissolve
    # e "{b}Your Goal{/b}: Keep the tournament moving! If a set is ready to be played, make sure the players find a setup."
    # m "Okay... bracket, scores, winners, losers. I think I've got the hang of it."
    # $ tutorial_active = False

    scene background 2 with fade
    n "The room is buzzing with energy. It's time to get this bracket moving."
    n "I should check the bracket and see which sets are ready to be played."
    # Show the bracket and have the player choose 4 1st round matches to start
    python:
        # Reset the counter before starting this segment
        matches_started = 0
    label match_starting_loop:
        if matches_started < 4:
            n "I need to get at least [4 - matches_started] more matches running."
            call screen bracket_screen
            # When the player clicks "Start Match", the screen returns here
            jump match_starting_loop
        else:
            n "That looks like a good start. The setups are mostly full now."
    
    n "Oh! It looks like someone's finished playing their set."
    show p2 at left onlayer screens with dissolve
    p2 "Hello, I beat [p1.name] 2-1. They got DESTROYED hahaha."
    m "Okay, I'll have to input that into the bracket."

    # 1st set report (winners round 1, SaggyMilkJug)
    # Copyable logic for reporting a set. Use this format when you want the player to input a score after a set finishes
    $ a_correct_gamecount = 1
    $ b_correct_gamecount = 2
    hide p2 onlayer screens with dissolve
    call screen venue_screen
    $ results = _return
    if results[0] == a_correct_gamecount and results[1] == b_correct_gamecount and results[2] == p2:
        s "Success! The score was recorded correctly." 
    else:
        f "Failure. That wasn't the correct score, or perhaps you reported the wrong set."

    # show screen room_screen_with_button

    # 2nd set report (winners round 1, colorful)
    show p3 at left onlayer screens with dissolve
    p3 "Hey, I beat [p4.name] 2-0."
    m "Sounds good! I'll input that for you now."

    # Copyable logic for reporting a set. Use this format when you want the player to input a score after a set finishes
    $ a_correct_gamecount = 2
    $ b_correct_gamecount = 0
    # hide screen room_screen
    hide p3 onlayer screens with dissolve
    call screen venue_screen
    $ results = _return
    if results[0] == a_correct_gamecount and results[1] == b_correct_gamecount and results[2] == p3:
        s "Success! The score was recorded correctly." 
    else:
        f "Failure. That wasn't the correct score, or perhaps you reported the wrong set."

    n "Two sets have just finished, which means that there's currently two empty setups."
    show screen venue_screen
    n "I should see if I can call any sets to fill the setups."

    # Waiting for losers r1
    label wait_for_losers_match:
    show screen venue_screen
    n "I should see if I can call any sets to fill the setups"
    
    # This pauses the script and lets the player use the UI
    call screen bracket_screen 

    # Check if the match has been started yet
    $ current_match = find_setup(setups, p1, p4)
    if current_match is None:
        n "I still need to get that Losers match between [p1.name] and [p4.name] started."
        jump wait_for_losers_match
    
    # 3rd set report (losers round 1, red dot)
    hide screen venue_screen
    show p1 angry at left onlayer screens
    p1 "{cps=50}Dang ZSS is so busted with her frame 1 jab, she gets away with WAY TOO MUCH{nw}{/cps}"
    p1 "{cps=60}And don't get me even started on flip kick having invulnerability. I don't know who's idea it was to add that {nw}{/cps}"
    p1 "{cps=70}I can't stand this stupid character, WE NEED TO BAN HER IMMEDIATELY AND GET RID OF ALL ZSS PLAYERS AT THIS TOURNAMENT {nw}{/cps}"
    m "{cps=2}.  .  .  {nw}{/cps}"
    n "What's this guy's problem? He must've lost pretty badly I suppose."
    m "Uh... alright. What was the score for your set?"
    hide p1 angry onlayer screens
    show p1 happy at left onlayer screens
    p1 "Oh! I won 2-0."
    n "I can't believe it. I've never met such a sore winner before."
    m "Okay I'll put that in for you."

    $ a_correct_gamecount = 0
    $ b_correct_gamecount = 2
    hide screen room_screen
    hide p3 onlayer screens
    call screen venue_screen
    $ results = _return
    if results[0] == a_correct_gamecount and results[1] == b_correct_gamecount and results[2] == p1:
        s "Success! The score was recorded correctly." 
    else:
        f "Failure. That wasn't the correct score, or perhaps you reported the wrong set."
    
    return
