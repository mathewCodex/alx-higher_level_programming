#include "lists.h"

/**
insert_node - insert a numb into a sorted single list
@head: A ptr to the head
@number: The numb to insert
Author - mathewCodex
Return: if the func dissapoints - NULL else - a ptr to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

		while (node && node->next && node->next->n < number)
			node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
