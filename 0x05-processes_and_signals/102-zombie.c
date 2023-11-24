#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - the function name
 * Return: the result
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the principal entry
 * Return: the result
 */
int main(void)
{
	pid_t PID;
	char car;

	for (car = 0; car < 5; car++)
	{
		PID = fork();
		if (PID > 0)
		{
			printf("Zombie process created, PID: %d\n", PID);
			sleep(1);
		}
		else
			exit(EXIT_FAILURE);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
