#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 *insert_node - inserts a number to a sorted linked list.
 *@head: the list
 *@number: number to be inserted
 *Return: address of the new node;
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));


	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (temp == NULL)
		new_node->next = NULL;
	else
	{
		while (temp->n <= number)
			temp = temp->next;
		new_node->next = temp->next;
	}
	temp->next = new_node;
	return (new_node);
}
