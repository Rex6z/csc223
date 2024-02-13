* Linear collection of data elements called nodes
* Can be used to impliment other data structures
* Sequence of nodes in which each node contains at least one data fiels and a pointer to the next node
* Made up of two fields, data (the data being stored) and next (the address of the next piece of data)
* Ends on NULL or -1 value for next
* Do not need to be consecutive memory locations
* Does not allow for random access of data, needs to be acccess sequentialy
* Can add more values later
* START marks the start and AVAIL marks open spaces
* 

Impliment
struct node{
    int data;
    struct node *next;
}