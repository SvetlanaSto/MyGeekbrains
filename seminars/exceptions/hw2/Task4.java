import java.util.Scanner;

// Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
// Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

public class Task4 {
    public static String getLineInput() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите непустую строку: ");
        String result = scanner.nextLine();
        scanner.close();

        if (result.isEmpty()) {
            throw new RuntimeException("Вы ввели пустую строку!");
        }

        return result;
    }

    public static void main(String[] args) {
        String userInput = getLineInput();
        System.out.println("Введенная строка: " + userInput);
    }
}
