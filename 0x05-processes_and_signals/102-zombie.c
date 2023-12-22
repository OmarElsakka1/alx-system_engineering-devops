#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
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
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 * Made by: Omar El-Sakka
 */
int main(void)
{
  pid_t pid;
  char counter = 0;

  while (counter < 5)
    {
      pid = fork();
      if (pid > 0)
	{
	  printf("Zombie process created, PID: %d\n", pid);
	  sleep(1);
	  counter++;
	}
      else
	exit(0);
    }

  infinite_while();

  return (EXIT_SUCCESS);
}
