// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@24576
D = A
@R1                    //Maximum screen value
M = D                  // Sets R1 to 16416, the last byte that the screen uses


(RESET)
    @SCREEN
    D = A - 1
    @R0
    M = D 

    @KEYBOARD_TEST 
    0;JMP

(RESTART)
    @0
    D = !A             //Set D to all 1 bits i.e. Black screen
    @R0                //Technically not necessary since R0 and @0 are the same but I like to be explicit
    A = M
    M = D

(KEYBOARD_TEST)
    @R0
    M = M + 1          //Increment the screen pointer

//Check to see if M > maximum screen byte and if so reset to @screen 

    @R1
    D = M
    @R0
    D = D - M
    @RESET 
    D;JLE
    
    @R0
    A = M
    M = 0              //Set current screen pointer value to 0

    @KBD
    D=M
    @RESTART
    D;JNE
    
    @KEYBOARD_TEST
    0;JMP

   