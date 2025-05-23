#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 *is_palindrome - checks if a singly linked list is palindrome
 *@head: pointer to the pointer of the first node
 *Return: 1 if is palindrome, 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	int mid, length = 0, i;
	listint_t *temp = *head, *prev = NULL, *next = NULL;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		length++;
	}
	temp = *head;
	mid = length / 2;

	for (i = 0; i < mid; i++)
	{
		temp = temp->next;
	}
	if (length % 2 == 1)
		temp = temp->next;
	while (temp != NULL)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	temp = prev;

	for (i = 0; i < mid; i++)
	{
		if (temp->n != (*head)->n)
			return (0);
		temp = temp->next;
		*head = (*head)->next;
	}
	return (1);
}
