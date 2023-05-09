#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - function of the prototype
 * Return: 0 if no cycle, 1 is yes
*/
int check_cycle(listint_t *list)
{
listint_t *faster = list;
listint_t *slower = list;
if (!list)
return (0);
while (1)
{
if (faster->next != NULL && faster->next->next != NULL)
{
faster = faster->next->next;
slower = slower->next;
if (faster == slower)
return (1);
}
else
return (0);
}
}
