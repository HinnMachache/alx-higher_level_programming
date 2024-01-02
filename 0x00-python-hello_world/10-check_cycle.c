#include "lists.h"
/**
 * check_cycle - Checks if cycles exists in a list
 * @list: Head pointer to the list
 * Return: 0 if no Cycle, else 1
 * Used Floyd's Tortoise and Hare
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
