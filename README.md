# grammar-engineering
The program is being run from main.py.
So, to run, do
python main.py

This will run valid sentences first, then the invalid sentences.
In each case, it is possible to print just the number of trees generated for a siungle sentence, 
or all the generated trees, or only trees for the cases where more than one tree has been generated.

There are four flags available:
--toPrintValid - prints all the trees for every sentence from the valid set
--toPrintRepetitionsValid - prints all the trees for cases where more than one tree has been generated for a sentence from the valid set
--toPrintInvalid - prints all the trees for every sentence from the invalid set
--toPrintRepetitionsInvalid - prints all the trees for cases where more than one tree has been generated for a sentence from the invalid set

To use these, simply add a construct <flag>=True to the command line, for example,
python main.py --toPrintRepetitionsValid=True 

Flags are False by default.



