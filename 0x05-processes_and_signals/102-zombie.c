#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
/**
 * infinite_while - infinite loop
 * Return: int
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
 * main - main block
 * Return: int
 */
int main(void)
{
	pid_t pid;
	int num = 0;

	while (num < 5)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			num++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
