#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: list to be checked
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (list == NULL)
		return (0);
	while (tortoise && tortoise->next)
	{
		hare = hare->next;
		tortoise = tortoise->next->next;
		if (hare == tortoise)
			return (1);
	}
	return (0);
}
