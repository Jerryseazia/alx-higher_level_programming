#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - prototype of the function
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
unsigned int size = 0, x = 0;
int data[10240];
if (head == NULL)
return (0);
if (*head == NULL)
return (1);
while (tmp)
{
tmp = tmp->next;
size += 1;
}
if (size == 1)
return (1);
tmp = *head;
while (tmp)
{
data[x++] = tmp->n;
tmp = tmp->next;
}
for (x = 0; x <= (size/2); x++)
{
if (data[x] != data[size - x - 1])
return (0);
}
return (1);
}
