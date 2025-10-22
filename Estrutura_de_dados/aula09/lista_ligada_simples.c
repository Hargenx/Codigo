#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int val;
  struct Node *next;
} Node;

Node *push_front(Node *head, int v) {
  Node *n = (Node *)malloc(sizeof *n);
  n->val = v;
  n->next = head;
  return n;
}

void print_list(Node *h) {
  for (; h; h = h->next)
    printf("%d ", h->val);
  puts("");
}

void free_list(Node *h) {
  while (h) {
    Node *t = h->next;
    free(h);
    h = t;
  }
}

int main() {
  Node *head = NULL;
  head = push_front(head, 3);
  head = push_front(head, 10);
  head = push_front(head, 7);
  print_list(head);
  free_list(head);
  return 0;
}
