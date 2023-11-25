#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
/**
 * infinite_while - runs an infinite while loop
 *
 * Return: 0
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
 * main - spawn 5 zombie processess
 *
 * Return: 0 for success, -1 for error/failure
 */
int main(void)
{
	/* create a pid variable type*/
	pid_t pid;
	int i; /*create a for counter of how many processes to fork*/

	for (i = 0; i < 5; i++)
	{
		/*fork the first process and check for return value, do same for the rest*/
		pid = fork();

		if (pid == -1)
		{
			perror("Error: fork failed");
			exit(1);
		}

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	/*call the infinite while loop, which child would terminate before parent*/
	infinite_while();
	return (0);
}
