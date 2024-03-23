/* make a program to search 10 names and the program needs to let user to search by name and display names in alphabetical order*/ 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_NAMES 10
#define MAX_NAME_LENGTH 50

// Function to compare two strings for qsort
int compareStrings(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

// Function to search for a name in the list
void searchName(char *names[], char *searchName) {
    int found = 0;
    for (int i = 0; i < NUM_NAMES; ++i) {
        if (strcmp(names[i], searchName) == 0) {
            found = 1;
            break;
        }
    }
    if (found)
        printf("Name '%s' found!\n", searchName);
    else
        printf("Name '%s' not found!\n", searchName);
}

// Function to display all names
void displayNames(char *names[]) {
    printf("Names in alphabetical order:\n\n");
    for (int i = 0; i < NUM_NAMES; ++i) {
        printf("%s\n", names[i]);
    }
}

int main() {
    char *names[NUM_NAMES];
    char inputName[MAX_NAME_LENGTH];
    int option;

    // Prompt user to add 10 names
    printf("Please enter 10 names:\n");
    for (int i = 0; i < NUM_NAMES; ++i) {
        printf("Enter name %d: ", i + 1);
        fgets(inputName, MAX_NAME_LENGTH, stdin);
        // Remove newline character if present
        if (inputName[strlen(inputName) - 1] == '\n')
            inputName[strlen(inputName) - 1] = '\0';
        // Allocate memory for the name and copy it
        names[i] = malloc(strlen(inputName) + 1);
        strcpy(names[i], inputName);
    }

    // Sort names in alphabetical order
    qsort(names, NUM_NAMES, sizeof(char *), compareStrings);

    // Loop until the user chooses to exit
    do {
        // Prompt user to choose an option
        printf("\nOptions:\n");
        printf("1. Search for a name\n");
        printf("2. Display all names\n");
        printf("3. Exit\n");
        printf("Enter option: ");
        scanf("%d", &option);
        getchar(); // Consume newline character

        switch(option) {
            case 1:
                // Prompt user to search for a name
                printf("\nEnter a name to search: ");
                fgets(inputName, MAX_NAME_LENGTH, stdin);
                // Remove newline character if present
                if (inputName[strlen(inputName) - 1] == '\n')
                    inputName[strlen(inputName) - 1] = '\0';

                // Search for the entered name
                searchName(names, inputName);
                break;
            case 2:
                // Display all names
                displayNames(names);
                break;
            case 3:
                printf("Exiting program...\n");
                break;
            default:
                printf("Invalid option!\n");
        }
    } while (option != 3);

    // Free memory allocated for names
    for (int i = 0; i < NUM_NAMES; ++i) {
        free(names[i]);
    }

    return 0;
}