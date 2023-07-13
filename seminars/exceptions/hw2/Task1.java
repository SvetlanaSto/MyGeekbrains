import java.util.Scanner;

// Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. 
// Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить 
// у пользователя ввод данных.
public class Task1 {
    public static float getFloatInput() {
        Scanner scanner = new Scanner(System.in);
        float result = 0;
        boolean validInput = false;

        while (!validInput) {
            try {
                System.out.print("Введите дробное число: ");
                result = Float.parseFloat(scanner.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Ошибка! Введено некорректное значение. Попробуйте снова.");
            }
        }
        scanner.close();

        return result;
    }

    public static void main(String[] args) {
        float userInput = getFloatInput();
        System.out.println("Введенное число: " + userInput);
    }
}
