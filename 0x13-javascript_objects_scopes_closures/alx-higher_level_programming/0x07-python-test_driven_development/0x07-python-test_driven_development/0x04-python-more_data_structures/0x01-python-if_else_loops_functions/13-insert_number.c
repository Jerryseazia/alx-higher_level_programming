#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - function of the prototype
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *current = NULL;

	if (!head)
		return (NULL);

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;
	current->next = NULL;

	if (*head == NULL)
	{
		*head = current;
		(*head)->next = NULL;
		return (current);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < current->n)
			(*head)->next = current;
		else
		{
			current->next = *head;
			*head = current;
		}
		return (current);
	}

	temp = *head;
	while (temp->next != NULL)
	{
		if (current->n < temp->n)
		{
			current->next = temp;
			*head = current;
			return (current);
		}
		if (((current->n > temp->n) && (current->n < (temp->next)->n)) ||
		    (current->n == temp->n))
		{
			current->next = temp->next;
			temp->next = current;
			return (current);
		}
		temp = temp->next;
	}
	temp->next = current;
	return (current);
}
