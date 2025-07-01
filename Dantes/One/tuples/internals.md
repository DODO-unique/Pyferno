# Tuple Internals

Tuples are faster than lists- not crazy fast, but faster in general. 
They are faster in iteration and creation, mainly because python has to deal with lists dynamically since they are mutable

Interestingly, tuples are also smaller than lists. They are stored as fixed-length C arrays.

That said, tuples don't have hashtables like sets or dictionaries
What are hashtables? [read this](C:\Users\victo\codes_real\making\python\Dantes\Zero\hashtables.md)