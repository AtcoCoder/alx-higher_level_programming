#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer to the head node
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev_node;
	listint_t *current_node;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	prev_node = NULL;
	current_node = *head;

	while ((current_node != NULL) && (number > current_node->n))
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	if (prev_node == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev_node->next = new_node;
		new_node->next = current_node;
	}

	return (new_node);
}
