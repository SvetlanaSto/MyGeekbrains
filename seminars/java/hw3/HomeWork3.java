import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Random;

//1 Объявить два списка список ArrayList, в каждый добавить по 20 случайных чисел. 
//Удалить из первого списка элементы отсутствующие во втором списке. 
//Отсортировать первый список методом sort класса Collections.
//2 * Отсортировать второй список методом sort списка и компаратором по уменьшению.
//3 **Отсортировать первый список пузырьковой сортировкой самостоятельно, без использования доп методов и классов.

public class HomeWork3 {
    public static void main(String[] arg) {
        ArrayList<Integer> list1 = new ArrayList<>(20);
        ArrayList<Integer> list2 = new ArrayList<>(20);

        for (int i = 0; i < 20; i++) {
            list1.add(new Random().nextInt(30));
            list2.add(new Random().nextInt(30));
        }
        System.out.println("list1 = " + list1);
        System.out.println("list2 = " + list2);

        list1.retainAll(list2);
        System.out.println("list1.retainAll(list2) = " + list1);

        Collections.sort(list1);
        System.out.println("list1 (sorted) = " + list1);

        Collections.sort(list2, Comparator.reverseOrder());
        System.out.println("list2 (sorted) = " + list2);
    }

}
