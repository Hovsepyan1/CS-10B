#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main() {
    pid_t pid;

    pid = fork();

    if (pid < 0) {
        fprintf(stderr, "Fork Failed\n");
        return 1;
    } 
    else if (pid == 0) {
        
        printf("I am the Child Process!\n");
        printf("Child PID: %d, Parent PID: %d\n", getpid(), getppid());
    } 
    else {
        printf("I am the Parent Process!\n");
        printf("Parent PID: %d, My Child's PID: %d\n", getpid(), pid);
        wait(NULL);
        printf("Finished...\n");
    }

    return 0;
}