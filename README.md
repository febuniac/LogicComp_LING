# LogicComp_LING

## SLCL - Single Letter Computer Language
### Installation requirements ###

* Python3
* ply
* py2exe

### Installation requirements ###

* Python3
* ply
* py2exe

## EBNF
program
: statement_list+
;

statement_list 
: statement
| statement_list statement
;

statement
: variable
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
: function_call_exp
| arithmetics
| booleans,
| unary
| paren_expression
| attribution
| primitive
;

function_declaration
: 'f', variable, '(', arguments, ')', '{', statement_list, '}'
| 'f', variable, '{', statement_list,'}'
;

function_call_stat
:variable, '(', arguments,')',';'
;


if_statement
: 'I',':', expression,'{' statement_list '}'
| 'I',':', expression, '{', statement_list, '}', 'E',':', '{', statement_list, '}',':'
| 'I',':',expression'{', statement_list, '}', 'E',':', if_statement 
;

break
: 'B', ';'
;

print
: 'P',':','(',arguments,')',';'
;


compounds
: variable, '+=', expression, ';'
| variable, '-=', expression, ';'
| variable, '*=', expression, ';'
;


for_loop
:'F',':',expression, '{', statement_list, '}'
;

while_loop
:'W',':', '{', statement_list, '}'
;

return
: 'R' expression ';'
;

function_call_exp
:variable, '(', arguments,')'
;

arithmetics
: expression, '+', expression 
| expression, '-', expression 
| expression, '*', expression 
| expression, '/', expression 
| expression, '**', expression 
| expression, '%', expression 
;  

bools
: expression, '|', expression
| expression, '&', expression
| expression, '^',  expression
| expression, '~',  expression
;

unary
: '+', expression
| '-', expression
| '~', expression
| 'N', expression
(* | number
| '(',expression,')'
| variable *)
;

paren_expression
: '(', expression, ')'
;  

attribution
: variable, '=', expression, ';'
;

primitive 
: relats
| number
| string
| simple_bool
;

relats
: expression, '>',  expression
| expression, '<',  expression
| expression, '>=', expression
| expression, '<=', expression
| expression, '==', expression
| expression, '!=', expression
;



variable
: STRING, {STRING, INT, '_'}
;

number
: FLOAT
;

string
:  "A" | "B" | "C" | "D" | "E" | "F" | "G"
| "H" | "I" | "J" | "K" | "L" | "M" | "N"
| "O" | "P" | "Q" | "R" | "S" | "T" | "U"
| "V" | "W" | "X" | "Y" | "Z" 
| "a" | "b"| "c" | "d" | "e" | "f" | "g" 
| "h" | "i"| "j" | "k" | "l" | "m" | "n" 
| "o" | "p"| "q" | "r" | "s" | "t" | "u" 
| "v" | "w"| "x" | "y" | "z" ;
;

simple_bool
: 'Tr'
| 'Fa'
;
float
: INT, ['.', INT]
;

int
: "0"|"1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
;

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

#### Variables ####
 Dynamically typed immediately declared upon use
 #### `number = 42;` ####

### Operators ###

#### 
logic: `and` `or` `not` `in` `not in` `>` `>=` `<` `<=` `==` `!=`

arithmetic: `+` `-` `*` `/` `**`

binary: `~` `^` `|` `&` 

compound: `+=` `-=` `*=`  

####

#### Functions ####

functions are declared via the following grammar

fn func_name( [<arguments>,] ){
< statements >
}

fn random(){
ret 4;
}

return value is specified with the `ret` keyword which, as expected, immediately halts function execution upon being called. Functions can have their private functions which are inaccessible to the outer scope.

#### Flow control ####

Mamba supports `if` statements for flow control via the following syntax

if < expression > {
< statements >
}

nb: Brackets are mandatory, while parenthesis on the expression are optional


### Loops ###

Mamba supports two kind of loops, `for` and `while`

** for syntax **

for variable in sequence {
< statements >
}

nb: sequence accepts arrays and strings

for variable in low -> high {
< statements >
}

down to loops are constructed as

for variable in high <- low {
< statements >
}

nb: loop indexes are inclusive

** while syntax **

while < expression > {
< statements >
}

there is also the alternative `for` syntax

for {
< statements >
}

which acts as an infinite loop (which internally is expressed as a `while true {}` statement)

All loops can be prematurely exited via the `exit` statement when necessary


### Arrays ###

Arrays have dynamic length and can be declared via the  `[ ... ]` expression


### Printing ###

Printing is supported via the `say` keyword which accepts a list of values to print. Note that `say` doesn't
add spaces nor newlines after printing.


### Standard library ###

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
* `array_insert(array, index, value)`
* `array_pop(array)` *returns removed value and modifies array*
* `array_push(array, value)`
* `array_remove(array, index)` *returns removed value and modifies array*
* `array_reverse(array)` *reverses array without returning it*
* `array_sort(array)` *sorts the array without returning it*
* `file(filename, mode)` *opens a file and returns the handle*
* `file_close(handle)`
* `file_write(handle, data)`
* `file_read(handle [,size])`
* `file_seek(handle, position)`
* `file_pos(handle)`
* `file_exists(filename)`
