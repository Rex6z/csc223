typedef struct node
{
    int val;
    struct node *next;
} Node;

Node *make_node(int);
void insert_in_front(Node **, Node **);

Node *remove_from_list(Node *, int);