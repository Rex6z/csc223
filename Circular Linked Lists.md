# Circular Linked Lists
* Works like a linked list but the last node conects back to the first one
* Can start traversing from anywhere, either forwards or backwards, until it reaches the node where the traversing started
    * go until you find the NEXT value that directs to the first node to go backwards
* No NULL value for NEXT
* Can have multiple linked lists maintained in the same program that can be referanced independently from any point within the list you want