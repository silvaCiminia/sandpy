# sand.py

Some small snippets of code to express arithmetic expressions within the square abelian sandpile (Bak–Tang–Wiesenfeld) model.

## Examples:

Set the dimensions of the group with which you would like to experiment (must be a square number):  
`Pile.set_dims(9)`  

The max member (all 3s) and the special identity member can be calculated as follows:  
`max_pile = Pile.max_pile()`
`id_pile = Pile.zero()`

For our 3x3 group, these are respectively:  

    3 3 3  
    3 3 3  
    3 3 3  

and  

    2 1 2
    1 0 1
    2 1 2


If you are using grids larger than 4x4, you will have to define the identity element for yourself. This module will not derive sandpile identities.

Piles can also be defined using bidimensional arrays:  

    id_pile2 = Pile([[2, 1, 2],
                     [1, 0, 1],
                     [2, 1, 2]])
The above pile is equivalent to the identity shown earlier.

The sums of these piles can be calculated by:  
`new_pile = max_pile.add(id_pile)`

and printed easily by:  
`print(new_pile)`

Enjoy the sandbox!
