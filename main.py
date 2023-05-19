RandomNum = 0

def on_gesture_shake():
    global RandomNum
    RandomNum = randint(1, 3)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
    """)
    basic.show_leds("""
        . # # . .
                # # # # .
                # # # # #
                . # # # #
                . . # # .
    """)
    basic.show_string("TED!")
    if RandomNum == 1:
        basic.show_leds("""
                # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
            """)
    elif RandomNum == 2:
        basic.show_leds("""
                # . . . #
                        . # . # .
                        . . # . .
                        # # . # #
                        # # . # #
            """)
    else:
        basic.show_leds("""
                . # # . .
                        # # # # .
                        # # # # #
                        . # # # #
                        . . # # .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
