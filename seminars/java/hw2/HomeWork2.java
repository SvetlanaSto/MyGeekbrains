public class HomeWork2 {
    public static void main(String[] arg) {

        // 1. Напишите программу, чтобы найти вхождение в строке (содержащей все символы
        // другой строки).
        boolean t1f = contains("asdf", "ghjk");
        System.out.println("результат поиска несуществующей подстроки: " + t1f);
        boolean t1t = contains("asdf", "asd");
        System.out.println("результат поиска существующей подстроки: " + t1t);

        // 2. Напишите программу, чтобы проверить, являются ли две данные строки
        // вращением друг друга (вхождение в обратном порядке).
        boolean t2f = isReverse("asdf", "ghjk");
        System.out.println("проверка вращения строк (false): " + t2f);
        boolean t2t = isReverse("asdf", "fdsa");
        System.out.println("проверка вращения строк (true): " + t2t);

        // 4. Дано два числа, например 3 и 56, необходимо составить следующие строки:
        // 3 + 56 = 59
        // 3 – 56 = -53
        // 3 * 56 = 168
        // Используем метод StringBuilder.append().
        String t4 = calculate(3, 56);
        System.out.println(t4);

        // 5. Замените символ “=” на слово “равно”. Используйте методы
        // StringBuilder.insert(),StringBuilder.deleteCharAt().
        double begin = System.currentTimeMillis();
        String t5 = replaceRavno5("3 + 56 = 59");
        System.out.println(t5);
        System.out.println(System.currentTimeMillis() - begin);

        // 6*. Замените символ “=” на слово “равно”. Используйте методы
        // StringBuilder.replace().
        begin = System.currentTimeMillis();
        String t6 = replaceRavno6("3 + 56 = 59");
        System.out.println(t6);
        System.out.println(System.currentTimeMillis() - begin);
    }

    private static String replaceRavno5(String str) {
        StringBuilder sb = new StringBuilder(str);
        int i = sb.indexOf("=");
        sb.deleteCharAt(i);
        sb.insert(i, "равно");
        return sb.toString();
    }

    private static String replaceRavno6(String str) {
        StringBuilder sb = new StringBuilder(str);
        int i = sb.indexOf("=");
        sb.replace(i, i + 1, "равно");
        return sb.toString();
    }

    private static String calculate(int a, int b) {
        StringBuilder sb = new StringBuilder();
        sb.append(a);
        sb.append(" + ");
        sb.append(b);
        sb.append(" = ");
        sb.append(a + b);
        sb.append("\n");
        sb.append(a);
        sb.append(" - ");
        sb.append(b);
        sb.append(" = ");
        sb.append(a - b);
        sb.append("\n");
        sb.append(a);
        sb.append(" * ");
        sb.append(b);
        sb.append(" = ");
        sb.append(a * b);

        return sb.toString();
    }

    private static boolean contains(String s1, String s2) {
        return s1.contains(s2);
    }

    private static boolean isReverse(String s1, String s2) {
        return s1.equals(new StringBuilder(s2).reverse().toString());
    }

}