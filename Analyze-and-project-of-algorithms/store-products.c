#include <stdio.h>
#include <string.h>

// Algorithm of sorting and search, with product list, name and id

// Structure of product
struct Product {
    char name[30];
    int id;
};

// Function to sort products by name (ascending order)
void sortByName(struct Product products[], int n) {
    struct Product temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strcmp(products[i].name, products[j].name) > 0) {
                temp = products[i];
                products[i] = products[j];
                products[j] = temp;
            }
        }
    }
}

// Function to sort products by ID (ascending order)
void sortByID(struct Product products[], int n) {
    struct Product temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (products[i].id > products[j].id) {
                temp = products[i];
                products[i] = products[j];
                products[j] = temp;
            }
        }
    }
}

// Function to search for a product by name
struct Product* searchByName(struct Product products[], int n, char name[]) {
    for (int i = 0; i < n; i++) {
        if (strcmp(products[i].name, name) == 0) {
            return &products[i];
        }
    }
    return NULL;
}

// Function to search for a product by ID
struct Product* searchByID(struct Product products[], int n, int id) {
    for (int i = 0; i < n; i++) {
        if (products[i].id == id) {
            return &products[i];
        }
    }
    return NULL;
}

int main() {
    // Initialize product array
    struct Product products[5] = {
        {"Laptop", 101},
        {"Keyboard", 102},
        {"Mouse", 103},
        {"Monitor", 104},
        {"Webcam", 105}
    };
    int n = sizeof(products) / sizeof(products[0]);

    // Display unsorted product list
    printf("Product available:\n\n");
    for (int i = 0; i < n; i++) {
        printf("Name: %s, ID: %d\n", products[i].name, products[i].id);
 
    char searchName[30];
    int searchID;
    printf("\nSearch by Name or ID (enter 'N' for name, 'I' for ID): ");
    char choice;
    scanf(" %c", &choice);
    
    if (choice == 'N' || choice == 'n') {
        printf("Enter product name: ");
        scanf("%s", searchName);
        struct Product* foundProduct = searchByName(products, n, searchName);
        if (foundProduct != NULL) {
            printf("Product Found: Name: %s, ID: %d\n", foundProduct->name, foundProduct->id);
        } else {
            printf("Product not found.\n");
        }
    } else if (choice == 'I' || choice == 'i') {
        printf("Enter product ID: ");
        scanf("%d", &searchID);
        struct Product* foundProduct = searchByID(products, n, searchID);
        if (foundProduct != NULL) {
            printf("Product Found: Name: %s, ID: %d\n", foundProduct->name, foundProduct->id);
        } else {
            printf("Product not found.\n");
        }
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}

