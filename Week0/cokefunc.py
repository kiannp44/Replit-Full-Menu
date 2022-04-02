import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RED_COLOR = u"\u001b[34m"
TRAIN_COLOR = u"\u001b[34m"

# print a train moving across screen
def label_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    os = " " * position
    print(RED_COLOR)
    print(os + "      z$$$$$.$$")
    print(os + "    $$$$$$$$$$$")
    print(os + "    $$$$$$**$$$$             eeeeer")
    print(os + "   $$$$$%   '$$$             $$$$$F")
    print(os + "  4$$$$P     *$$             *$$$$F")
    print(os + "  $$$$$      '$$    .ee.      ^$$$F            ..e.")
    print(os + "  $$$$$       $$  .$$$$$$      $$$F  $$$$$$   $$$$$$c")
    print(os + " 4$$$$F           4$$$""$$$$    $$$F  *$$$$*   $$$P$$$$")
    print(os + " 4$$$$F         .$$$F  ^$$$b   $$$F  J$$$   $$$$  ^$$$.")
    print(os + " 4$$$$F         d$$$    $$$$   $$$F J$$P   .$$$F   $$$$")
    print(os + " 4$$$$F         $$$$    3$$$F  $$$FJ$$P    4$$$;   $$$$")
    print(os + " 4$$$$F        4$$$$    4$$$$  $$$$$$$r    $$$$$$$$$$$$")
    print(os + " 4$$$$$        4$$$$    4$$$$  $$$$$$$$    $$$$********")
    print(os + " $$$$$        4$$$$     4$$$F  $$$F4$$$b   $$$r")
    print(os + "  3$$$$F       d$$$$    $$$$;  $$$F *$$$F  4$$$L     .")
    print(os + "   $$$$$.     d$$$$$.   $$$$   $$$F  $$$$.  $$$$    z$P")
    print(os + "    $$$$$e..d$$$$$$$b  4$$$;  J$$$L  '$$$$  '$$$b..d$$")
    print(os + "     *$$$$$$$$$  ^$$$be$$$;  $$$$$$$  3$$$$F ;$$$$$$$")
    print(os + "      ^*$$$$P;     *$$$$*    $$$$$$$   $$$$F  ^*$$$;") 

# Pattern function for the non-animated(static) pattern
def staticanime():
  label_print(0)

# Pattern function for drawing the animated pattern
def cokefunc():

    # Animation Variables
    start = 0  # Start with no offset
    distance = 40  # Number of loops
    step = 1  # Step amount

    # Loop to move the train to the right
    for position in range(start, distance, step):
        label_print(position)  
        time.sleep(.1)


