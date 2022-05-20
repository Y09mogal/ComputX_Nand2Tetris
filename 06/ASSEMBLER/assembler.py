import sys
import parse
import code
import symbolTable
import os

if __name__ == "__main__":

    #This block imports the filepath used to open Prog.asm to save the Prog.hack file
    base_Path = os.path.splitext(parse.root.filename)[0] 
    f = open((base_Path + ".hack"),"w+")

    ROMaddress = 0

    #This passes all labels ie (Xxx) and thier ROM addresses to the symbol table
    while parse.hasMoreCommands(): 
        parse.advance()
        if parse.commandType() == "A_COMMAND":
            ROMaddress += 1
        elif parse.commandType() == "C_COMMAND":
            ROMaddress += 1
        elif parse.commandType() == "L_COMMAND":
             symbolTable.addEntry(parse.symbol(), ROMaddress)

    #The current command needs to be set to the start so the instrunction can be parsed and translated
    parse.current_cmd_Cntr = 0    

    RAMaddress = 16
    while parse.hasMoreCommands():
        parse.advance()
        
        #If A_COMMAND is then translated instruction, it is a 0 followed by symbol address (15 bits)
        if parse.commandType() == "A_COMMAND": 
            if parse.symbol().isdigit():
                # We convert to binary if the A_COMMAND does not use a symbol.
                f.write("0%s\n" %(format(int(parse.symbol()), '015b'))) 
            else:
                if symbolTable.contains(parse.symbol()):
                    # Use symbol's associated value ff symbol exists in the symbol table.
                    f.write("0%s\n" %(format(int(symbolTable.getAddress(parse.symbol())), '015b'))) 
                else:
                    symbolTable.addEntry((parse.symbol()), str(RAMaddress))
                    # Add the symbol to the symbol table if the symbol does not exist.
                    f.write("0%s\n" %(format(int(symbolTable.getAddress(parse.symbol())), '015b'))) 
                    RAMaddress += 1

        elif parse.commandType() == "C_COMMAND":
            a = "0"
            if "M" in parse.comp():
                a = "1"
            f.write("111%s%s%s%s\n" %(      #C_COMMAND is as follows:   111
                a,                          # a       is 0 if comp using A, 1 if using M
                code.comp(parse.comp()),    # c1..c6  Comp bits
                code.dest(parse.dest()),    # d1..d3  Dest bits
                code.jump(parse.jump())     # j1..j3  Jump bits
                ))                          # Put together is: 1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3
    f.close
