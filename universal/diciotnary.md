
1. Segmentation Fault: When you are trying to access a restricted memory address, eg. trying to modify a tuple element in PyTupleObject would give you a sefgault.
2. RefCount or Reference Count: How many times is a occupied address being referenced/assigned. if this is 0, python deletes the value from memory (exception: interned, cached values)
3. 