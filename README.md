#Compiler for a simple language for the CIIC4082 project 1 CPU.

To use this, write your desired program in input.txt, then run. The output will be available in output.txt, from where you can load it into your RAM in logisim.  
You may also choose to run it from the command line by passing in the relative path to the input file, followed by the relative path to the output file (it will create one if it does not exist).

You may declare variables by writing a line:
```var [name] [initial value]```

Then reference them later by writing the name again. This **only** works for instructions that use an address argument, i.e. `load`, `store`, `out`, and `jump`.
Therefore these variables are mostly useful so you don't have to remember where a particular value is stored. They do not work as a substitute for registers.

The instructions are the following
-

- `load [register] [address]` will load the value at location `[address]` to `[register]`.  
- `store [register] [address]` will store the value in `[register]` to `[address]`.
- `add [register1] [register2]` will calculate `*[register1] + *[register2]` and store it to `[register1]`.
- `neg [register]` will set the register to its 2's complement.
- `shiftr [register]` will set the register's value to itself shifted 1 bit right.
- `out [register] [address]` will set the IO port `[address]` to the value of `[register]`.
- `jump [address]` will set the PC back to the instruction at `[address]`.

Example program
-
Let's ask our CPU what 9 + 10 is!
```
var x 9  
var y 10 
load 1 x 
load 2 y 
add 2 1  
out 2 0  
```
With comments:
```
var x 9   # RAM15 = 9
var y 10  # RAM14 = 10
load 1 x  # R1 <- RAM15
load 2 y  # R2 <- RAM14
add 2 1   # R2 <- *R2 + *R1
out 2 0   # IO0 <- *R2
```
We expect that the hexadecimal display will hold the value 13, which translates to 19 in decimal.  

Notes
-

Your program will be compiled with all the variables at the end of the 16 byte memory. This means if you want to use the `jump` instruction, only consider instructions, not variable initializations.  
Another minor detail to keep in mind, you may only have 16 instructions and variables in your program, as the memory is 16x8. If you do more than this, variables will start overriding instructions, or the compiler will crash.