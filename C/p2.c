#include <stdio.h>

int main() {
    int r, c, z = 0;
    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);

    int a[r][c];

    printf("Enter elements:\n");
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            scanf("%d", &a[i][j]);
            if(a[i][j] == 0) {
                z++;
            }
        }
    }

    printf("Total zero elements: %d\n", z);

    return 0;
}
