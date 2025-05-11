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
	int mid, length = 0, i, *arr;
	listint_t *temp = *head;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		length++;
	}
	temp = *head;
	mid = length / 2;
	arr = malloc(mid * sizeof(int));

	for (i = 0; i < mid; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	if (length % 2 == 1)
		temp = temp->next;
	for (i = mid - 1; i >= 0 ; i--)
	{
		if ((temp->n) != arr[i])
		{
			free(arr);
			return (0);
		}
		temp = temp->next;
	}
	free(arr);
	return (1);
}
