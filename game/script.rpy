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


style game_count_button is button:
    idle_background Frame(Solid("#dbdbdb"), corner_radius=50)
    hover_background Frame(Solid("#dbdbdb"), corner_radius=50)


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


# Screen for reporting the matches
screen match_report_screen(player_a, player_b):
    add "match_report":
        align(0.5, 0.5)

    text player_a:
        color "#000"
        align(0.35, 0.195)

    text player_b:
        color "#000"
        align(0.67, 0.195)
		
		

# The game starts here.

label start:
    scene black
    m "Quit your friendlies!"

    call screen room_screen

    
    return
