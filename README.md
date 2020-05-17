# Unate Recursive Complement (URC)

* As with the previous **tautology-checking** algorithm, the complementation algorithm uses a recursive “divide-and-conquer” approach.</br> 
*   Given an initial cover F of a Boolean function f, the algorithm divides the cover
into smaller pieces until termination conditions are met. Results are then returned and reassembled into a
final solution.</br> 
* For the complementation algorithm, the result is the complement of the initial cover.
An important aspect the complementation algorithm, as in tautology checking, is that properties of unate
functions are exploited to simplify or terminate the recursion.</br>
*  Unate functions have special properties which
make them especially useful. While most logic functions are not unate, the recursive decomposition often
leads to cofactors which are unate.</br>
* The name for this general approach is the unate recursive paradigm.</br>
* The **unate recursive paradigm** consists of exploiting special properties of unate functions, while performing
recursive decomposition.


## Dependencies

* Python 3.x


## Installing

>On macOS/Linux/Windows you may follow [this link](https://www.python.org/downloads/ "python install")

## Procedure
* Check if you have ``git`` installed on your system  using the follow command in your ``Command Prompt``:
```
git --version
```
  
 >Tip: You may follow [this link](https://git-scm.com/downloads "git download" ) 
    
* Clone this repository using the following command in your preferred directory:

```
git clone 
```
* Run `UnateRecursiveComplement.py` file in ``command prompt``  in the same directory

```
    python UnateRecursiveComplement.py
```
or
```
    python3 UnateRecursiveComplement.py
```

## Format of input and output files 

### Input file:

> Input files use a simple text file format. The same file format applies on ouput files, too. The file format uses the above skeleton:

1. First line of the file is a number *(positive integer)* declaring how many variables are in the equation. Variables numbering starts with index 1.
2. Second line of the file is a number *(positive integer)* declaring how many cubes are in this cube list.
3. Each of the subsequent lines of the file describes one cube, that means one line for every cude for all cubes defined at second line of the input file. Each line should follow the above format
  1. The first number on the line says how many variables are not don’t cares in this cube. 
  2. The next numbers use the next form. If this number of variables is, *e.g., 5*, then the next 5 numbers on the line specify the true or complemented form of each variable in this cube. A simple convention is used: if variable xk appears in true form, then put integer "k" on the line else put integer "-k" on the line. The file will always order these variables in increasing index order.
  
#### Example of input file
Suppose we have this function as input:

    F(x1,x2,x3,x4,x5,x6) =x2x4x5’ + x2’x4’x6 + x1x2x3’x4’ + x5x6

Then the input file format would look like this:

    6
    4
    3 2 4 -5
    3 -2 -4 6
    4 1 2 -3 -4
    2 5 6

### Output file:
> Same as input file


## Note
* Input files are added [here](https://github.com/siddhipandare/Unate_Recursive_Complement/tree/master/Inputs "inputs")
*  Output files are added [here](https://github.com/siddhipandare/Unate_Recursive_Complement/tree/master/Outputs "outputs")


## Authors

* [**Siddhi Pandare**](https://github.com/siddhipandare), Veermata Jijabai Technological Institute.




