#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: first parameter
 * @number: second parameter
 * Return: address or NULL
 * 
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *temp;

	if (head == NULL)
	{
	return (NULL);
	}

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
	{
	return(NULL);
	}

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
	
	*head = newnode;
	

	while (temp->next != NULL)
	{
	temp = temp->next;
	temp->next = newnode;
	temp->n = number;
	}

	return (newnode);
}
