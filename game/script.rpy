# The script of the game goes in this file.
image reggie = "images/reggie.png"
image bracketTemplate = "images/bracketTemplate.png"
default tutorial_active = True
default matches_started = 0
default completed_sets = 0
# Characters
define n = Character(None) # Narrator
define e = Character(None, what_italic=True, what_color="#58eafd") # Special events. Emphasis.
define m = Character("Me")
define r = Character(name="Reggie", color="#32f35c")
define p1 = Character(name="red dot", color="#ffe449")
define p2 = Character(name="Surume", color="#c7ffcf")
define p3 = Character(name="colorfulʚɞ", color="#ee89e0")
define p4 = Character(name="Subzero", color="#f77c7c")
define p5 = Character(name="Nyramyss", color="#778af7")
define p6 = Character(name="Flan", color="#5ddbf1")
define p7 = Character(name="Ford", color="#f89451")
define p8 = Character(name="Pacil", color="#9cffbb")

# Give each character a profile picture
define player_pictures = {p1: "p1 cropped", p2: "p2 cropped", p3: "p3 cropped", p4: "p4 cropped", p5: "p5 cropped", p6: "p6 cropped", p7: "p7 cropped", p8: "p8 cropped"}

# Keep track of where to return if you tell a setup to quit their friendlies
define cur_label = "match_starting_loop"
# define store.current_label = "match_starting_loop"

# Keep track of how many matches are occurring at any given point
define matches_in_progress = 0

# The expected result that the player has to report
define expected_result = {"winner": p2, "loser": p1, "winner_games": -999, "loser_games": -999}

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

# Tutorial vars
define clicked_setups = False # Has the player clicked "Setups" in the tutorial?
define clicked_2 = False # Has the player clicked back to the venue from setups?


define bracket = [wr1, wr2, wf, gf, lr1, lr2, lr3, lf, tf]

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
    xysize (700, 70)
    background Frame(Solid("#e2e2e2"))
    hover_background Frame(Solid("#2727ec"))
    align (0.5, 0.5)

style submit_result_button_text:
    size 30
    align (0.5, 0.5)
    color "#000000"
    hover_color "#ffffff"

style submit_result_button_disabled is button:
    xysize (700, 70)
    background Frame(Solid("#cecece"))
    align (0.5, 0.5)

style submit_result_button_disabled_text:
    size 30
    align (0.5, 0.5)
    color "#000000"

style submit_result_button_wrong is button:
    xysize (700, 70)
    background Frame(Solid("#e2e2e2"))
    hover_background Frame(Solid("#2727ec"))
    selected_background Frame(Solid("#ec2727"))
    align (0.5, 0.5)

style submit_result_button_wrong_text:
    size 30
    align (0.5, 0.5)
    color "#000000"
    hover_color "#ffffff"

style submit_result_button_wrong_selected is button:
    xysize (700, 70)
    background Frame(Solid("#ec2727"))
    # hover_background Frame(Solid("#2727ec"))
    # selected_background Frame(Solid("#ec2727"))
    align (0.5, 0.5)

style submit_result_button_wrong_selected_text:
    size 30
    align (0.5, 0.5)
    color "#ffffff"
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

# Quit friendlies button
style quit_friendlies_button is button:
    background Frame(Solid("#cecece"))
    hover_background Frame(Solid("#8c8c8c"))
    align (0.5, 0.5)

style quit_friendlies_button_text:
    size 30
    align (0.5, 0.5)
    color "#000000"

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

# For tutorial. Only "Setups" button is active
screen tutorial_venue_screen_1():
    add "background 2"
    # Buttons to transition to the bracket and setups screens
    textbutton "{color=#000000}Bracket{/color}":
        style "bracket_button"
        align (0.95, 0.825)
        text_align 1.0
        xsize 200

        # action [
        #     Show("bracket_screen"),
        #     Hide("venue_screen")
        # ]
    textbutton "{color=#000000}Setups{/color}":
        style "setups_button"
        align (0.95, 0.95)
        text_align 1.0
        xsize 200

        action [
            Hide("venue_screen"),
            Show("tutorial_setups_screen"), 
            SetVariable("clicked_setups", True)
        ]

# For tutorial. Only "Venue" button is active
screen tutorial_setups_screen():
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
            Show("venue_screen"), 
            SetVariable("clicked_2", True)
        ]
    textbutton "{color=#000000}Bracket{/color}":
        style "bracket_button"
        align (0.95, 0.95)
        text_align 1.0
        xsize 200

        # action [
        #     Show("bracket_screen"),
        #     Hide("setups_screen")
        # ]

    # The setups and players
    $ alignments = [(0.25, 0.1), (0.75, 0.1), (0.25, 0.9), (0.75, 0.9)]
    for i in range(4):
        $ setup = setups[i]
        $ alignment = alignments[i]

        hbox:
            align alignment
            vbox:
                hbox:
                    if i % 2 == 0:
                        frame:
                            style "setup_box"
                            vbox:
                                xsize 150
                                ysize 350
                                text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                                    xalign 0.5
                                    yalign 0.5
                        vbox:
                            xsize 150
                            ysize 350
                            for name, picture in setup.get_player_names_and_pictures():
                                add picture:
                                    xalign 0.5
                                    xysize (150, 150)
                                text "{color=#ffffff}[name]{/color}":
                                    xalign 0.5
                    else:
                        vbox:
                            xsize 150
                            ysize 350
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
                                ysize 350
                                text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                                    xalign 0.5
                                    yalign 0.5
                if not setup.is_free():
                    # quit friendlies button
                    vbox:
                        xsize 300
                        ysize 50
                        xalign 0.5
                        # ypadding 10
                        textbutton "{color=#000000}Ask to hop off{/color}":
                            style "quit_friendlies_button"
                            # action [
                            #     SetVariable("setup_player", setup.get_p1()),
                            #     SetVariable("setup_player_picture", setup.get_p1_picture()[:2]),
                            #     SetVariable("cur_label", store.current_label),
                            #     Hide(),
                            #     Jump("quit_friendlies")
                            # ]



screen setups_screen(show_navigation=True):
    add Solid("#000000")

    if not tutorial_active:
        key "mouseup_1" action NullAction()

    # Buttons to transition to the venue and bracket screens
    if show_navigation:
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
            vbox:
                hbox:
                    if i % 2 == 0:
                        frame:
                            style "setup_box"
                            vbox:
                                xsize 150
                                ysize 375
                                text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                                    xalign 0.5
                                    yalign 0.5
                        vbox:
                            xsize 150
                            ysize 350
                            for name, picture in setup.get_player_names_and_pictures():
                                add picture:
                                    xalign 0.5
                                    xysize (150, 150)
                                text "{color=#ffffff}[name]{/color}":
                                    xalign 0.5
                    else:
                        vbox:
                            xsize 150
                            ysize 350
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
                                ysize 375
                                text "{color=#000000}Setup [setup.get_setup_number()]{/color}":
                                    xalign 0.5
                                    yalign 0.5
                if not setup.is_free():
                    # quit friendlies button
                    vbox:
                        xsize 300
                        ysize 50
                        xalign 0.5
                        # ypadding 10
<<<<<<< HEAD
                        textbutton "{color=#000000}Ask to hop off{/color}":
                            style "quit_friendlies_button"
                            # Old logic; this raised an error. I used an inline if statement to fix this.
                            # $ label_to_jump_to = "quit_friendlies"
                            # if set_in_bracket(setup.get_p1(), setup.get_p2(), bracket):
                            #     $ label_to_jump_to = "quit_bracket"
                            action [
                                SetVariable("setup_player", setup.get_p1()),
                                SetVariable("setup_player_picture", setup.get_p1_picture()[:2]),
                                SetVariable("cur_label", store.current_label),
                                Hide(),
                                Jump("quit_bracket" if set_in_bracket(setup.get_p1(), setup.get_p2(), bracket) else "quit_friendlies")
                            ]

# For tutorial. Only one match will be clickable
screen tutorial_bracket_screen(show_navigation=True):
    # Set buttons should be (315, 130) pixels away from each other
    # For a sample 12-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-34/event/ultimate-singles/brackets/1868263/2751603
    # For a sample 8-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-44/event/ultimate-singles/brackets/1940157/2849091
    # This will be an 8-person bracket screen

    add "bracketTemplate"
    key "mouseup_1" action NullAction()

    # Buttons to transition to the venue and setups screens
    if show_navigation:
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
=======
                        # Case: This set is a bracket set
                        if set_in_bracket(setup.get_p1(), setup.get_p2(), bracket):
                            textbutton "{color=#000000}Ask to hop off{/color}":
                                style "quit_friendlies_button"
                                action [
                                    # Function(setup.clear_setup), # don't clear the setup; it's bracket
                                    SetVariable("setup_player", setup.get_p1()),
                                    SetVariable("setup_player_picture", setup.get_p1_picture()[:2]),
                                    SetVariable("cur_label", store.current_label),
                                    Hide(),
                                    Jump("quit_bracket"),
                                    Return()
                                ]
                        # Friendlies set
                        else:
                            textbutton "{color=#000000}Ask to hop off{/color}":
                                style "quit_friendlies_button"
                                action [
                                    Function(setup.clear_setup),
                                    SetVariable("setup_player", setup.get_p1()),
                                    SetVariable("setup_player_picture", setup.get_p1_picture()[:2]),
                                    SetVariable("cur_label", store.current_label),
                                    Hide(),
                                    Jump("quit_friendlies"),
                                    Return()
                                ]
>>>>>>> bef263060fc1bcfbe67b6e869bfd4396bee608f4
                                

screen bracket_screen(show_navigation=True):
    # Set buttons should be (315, 130) pixels away from each other
    # For a sample 12-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-34/event/ultimate-singles/brackets/1868263/2751603
    # For a sample 8-person bracket, see https://www.start.gg/tournament/ultimate-tech-chase-44/event/ultimate-singles/brackets/1940157/2849091
    # This will be an 8-person bracket screen

    add "bracketTemplate"
    key "mouseup_1" action NullAction()

    # Buttons to transition to the venue and setups screens
    if show_navigation:
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
    
    default fake_submit_text = "Submit Result"
    default fake_submit_style = "submit_result_button_wrong"
    
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
                        SetScreenVariable("fake_submit_text", "Submit Result"),
                        SetScreenVariable("fake_submit_style", "submit_result_button")
                    ]

                else:
                    selected(player_b_active_button == i)
                    action [
                        SetVariable("player_b_active_button", i), 
                        SetVariable("b_selected_gamecount", cur),
                        SetScreenVariable("fake_submit_text", "Submit Result"),
                        SetScreenVariable("fake_submit_style", "submit_result_button")
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
                SetScreenVariable("fake_submit_text", "Submit Result"),
                SetScreenVariable("fake_submit_style", "submit_result_button"),
                SetVariable("matches_in_progress", matches_in_progress + 1),
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
            SetScreenVariable("fake_submit_text", "Submit Result"),
            SetScreenVariable("fake_submit_style", "submit_result_button"),
            Show("bracket_screen"),
            Hide("match_report_screen")
        ]

    # Submit result button
    if find_setup(setups, player_a, player_b) is not None:
        $ winner = determine_winner(player_a, player_b, a_selected_gamecount, b_selected_gamecount)
        $ loser = determine_loser(player_a, player_b, a_selected_gamecount, b_selected_gamecount)
        if expected_result["winner"] == winner and expected_result["loser"] == loser and \
        expected_result["winner_games"] == max(a_selected_gamecount, b_selected_gamecount) and \
        expected_result["loser_games"] == min(a_selected_gamecount, b_selected_gamecount):
            textbutton "Submit Result":
                style "submit_result_button"
                align (0.87, 0.95)
                action [
                    SetVariable("completed_sets", completed_sets + 1), 
                    SetVariable("player_a_active_button", None),
                    SetVariable("player_b_active_button", None),
                    SetVariable("a_selected_gamecount", None),
                    SetVariable("b_selected_gamecount", None),
                    SetScreenVariable("fake_submit_text", "Submit Result"),
                    SetScreenVariable("fake_submit_style", "submit_result_button"),
                    SetVariable("matches_in_progress", matches_in_progress - 1),
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
        else:
            textbutton "[fake_submit_text]":
                if fake_submit_style == "submit_result_button_wrong_selected":
                    style "submit_result_button_wrong_selected"
                else:
                    style "submit_result_button_wrong"
                align (0.87, 0.95)
                action [
                    SetScreenVariable("fake_submit_text", "Wrong Result!"),
                    SetScreenVariable("fake_submit_style", "submit_result_button_wrong_selected")
                ]
    else:
        # Disabled submit results button
        textbutton "Cannot Submit Results":
            style "submit_result_button_disabled"
            align (0.87, 0.95)


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

    $ matches_in_progress = 0
    $ setups = [Setup(1), Setup(2), Setup(3), Setup(4)]

    # # dev skip
    # scene background 2
    # jump match_starting_loop

    # # Script
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

    # Tutorial
    scene black with fade
    e "Welcome to the TO's Chair. Since Reggie is off promoting Mario Kart 14, you're in charge of the bracket."
    e "Here is how a Smash Tournament works:"
    show screen venue_screen with dissolve
    e "From the {b}Venue{/b}, you'll access the core of the tournament."
    e "The buttons on the right allow you to jump between the {b}Bracket{/b} and the {b}Setups{/b}."
    hide screen venue_screen
    show screen tutorial_venue_screen_1
    label wait_for_setups_click:
        e "Click the {b}Setups{/b} button."
        if not clicked_setups:
            jump wait_for_setups_click
    
    hide screen tutorial_venue_screen_1
    e "{b}Assigning Setups{/b}: When players approach you to start a set, you'll need to find them an open setup in the room."

    e "A 'setup' is just a TV and a console ready for a match."
    e "You'll be able to see who is playing at what setup on this screen. During the tournament, you'll need to assign players to open setups so that players can start their sets."
    e "You can start matches from the bracket screen by clicking on a set and then clicking the \"Start Match\" button."
    label wait_for_venue_click_1:
        e "Go back to the venue by clicking the {b}Venue{/b} button."
        if not clicked_2:
            jump wait_for_venue_click_1

    hide screen tutorial_setups_screen
    show screen tutorial_venue_screen_1 with dissolve
    e "{b}Double Elimination{/b}: Most Smash events are 'Double Elimination'. Lose once, and you go to the Losers Bracket. Lose twice, and you're out! In a tournament bracket, it'll look like this."
    show bracketTemplate at truecenter with dissolve
    e "{b}The Bracket{/b}: This is the map of the tournament. This will be shown at appropriate times throoughout the game, and those white boxes will be filled in with players' names."
    e "Players are paired in 'Sets'. Clicking a set button will let you report the outcome."
    hide bracketTemplate with dissolve
    show match_report at truecenter with dissolve
    e "{b}Reporting Scores{/b}: When a set finishes, a player will come to you with their score." 
    e "You'll use this screen to input the games won by each player. Accuracy is key!"
    e "This is also where you'll start sets."
    hide match_report with dissolve
    e "{b}Your Goal{/b}: Keep the tournament moving! If a set is ready to be played, make sure the players find a setup."
    m "Okay... bracket, scores, winners, losers. I think I've got the hang of it."
    $ tutorial_active = False

    scene background 2 with fade
    n "The room is buzzing with energy. It's time to get this bracket moving."
    n "I should check the bracket and see which sets are ready to be played."
    jump match_starting_loop

label quit_friendlies:
    show background 2
    m "Hey, [setup_player.name], quit your friendlies! I have a bracket to run."
    show expression setup_player_picture at left
    with dissolve
    setup_player "My bad; I thought we had time to play some friendlies."
    $ renpy.hide(setup_player_picture) # normal hide statement doesn't work for some reason
    with dissolve
    jump expression cur_label

label quit_bracket:
    show background 2
    m "[setup_player.name], quit your friendlies. I need to keep bracket moving."
    show expression setup_player_picture at left
    with dissolve
    setup_player "This {i}{b}is{/b}{/i} bracket, dingus!"
    $ renpy.hide(setup_player_picture)
    with dissolve
    n "...oops."
    jump expression cur_label

# Show the bracket and have the player choose 4 1st round matches to start
label match_starting_loop:
    if matches_in_progress < 4:
        if matches_in_progress < 3:
            n "I need to get at least [4 - matches_in_progress] more sets running."
        else:
            n "I need to get just one more set running."
        call screen bracket_screen(show_navigation=False)
        # When the player clicks "Start Match", the screen returns here
        jump match_starting_loop
    else:
        n "That looks like a good start. The setups are mostly full now."

label reporting_sets:    
    n "Oh! It looks like someone's finished playing their set."
    show p2 at left onlayer screens with dissolve
    p2 "Hello, I beat [p1.name] 2-1. They got DESTROYED hahaha."
    m "Okay, I'll have to input that into the bracket."

    # 1st set report (winners round 1, SaggyMilkJug)
    # Copyable logic for reporting a set. Use this format when you want the player to input a score after a set finishes
    hide p2 onlayer screens with dissolve
    $ expected_result = {"winner": p2, "loser": p1, "winner_games": 2, "loser_games": 1}
    call screen venue_screen

    # 2nd set report (winners round 1, colorful)
    show p3 at left onlayer screens with dissolve
    p3 "Hey, I beat [p4.name] 2-0."
    m "Sounds good! I'll input that for you now."

    hide p3 onlayer screens with dissolve
    $ expected_result = {"winner": p3, "loser": p4, "winner_games": 2, "loser_games": 0}
    call screen venue_screen

    n "Two sets have just finished, which means that there's currently two empty setups."
    $ setups[0].set_players(PlayerPicture(p1, "p1 cropped"), PlayerPicture(p3, "p3 cropped"))
    n "...or at least, there {i}should{/i} be two empty setups, but it looks like two people are playing friendlies at setup 1."
    jump hop_off_1

label hop_off_1:
    if not (find_setup(setups, p1, p3) is None):
        n "I need to ask [p1.name] and [p3.name] to hop off setup 1 so I can run bracket."
        call screen setups_screen(show_navigation=False)
    n "Now that I have two free setups, I should start calling sets."

# Waiting for losers r1
label losers_r1_starting_loop:
    if matches_in_progress < 4:
        if matches_in_progress < 3:
            n "I need to get at least [4 - matches_in_progress] more sets running."
        else:
            n "I need to get just one more set running."
        call screen bracket_screen(show_navigation=False)
        # When the player clicks "Start Match", the screen returns here
        jump losers_r1_starting_loop
    else:
        n "Good, the setups are full now."
    

label third_set_report:
    # 3rd set report (losers round 1, red dot)
    show screen venue_screen
    show p1 angry at left onlayer screens
    m "Oh, looks like another set has finished. I sure hope he's a normal and reasonable person."
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

    hide screen room_screen
    
    hide p1 happy onlayer screens
    $ expected_result = {"winner": p1, "loser": p4, "winner_games": 2, "loser_games": 0}
    call screen venue_screen

# Nyramyss vs Kitsch (wr1). Nyramyss wins
label nyramyss_kitsch:
    n "Looks like that winners round 1 set has finally wrapped up."
    show p5 at left onlayer screens with dissolve
    p5 "Heyo, I lost 1-2 to [p6.name]."
    m "Understood."
    hide p5 onlayer screens with dissolve
    show screen venue_screen
    $ expected_result = {"winner": p6, "loser": p5, "winner_games": 2, "loser_games": 1}
    call screen venue_screen
    
# Ford vs Pacil (wr1). Pacil wins
label ford_pacil:
    n "This looks like the last winners round 1 match being reported."
    show p7 at left onlayer screens with dissolve
    p7 "I lost 1-2 to [p8.name] because I'm a TERRIBLE player with NO REDEEMING QUALITIES."
    m "Sorry to hear that. I'll report the set."
    hide p7 onlayer screens with dissolve
    show screen venue_screen
    $ expected_result = {"winner": p8, "loser": p7, "winner_games": 2, "loser_games": 1}
    call screen venue_screen

# Prompt player to start another 2 sets (nyramyss vs ford and kitsch vs pacil). p5 vs p8, p6 vs p7
label start_loop_23_57:
    # Note: The numbers here are 3 and 2 instead of 4 and 3 because only THREE sets can be active right now!
    # You'll have to change the numbers depending on how many sets can be called
    if matches_in_progress < 3:
        if matches_in_progress < 2:
            n "I need to get at least [3 - matches_in_progress] more sets running."
        else:
            n "I need to get just one more set running."
        call screen bracket_screen(show_navigation=False)
        # When the player clicks "Start Match", the screen returns here
        jump start_loop_23_57
    else:
        n "All of the setups are in use now."

# Saggy vs colorful wr2. colorful wins 2-0. p2 vs p3. p3 wins 2-0
label report_23:
    hide screen bracket_screen
    show screen venue_screen
    n "The first match of winners round 2 is being reported now."
    show p3 at left onlayer screens with dissolve
    p3 "Hi, I won 2-0 against [p2.name]."
    m "Understood."
    show screen venue_screen
    hide p3 onlayer screens with dissolve
    $ expected_result = {"winner": p3, "loser": p2, "winner_games": 2, "loser_games": 0}
    call screen venue_screen
    
# Nyramyss vs Ford Ford wins 2-0. p7 vs p5 p7 wins 2-0
label report_57:
    hide screen bracket_screen
    show screen venue_screen
    n "A losers round 1 match is being reported."
    show p7 at left onlayer screens with dissolve
    p7 "Hi, I won 2-0 against [p5.name]."
    m "Understood."
    show screen venue_screen
    hide p7 onlayer screens with dissolve
    $ expected_result = {"winner": p7, "loser": p5, "winner_games": 2, "loser_games": 0}
    call screen venue_screen

# Prompt player to start saggy vs ford. p2 vs p7
# label wait_27:
#     show screen venue_screen
#     $ current_match = find_setup(setups, p2, p7)
#     $ matches_started = 0
#     n "Looks like there's some downtime to call another set. Let's see if anything can be started."
#     call screen venue_screen
#     if (matches_started < 2) and current_match is None:
#         jump wait_27
#     else:
#         jump report_68

# Report Kitsch vs Pacil Kitsch wins 2-1. p6 vs p8 p6 wins 2-1.
label report_68:
    n "The final winners round 2 match is being reported now."
    show p6 at left onlayer screens with dissolve
    p6 "Hi, I won 2-1 against [p8.name]."
    m "Understood."
    show screen venue_screen
    hide p6 onlayer screens with dissolve
    $ expected_result = {"winner": p6, "loser": p8, "winner_games": 2, "loser_games": 1}
    call screen venue_screen
    n "Looks like no more bracket matches are currently being played, so I ought to call some sets now."

label start_loop_27_18_36:
    # You'll have to change the numbers depending on how many sets can be called
    if matches_in_progress < 3:
        if matches_in_progress < 2:
            n "I need to get at least [3 - matches_in_progress] more sets running."
        else:
            n "I need to get just one more set running."
        call screen bracket_screen(show_navigation=False)
        # When the player clicks "Start Match", the screen returns here
        jump start_loop_27_18_36
    else:
        n "Bracket should be able to continue now."

# TODO: Report the following sets:
# p8 vs p1 (LR2), p2 vs p7 (LR2), p3 vs p6 (WF)
# After both LR2 sets are completed and reported, call LR3 (winner of LR2-a vs. winner of LR2-b)
# After WF and LR3 are completed and reported, call LF (loser of WF vs. winner of LR3)
# After LF is completed and reported, call Grand Finals (winner of WF vs. winner of LF)
# Report Ford vs Saggy Ford wins 2-0. p7 vs p2, p7 wins 2-0.
label report_27:
    n "That losers round 2 match just finished!"
    show p7 at left onlayer screens with dissolve
    p7 "Hello I won 2-0 against [p2.name]"
    m "Indubitably my good sir"
    show screen venue_screen
    hide p7 onlayer screens with dissolve
    $ expected_result = {"winner": p7, "loser": p2, "winner_games": 2, "loser_games": 0}
    call screen venue_screen

n "There's another set to call. I should start it while everyone else is playing."
label start_loop_18:
    # You'll have to change the numbers depending on how many sets can be called
    if matches_in_progress < 1:
        n "I need to call the next set."
        call screen bracket_screen
        # When the player clicks "Start Match", the screen returns here
        jump start_loop_18

# Report red dot vs Pacil, red dot wins 2-1. p1 vs p8, p1 wins 2-1.
label report_18:
    n "An ashamed individual seems to be approaching me."
    show p8 shame at right onlayer screens with dissolve
    p8 "How embarassing. I shieldbroke him and he mashed out before I could charge a smash attack."
    p8 "I lost 1-2 to [p1.name]"
    m "Geezaloo, that sucks. I'll input your score."
    show screen venue_screen
    hide p8 shame onlayer screens with dissolve
    $ expected_result = {"winner": p1, "loser": p8, "winner_games": 2, "loser_games": 1}
    call screen venue_screen


# Prompt player to start winners finals and losers semifinals. Top 4 so BO5
n "Jimminy crickets! It's top 4 now so all matches from here on out will be best of 5!"
n "Let's start the set that can be played."
label start_loop_36_17:  
    if matches_in_progress == 0:
        n "I need to get at least [2 - matches_in_progress] more sets running."
    elif matches_in_progress == 1:
        n "I need to get just one more set running."
    call screen bracket_screen
    # When the player clicks "Start Match", the screen returns here
    if matches_in_progress < 2:
        jump start_loop_36_17

# Report red dot vs Ford red dot wins 3-0. p1 vs p7 p1 wins 3-0.
label report_17:
    n "Losers semifinals have finished!"
    show p1 happy at left onlayer screens with dissolve
    p1 "I won 3-0 against [p7.name]"
    show p7 at right onlayer screens with dissolve
    p7 "But it was close! 🤓☝️"
    m "Close only counts in horseshoes and handgrenades, sorry."
    show screen venue_screen
    hide p7 onlayer screens with dissolve
    hide p1 onlayer screens with dissolve
    $ expected_result = {"winner": p1, "loser": p7, "winner_games": 3, "loser_games": 0}
    call screen venue_screen

# Waiting...
n "Seems like that winner's set is taking a while. Good thing that everyone here is patient and respectful, though!"
show p1 angry at center onlayer screens with dissolve
p1 "When am I playing my next match??? I've got 8 seasons of Smash n Splash to catch up on tonight."
m "Please be patient, winner's finals is just taking a while."
p1 "All you TO's are the same, wait for this, quit your friendlies that, I've about had it up to HERE with you!!"
m "Well there's nothing I can do. You can always watch their match if you want. You might get some insight into your next opponent."
p1 "Watch a CLOUD DITTO are you kidding me?!?! Might as well watch paint dry and calculus lectures more like!   {nw}"
p1 "Matter of fact, ban both ZSS and Cloud. While you're at it, ban all the sword characters   {nw}"
p1 "{cps=70}Things were better when we had frame perfect links and Akuma as a top tier! Bring back the good old days, I say!! This tyranny cannot go on! ¡Viva la revolución! I hate projectiles I hate Steve I hate Cloud I hate this game gwaaarrrrrrr!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{nw}{/cps}"
n "Wow, I think he's actually lost it. I feel like we should make a documentary out of his life."
m "Hey, well that's just like... your opinion man..."
hide p1 angry onlayer screens
show p1 happy at center onlayer screens
p1 "Fair enough! Glad we could have this discussion."
n "I have no words."
hide p1 happy onlayer screens with dissolve

# Report colorful vs Kitsch, Kitsch wins 3-2. p3 vs p6, p6 wins 3-2
label report_36:
    n "Winner's finals are done!"
    show p6 at left onlayer screens with dissolve
    p6 "I love the Cloud ditto! I won 3-2 against [p3.name]."
    m "Don't go saying that too loud, but congrats!"
    show screen venue_screen
    hide p6 onlayer screens with dissolve
    $ expected_result = {"winner": p6, "loser": p3, "winner_games": 3, "loser_games": 2}
    call screen venue_screen

# Start loser's finals
label start_loop_13:
    n "Time to start another set."
    call screen bracket_screen
    # When the player clicks "Start Match", the screen returns here
    if matches_in_progress < 1:
        jump start_loop_13
    else:
        n "All the sets are started now."

# Report colorful vs red dot, colorful wins 3-1. p3 vs p1, p3 wins 3-1.
label report_31:
    n "Another day, another set completion."
    show p3 at left onlayer screens with dissolve
    p3 "I won against [p1.name] 3-1."
    m "Delightful. I'll report that for you."
    show screen venue_screen
    hide p3 onlayer screens with dissolve
    $ expected_result = {"winner": p3, "loser": p1, "winner_games": 3, "loser_games": 1}
    call screen venue_screen

# Call Grand Finals
label start_loop_gf:
    n "Grand finals time! Let's start it :)"
    call screen bracket_screen
    # When the player clicks "Start Match", the screen returns here
    if matches_in_progress < 1:
        jump start_loop_gf
    else:
        n "All the sets are started now."

# Report grand finals. p3 wins 3-0
label report_gf:
    n "Grands has wrapped up."
    show p3 at left onlayer screens with dissolve
    p3 "I won against [p6.name] 3-0."
    m "Dang, nice. I'll put that in."
    show screen venue_screen
    hide p3 onlayer screens with dissolve
    $ expected_result = {"winner": p3, "loser": p6, "winner_games": 3, "loser_games": 0}
    call screen venue_screen

# Call tf.
n "Since the winner of the loser's bracket, [p3.name], won grand finals, we now have a \"bracket reset\". This means that the same players will play again. Whoever wins this set wins the tournament!"
label start_loop_tf:
    n "Call the grand finals reset."
    call screen bracket_screen
    # When the player clicks "Start Match", the screen returns here
    if matches_in_progress < 1:
        jump start_loop_tf
    else:
        n "All the sets are started now."

# Report tf.
label report_tf:
    n "The last set has finished."
    show p6 at left onlayer screens with dissolve
    p6 "Let's gooooooo I beat [p3.name] 3-2."
    m "Very nice. Congrats on the W! I'll submit that."
    show screen venue_screen
    hide p6 onlayer screens with dissolve
    $ expected_result = {"winner": p6, "loser": p3, "winner_games": 3, "loser_games": 2}
    call screen venue_screen


# Ending
hide screen venue_screen
scene background 2 with fade
    
$ champion = tf[0].winner.name
n "And that's it! [champion] is our tournament champion!" 

m "I... I actually did it. I ran the whole bracket without Reggie."

show reggie at right with moveinright
play sound "audio/heheh.mp3"
r "I'm back! And I brought Shaq!"
n "Thanks for playing!"
