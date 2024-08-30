#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void readFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    fclose(file);
}

void writeFile(const char *filename, const char *content) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }
    fprintf(file, "%s", content);
    fclose(file);
}
// #include <stdio.h>

// Example of a simple main function
int main(int argc, char *argv[]) {
    if (argc > 1) {
        readFile(argv[1]); // Assuming readFile is one of your defined functions
    } else {
        printf("Please provide a file name.\n");
    }
    return 0;
}
