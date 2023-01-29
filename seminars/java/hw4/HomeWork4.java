import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;

/*
1.Сохранить в файл строку и загрузить из файла строку с выводом в консоль используя классы FileWriter и FileReader
2.Загрузить из файла многострочный текст формата ФИО возраст и пол через пробелы. Разбить по строкам и вывести в консоль в формате "Иванов И.И. 32 М"
3.Загруженный и разбитый по строкам текст загрузить в подготовленные списки. Фамилии, имена, отчества, возрас и пол в отдельных списках.
4.Отсортировать по возрасту используя дополнительный список индексов.
 */
public class HomeWork4 {
    public static void main(String[] args) {

        task1();

        ArrayList<String> lastname = new ArrayList<>();
        ArrayList<String> firstname = new ArrayList<>();
        ArrayList<String> patronymic = new ArrayList<>();
        ArrayList<Integer> age = new ArrayList<>();
        ArrayList<Boolean> gender = new ArrayList<>();
        LinkedList<Integer> index = new LinkedList<>();

        String text = "";
        try {
            FileReader fileReader = new FileReader("db.sql");
            while (fileReader.ready()) {
                text += (char) fileReader.read();
            }
            fileReader.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        String[] str = text.split("\n");
        for (int i = 0; i < str.length; i++) {
            String[] sb = str[i].split(" ");
            lastname.add(sb[0]);
            firstname.add(sb[1].charAt(0) + ".");
            patronymic.add(sb[2].charAt(0) + ".");
            age.add(Integer.valueOf(sb[3]));
            gender.add(sb[4].equals("Ж") ? true : false);
            index.add(i);
        }
        index.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return age.get(o1) - age.get(o2);
            }
        });

        for (int i = 0; i < index.size(); i++) {
            System.out.printf(lastname.get(index.get(i)) + " ");
            System.out.printf(firstname.get(index.get(i)));
            System.out.printf(patronymic.get(index.get(i)) + " ");
            System.out.printf(age.get(index.get(i)).toString());
            System.out.printf((gender.get(index.get(i)) ? " Ж" : " М"));
            System.out.println();
        }

        System.out.println(lastname);
    }

    private static void task1() {
        try {
            FileWriter fileWriter = new FileWriter("task1.txt", true);
            fileWriter.append("Hello world from task1");
            fileWriter.flush();
            fileWriter.close();

            String text = "";
            FileReader fileReader = new FileReader("task1.txt");
            while (fileReader.ready()) {
                text += (char) fileReader.read();
            }
            fileReader.close();
            System.out.println(text);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
