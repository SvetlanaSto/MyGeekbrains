import java.util.Arrays;

public class Task2 {

    public static int[] calculateDiff(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            System.out.println("Длины массивов не равны!");
            return null;
        }

        int[] diff = new int[arr1.length];

        for (int i = 0; i < arr1.length; i++) {
            diff[i] = arr1[i] - arr2[i];
        }

        return diff;
    }

    public static void main(String[] args) {
        int[] array1 = { 1, 2, 3, 4, 5 };
        int[] array2 = { 5, 4, 3, 2, 1, 10 };

        int[] diffArray = calculateDiff(array1, array2);
        if (diffArray != null) {
            System.out.print("Разность элементов массивов: ");
            System.out.println(Arrays.toString(diffArray));
        }
    }
}