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
            Show("laptop_screen", transition=dissolve),
            Hide("room_screen")
        ]



screen laptop_screen():
    add "laptop_(transparent)"

    # Go to venue view
    textbutton "Venue":
        # Placement and styling
        align(0.7, 0.8)
        style "blue_button"

        # Logic
        action [
            Show("room_screen", transition=dissolve), 
            Hide("laptop_screen")
        ]


# The game starts here.

label start:
    scene background 2 with dissolve
    m "Quit your friendlies!"

    call screen room_screen

    
    return
