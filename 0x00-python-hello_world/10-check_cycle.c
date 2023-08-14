#include "lists.h"
/**
 *check_cycle - finds cycle if present in linked list
 *@list: head
 *Return: 1 if cycle found, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *behind, *ahead;

	if (!list || !(list->next))
		return (0);
	behind = list;
	ahead = list;

	while (ahead != NULL && ahead->next != NULL)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (behind == ahead)
			return (1);
	}

	return (0);
}
