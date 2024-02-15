#include <stdio.h>
#include <stdlib.h>
#include "list.h"

Node *make_node(int data)
{
    Node *new = malloc(sizeof(Node));
    if (new == NULL)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->val = data;
    new->next = NULL;

    return new;
}

void insert_in_front(Node **list, Node **newnode)
{
    (*newnode)->next = *list;
    *list = *newnode;
}

Node *remove_from_list(Node *ptr, int n)
{
    Node *aux = NULL;

    if (ptr == NULL) // this means that theres is no 'n' in this linked list
    {
        exit(1);
    }
    if (ptr->next == n)
    {                    // if this is the value you want
        aux = ptr->next; // aux will point to the remaining list
        free(ptr);       // free the actual node
        return aux;      // return the pointer to the remaining list
    }
    else // lets see the remaining nodes
        ptr->next = remove_from_list(ptr->next, n);

    return ptr;
}