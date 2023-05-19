#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: parametere to be checked
 * Return: 1 cycle, 0 no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	while (slow != fast)
	{
	if (fast == NULL || fast->next == NULL)
	{
	return (0);
	}

	slow = slow->next;
	fast = fast->next->next;
	}

	return (1);
}

