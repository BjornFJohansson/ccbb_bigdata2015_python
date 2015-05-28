## SJS 
## This file contains solutions for the Python exercises of Day 2


##################### Working with Dictionaries ##################### 

## 1. Define this dictionary in Python: molecules = {"DNA":"nucleotides", "protein":"amino acids", "hair":"keratin"},and perform the following tasks:
molecules = {"DNA":"nucleotides", "protein":"amino acids", "hair":"keratin"}

## (a) Create two lists called molecules_keys and molecules_values, comprised of the keys and values in molecules, respectively. Use dictionary methods for this task.
molecules_keys = molecules.keys()
molecules_values = molecules.values()

## (b) Add the key:value pair "ribosomes":"RNA" to the molecules dictionary. Print the dictionary to confirm.
molecules["ribosomes"] = "RNA"
print molecules

## (c) Add yet another key:value pair, "ribosomes":"rRNA", to the molecules dictionary, and print out the new dictionary. Understand why the result contains the key:value pairs shown.
molecules["ribosomes"] = "rRNA" # the key:value pair "ribosomes":"RNA" is now gone and has been replaced!



##################### If/elif/else Exercises ##################### 

## 1. In Texas, you can be a member of the elite "top 1%" if you make at least $423,000 per year. Alternatively, in Hawaii, you can be a member once you start making at least $279,000 per year! Finally, if you live in New York, you need to earn at least $506,000 a year to make the cut. Andrew is CEO of Big Money Company, and he earns $425,000 per year, and Stacey is CEO of Gigantic Money Company with an annual salary of $700,000. Use if-statements to determine, and print, whether Andrew and Stacey would be considered top 1%-ers in Texas, Hawaii, and New York.

texas = 423000
hawaii = 279000
newyork = 506000

andrew = 425000
stacey = 700000

# Evaluate Stacey across states
if stacey >= texas:
    print "Stacey is a 1%er in Texas"
if stacey >= hawaii:
    print "Stacey is a 1%er in Hawaii"
if stacey >= newyork:
    print "Stacey is a 1%er in New York"
    
    
    
    
    











