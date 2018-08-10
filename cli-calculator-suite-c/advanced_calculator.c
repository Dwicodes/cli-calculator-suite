#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    double num1, num2, result;

    while (1) {
        printf("\n=== Kalkulator Lanjutan ===\n");
        printf("1. Tambah\n");
        printf("2. Kurang\n");
        printf("3. Kali\n");
        printf("4. Bagi\n");
        printf("5. Modulus\n");
        printf("6. Pangkat\n");
        printf("7. Keluar\n");
        printf("Pilih operasi (1-7): ");
        scanf("%d", &choice);

        if (choice == 7) {
            printf("Keluar dari program. Terima kasih!\n");
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
            case 5:
                if ((int)num2 == 0) {
                    printf("Error: Modulus dengan nol!\n");
                    continue;
                }
                result = (int)num1 % (int)num2;
                break;
            case 6:
                result = pow(num1, num2);
                break;
            default:
                printf("Pilihan tidak valid!\n");
                continue;
        }

        printf("Hasil: %.2lf\n", result);
    }

    return 0;
}
