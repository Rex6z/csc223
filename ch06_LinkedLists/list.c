#include <stdio.h>
#include <stdlib.h>
#include "list.h"

Node* make_node(int data)
{
    Node* new = malloc(sizeof(Node));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->val = data;
    new->next = NULL;

    return new;
}

void insert_in_front(Node** list, Node** newnode)
{
    (*newnode)->next = *list;
    *list = *newnode;
}