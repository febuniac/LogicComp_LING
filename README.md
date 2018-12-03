# LogicComp_LING

#  SLCL 
######Single Letter Computer Language

#### About
Sometimes typing can be exaustive, even more when typing repetitive words. In programming languages, reserved words become really repetitive at a certain point  and become an issue. SLCL purpose is to substitute reserved words for reserved letters, making coding easier and faster. No more typing                             
                            `if`  -->    `I`
                            `else`-->   `E` 
                            `for`-->    `F`
                            `while` --> `W`
                            `print`-->  `P` 
                            `break`-->  `B`
                            `function`--> `f`
                            `return`--> `R`
                            `and`-->    `A`
                            `or` -->    `O`
                            `not`-->    `N`
, now you can simply write them as one single capital letter (functions are not capital) .

Use `SLCL` and start coding faster!
### Installation requirements ###

- Python3
```
https://www.python.org/downloads/
```
- ply
```
https://pypi.org/project/ply/
```
- py2exe
```
https://pypi.org/project/py2exe/
```




## EBNF
```
program
: :statement_list+
;

statement_list 
: :statement
| statement_list statement
;

statement
: :variable
| expression
| function_declaration
| function_call_stat
| if_statement
| break
| print
| compounds
| for_loop
| while_loop
| return
;

expression
: :function_call_exp
| arithmetics
| booleans,
| unary
| paren_expression
| attribution
| primitive
;

function_declaration
: :'f', variable, '(', arguments, ')', '{', statement_list, '}'
| 'f', variable, '{', statement_list,'}'
;

function_call_stat
: variable, '(', arguments,')',';'
;


if_statement
: :'I',':', expression,'{' statement_list '}'
| 'I',':', expression, '{', statement_list, '}', 'E',':', '{', statement_list, '}',':'
| 'I',':',expression'{', statement_list, '}', 'E',':', if_statement 
;

break
: :'B', ';'
;

print
: :'P',':','(',arguments,')',';'
;


compounds
: :variable, '+=', expression, ';'
| variable, '-=', expression, ';'
| variable, '*=', expression, ';'
;


for_loop
: :'F',':',expression, '{', statement_list, '}'
;

while_loop
: :'W',':', '{', statement_list, '}'
;

return
: :'R' expression ';'
;

function_call_exp
: :variable, '(', arguments,')'
;

arithmetics
: :expression, '+', expression 
| expression, '-', expression 
| expression, '*', expression 
| expression, '/', expression 
| expression, '**', expression 
| expression, '%', expression 
;  

bools
: :expression, '|', expression
| expression, '&', expression
| expression, '^',  expression
| expression, '~',  expression
;

unary
: :'+', expression
| '-', expression
| '~', expression
| 'N', expression
;

paren_expression
: :'(', expression, ')'
;  

attribution
: variable, '=', expression, ';'
;

primitive 
: :relats
| number
| string
| simple_bool
;

relats
: :expression, '>',  expression
| expression, '<',  expression
| expression, '>=', expression
| expression, '<=', expression
| expression, '==', expression
| expression, '!=', expression
;



variable
: :string, {string, int, '_'}
;

number
: :float
;

string
: : "A" | "B" | "C" | "D" | "E" | "F" | "G"
| "H" | "I" | "J" | "K" | "L" | "M" | "N"
| "O" | "P" | "Q" | "R" | "S" | "T" | "U"
| "V" | "W" | "X" | "Y" | "Z" 
| "a" | "b"| "c" | "d" | "e" | "f" | "g" 
| "h" | "i"| "j" | "k" | "l" | "m" | "n" 
| "o" | "p"| "q" | "r" | "s" | "t" | "u" 
| "v" | "w"| "x" | "y" | "z" ;
;

simple_bool
: :'Tr'
| 'Fa'
;
float
: :int, ['.', int]
;

int
: :"0"|"1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
;
```

### Features ###
* Variables
* Functions
* Loops (for, while)
* Statements (If,else, else if) 
* Break
* Compound operators
* Booleans, Relational, Arithmetic, Unary


### Data types ###
* Integer
* Float
* String
* Boolean


### Language description ###

#### Disclaimer and Proper Credits
This projects was based in: [Mamba programming language](https://github.com/maldoinc/mamba) made by [@maldoinc](https://github.com/maldoinc). 

#### Variables ####
 Dynamically typed immediately declared upon use
`number = 42;` 

### Operators ###

#### 
relational: `and` `or` `not` `>` `>=` `<` `<=` `==` `!=`

arithmetic: `+` `-` `*` `/` `**`

booleans binary: `~` `^` `|` `&` 

simple booleans: `True (Tr)` `False (Fa)`  

compound: `+=` `-=` `*=`  

####



#### Functions ####

functions are declared via the following grammar

```
f func_name( arguments, ){
< statements >
}

Example:

f ten(){
R 10;
}
```
return value is specified with the `R` keyword.

### Loops ###

SLCL supports `for` and `while` loops.

#####For syntax
```

F :  <expression>  {
< statements >
}
```

#####While syntax
```
W : < expression > {
< statements >
}
```

All loops can be prematurely exited via the `break`(`B`keywork ) statement when necessary.

#### Statements ####


#####If Syntax
```
I :  < expression > {
< statements >
}
```
#####If  Else Syntax
```
I :  < expression > {
< statements >
}
E : < expression > {
< statements >
}
```
##### Else If Syntax
```
I :  < expression > {
< statements >
}
E : < expression > {
< statements >
}
I :  < expression > {
< statements >
}
```

### Printing ###

Printing is supported via the `P` keyword which accepts a list of values to print. 

##### Syntax
```
P : (<arguments>);
```

### Standard library ###
Extracted from [Mamba programming language](https://github.com/maldoinc/mamba).

Libraries are added to the Symbol Table.

#### 1. Constants ###

* `e`
* `pi`

#### 2. Globals

* `argv`

#### 3. Functions

* `ask(prompt)` *shows the prompt and returns the result as a string*
* `int(x [, base])` 
* `float(x)`
* `round(value, precision)`
* `abs(x)`
* `log(x)`
* `rand`
* `randrange(lo, hi)`
* `sin(x)`
* `cos(x)`
* `tan(x)`
* `atan(x)`
* `str(x)`
* `substr(str, start, length)`
* `len(str)`
* `pos(substr, str)`
* `upper(str)`
* `lower(str)`
* `replace(str, find, replace)`
* `format(string [, ... ])`
* `chr(x)`
* `ord(x)`
* `time`
* `file(filename, mode)` *opens a file and returns the handle*
* `file_close(handle)`
* `file_write(handle, data)`
* `file_read(handle [,size])`
* `file_seek(handle, position)`
* `file_pos(handle)`
* `file_exists(filename)`



#### RESOURCES
* `https://github.com/maldoinc/mamba` *inspired by*
* `https://www.dabeaz.com/ply/ply.html` PLY
* `https://github.com/dabeaz/ply` PLY

