#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - Structure for a singly linked list node
 * @n: Integer value (data) stored in the node
 * @next: Pointer to the next node in the list
 *
 * Description:
 * This structure defines a singly linked list node. It consists of an integer
 * value 'n' to hold data and a 'next' pointer that points to the next node
 * in the linked list, creating a linkage between nodes.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int numb);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif
