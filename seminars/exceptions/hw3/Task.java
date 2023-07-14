import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Task {
    public static void main(String[] args) {
        
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Введите данные (Фамилия Имя Отчество номер_телефона): ");
            String input = scanner.nextLine();
            
            String[] inputData = input.split(" ");
            if (inputData.length != 4) {
                throw new IllegalArgumentException("Неверное количество данных");
            }
            
            String surname = inputData[0];
            String firstName = inputData[1];
            String patronymic = inputData[2];
            long phoneNumber = Long.parseLong(inputData[3]);
            
            String fileName = surname + ".txt";
            String fileContent = String.format("<%s><%s><%s><%d>\n", surname, firstName, patronymic, phoneNumber);
            
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {
                writer.write(fileContent);
            }
            
            System.out.println("Данные успешно записаны в файл: " + fileName);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка: номер телефона должен быть целым беззнаковым числом");
        } catch (IllegalArgumentException e) {
            System.out.println("Ошибка: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Ошибка при записи данных в файл:");
            e.printStackTrace();
        } 
    }
}