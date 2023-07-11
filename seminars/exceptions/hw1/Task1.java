public class Task1 {

    public static void main(String[] args) {
        nullPointer();
        outOfBounds();
        divByZero();
    }

    // java.lang.ArithmeticException: / by zero
    private static void divByZero() {
        int x = 1 / 0;
    }

    // java.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 0
    private static void outOfBounds() {
        int[] arr = {};
        int x = arr[-1];
    }

    // java.lang.NullPointerException: Cannot invoke "String.length()" because "s" is null
    private static void nullPointer() {
        String s = null;
        System.out.println(s.length());
    }

}