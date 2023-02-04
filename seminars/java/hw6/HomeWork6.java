import java.util.HashMap;

/*
Разработать программу, имитирующую поведение коллекции HashSet. 
В программе содать метод add добавляющий элемент, и метод позволяющий 
выводить эллементы коллекции в консоль. Формат данных Integer.
*/

public class HomeWork6 {
    private static HashMap<Integer, Object> hMap = new HashMap<>();
    private static final Object PRESENT = new Object();

    public static void main(String[] args) {
        add(11);
        add(22);
        add(33);
        add(44);

        printSet();
    }

    public static void add(int numbers) {
        hMap.put(numbers, PRESENT);
    }

    public static void printSet() {
        System.out.println(hMap.keySet());
    }

}