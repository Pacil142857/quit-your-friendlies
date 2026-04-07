# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Me")

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
    xysize (215, 50)


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



# Screens
screen room_screen():
    add "background 2"
    
    # Go to laptop view
    textbutton "Laptop":
        # Placement and styling
        align(0.7, 0.8)
        style "blue_button"
        
        # Logic
        action [
            Show("laptop_screen", transition=easeinbottom),
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

screen bracket_screen():
    $ sets = [0, 1, 2, 3, 4, 5]
    for i in sets:
        textbutton "{color=#000000}RoyalXTitan{/color}":
            style "set_button"
            pos (281 + (228 * i), 108)


# Screen for reporting the matches. Pass the players as arguments
screen match_report_screen(player_a, player_b):
    add "match_report":
        align(0.5, 0.5)

    text player_a:
        color "#000"
        align(0.33, 0.175)

    text player_b:
        color "#000"
        align(0.69, 0.175)

    text player_a:
        color "#000"
        align (0.15, 0.52)

    text player_b:
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
                    action [
                        SetVariable("player_a_active_button", i), 
                        SetVariable("a_selected_gamecount", cur)
                    ]
                    selected(player_a_active_button == i) # Mark this button as selected if active_button == i

                else:
                    action [
                        SetVariable("player_b_active_button", i), 
                        SetVariable("b_selected_gamecount", cur)
                    ]
                    selected(player_b_active_button == i)

    # Submit result button
    textbutton "Submit Result":
        style "submit_result_button"
        align(0.87, 0.95)
        action [
            Show("post_match_report_screen", selected_agmc=a_selected_gamecount, selected_bgmc=b_selected_gamecount, 
                                            agmc=a_correct_gamecount, bgmc=b_correct_gamecount), 
            Hide("match_report_screen")
        ]


# Shown after the player submits the game score
# selected_agmc = The user-selected gamecount for player_a, selected_bgmc = The user_selected gamecount for player_b
# agmc = The correct gamecount for player_a, bgmc = The correct gamecount for player_b
screen post_match_report_screen(selected_agmc, selected_bgmc, agmc, bgmc):
    add "background 4":
        align(0.5, 0.5)

    # TODO: Add more robus success and failure states
    
    # Success!
    if selected_agmc == agmc and selected_bgmc == bgmc:
        text "Success!":
            align (0.5, 0.5)
            size 100
            color "#00ff00"

    # Failure
    else:
        text "Failure":
            align (0.5, 0.5)
            size 100
            color "#ff0000"



# The game starts here.

label start:

    # Previous code
    # scene black
    # m "Quit your friendlies!"

    # call screen room_screen

    # TEST for the match report screen.
    # player_a == "blah", player_b == "blahblah". 
    # If the user correctly enters the gamescore as 3-0, "Success!" will show, 
    # Otherwise, "Failure" will show.
    $ a_correct_gamecount = 3
    $ b_correct_gamecount = 0
    call screen match_report_screen("blah", "blahblah")
    
    

    
    return
