import java.util.Arrays;
import java.util.Random;

public class HomeWork1 {
    public static void main(String[] args) {

        int i = getRandomInt();
        int n = getMaxBit(i);

        int[] m1 = getDivisibles(i, n);
        int[] m2 = getNonDivisibles(i, n);

        System.out.println("i = " + i);
        System.out.println("n = " + n);

        // System.out.println(Arrays.toString(m1));
        // System.out.println(Arrays.toString(m2));
        System.out.println("m1 size = " + m1.length);
        System.out.println("m2 size = " + m2.length);
    }

    private static int getRandomInt() {
        return new Random().nextInt(2000);
    }

    private static int getMaxBit(int i) {
        return Integer.toBinaryString(i).length();
    }

    private static int[] getDivisibles(int i, int n) {
        int count = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j % n == 0)
                count++;
        }

        int[] m1 = new int[count];
        count = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j % n == 0)
                m1[count++] = j;
        }
        return m1;
    }

    private static int[] getNonDivisibles(int i, int n) {
        int count = 0;
        for (int j = Short.MIN_VALUE; j < i; j++) {
            if (j % n != 0)
                count++;
        }

        int[] m2 = new int[count];
        count = 0;
        for (int j = Short.MIN_VALUE; j < i; j++) {
            if (j % n != 0)
                m2[count++] = j;
        }
        return m2;
    }
}
