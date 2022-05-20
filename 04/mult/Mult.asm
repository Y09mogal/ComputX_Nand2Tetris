// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//This is a Hack assembly language program to multiply the numbers in registers
//R0 and R1

@R2
M=0

(LOOP)
    @R1
    D = M
    @INFINITE_LOOP
    D;JLE


    @R0
    D = M
    @R2
    M = D + M

    @R1
    M = M - 1
    D = M
    @LOOP
    0;JMP

(INFINITE_LOOP)
    @INFINITE_LOOP
    0;JMP 