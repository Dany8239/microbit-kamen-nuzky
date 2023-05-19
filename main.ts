let RandomNum = 0
input.onGesture(Gesture.Shake, function () {
    RandomNum = randint(1, 3)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(500)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
    basic.pause(500)
    basic.showLeds(`
        . # # . .
        # # # # .
        # # # # #
        . # # # #
        . . # # .
        `)
    basic.pause(500)
    basic.showString("TED!")
    if (RandomNum == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (RandomNum == 2) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    } else {
        basic.showLeds(`
            . # # . .
            # # # # .
            # # # # #
            . # # # #
            . . # # .
            `)
    }
})
basic.forever(function () {
	
})
