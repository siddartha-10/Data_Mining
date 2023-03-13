import java.util.Scanner;

public class TriangularFigure {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = 0;

        // Validate user input
        while (n < 1 || n > 9) {
            System.out.print("Enter a number between 1 and 9: ");
            n = input.nextInt();
        }

        // Generate triangular figure
        for (int i = 1; i <= n; i++) {
            // Print left side of row
            for (int j = n; j > i; j--) {
                System.out.print(" ");
            }
//            for (int j = 1; j <= i; j++) {
//                System.out.print(j);
//            }

            // Print right side of row
            for (int j = i ; j >= 1; j--) {
                System.out.print(j);
            }

            // Print spaces for alignment
            for (int j = n - i; j > 0; j--) {
                System.out.print(" ");
            }

            System.out.println();
        }
    }
}
