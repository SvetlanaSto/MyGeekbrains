public class Task2 {

    public static void main(String[] args) {
        try {
            int d = 0;
            int[] intArray = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }

    }
}