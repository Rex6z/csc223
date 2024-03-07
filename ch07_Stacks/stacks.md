### What are stacks
* Last element added is the first one removed
    * Last-In-First-Out (LIFO) data structure
* When a function is called, the inner most function must finish before the next layer can finish, all the way until the original function is finished

### How do stacks work
* 2 variables
    * MAX
        * Maximum number of elements a stack can hold
    * TOP
        * The address of the topmost element of the stack
        * TOP = NULL means stack is empty
        * TOP = MAX-1 means stack is full