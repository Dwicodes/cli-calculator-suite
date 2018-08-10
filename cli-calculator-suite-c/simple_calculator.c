#include <stdio.h>

int main() {
    int choice;
    double num1, num2, result;

    while (1) {
        printf("\n=== Kalkulator Sederhana ===\n");
        printf("1. Penjumlahan\n");
        printf("2. Pengurangan\n");
        printf("3. Perkalian\n");
        printf("4. Pembagian\n");
        printf("5. Keluar\n");
        printf("Pilih operasi (1-5): ");
        scanf("%d", &choice);

        if (choice == 5) {
            printf("Terima kasih!\n");
            break;
        }

        printf("Masukkan angka pertama: ");
        scanf("%lf", &num1);
        printf("Masukkan angka kedua: ");
        scanf("%lf", &num2);

        switch (choice) {
            case 1:
                result = num1 + num2;
                break;
            case 2:
                result = num1 - num2;
                break;
            case 3:
                result = num1 * num2;
                break;
            case 4:
                if (num2 == 0) {
                    printf("Error: Pembagian dengan nol!\n");
                    continue;
                }
                result = num1 / num2;
                break;
            default:
                printf("Pilihan tidak valid.\n");
                continue;
        }

        printf("Hasil: %.2lf\n", result);
    }

    return 0;
}
