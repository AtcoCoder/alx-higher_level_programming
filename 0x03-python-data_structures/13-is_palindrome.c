#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_listint(listint_t **list_head);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: pointer to the pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;
	listint_t *current = NULL;
	listint_t *second_head = NULL;

	if (*head == NULL)
		return (1);
	else if ((*head)->next == NULL)
		return (1);
	else if ((*head)->next->next == NULL)
	{
		if (((*head)->n) == ((*head)->next->n))
			return (1);
		else
			return (0);
	}
	slow = *head;
	fast = *head;
	while (1)
	{
		fast = fast->next->next;
		if (fast->next == NULL)
		{
			second_head = slow->next;
			slow = NULL;
			break;
		}
		if (fast->next->next == NULL)
		{
			second_head = slow->next;
			slow->next = NULL;
			break;
		}
		slow = slow->next;
	}
	second_head = reverse_listint(&second_head);
	current = *head;
	while (current != NULL)
	{
		if (current->n != second_head->n)
		{
			return (0);
		}
		current = current->next;
		second_head = second_head->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t list
 * @list_head: pointer to the pointer to the first node
 * Return: pointer to the new first node
 */
listint_t *reverse_listint(listint_t **list_head)
{
	listint_t *current;
	listint_t *previous = NULL;

	current = *list_head;
	while ((*list_head)->next != NULL)
	{
		*list_head = (*list_head)->next;
		current->next = previous;
		previous = current;
		current = *list_head;
	}
	(*list_head)->next = previous;
	return (*list_head);
}
