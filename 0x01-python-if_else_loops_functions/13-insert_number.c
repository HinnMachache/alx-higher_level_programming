#include "lists.h"
/**
 * insert_node - insert number into a sorted list
 * @head: Head Pointer
 * @number: Number to insert
 * Return: Address of new nonde created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *temp;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	temp = *head;
	newNode->n = number;
	if (head == NULL || *head->n >= number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (temp->next && temp->next->n < number)
		temp = temp->next;
	newNode->next = temp->next;
	temp->next = newNode;

	return (newNode);
}

