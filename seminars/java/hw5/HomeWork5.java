import java.util.HashMap;

/*
Создать словарь HashMap. Обобщение <Integer, String>.
Заполнить пятью ключами (индекс, ФИО+Возраст+Пол "Иванов Иван Иванович 28 м"), добавить ключь, если не было!)
Изменить значения сделав пол большой буквой.
Пройти по коллекции и вывести значения в формате Фамилия инициалы "Иванов И.И."
*Сортировать значения по возрасту и вывести отсортированную коллекция как в четвёртом пункте.
*/

public class HomeWork5 {
    public static void main(String[] args) {

        HashMap<Integer, String> hashMap = new HashMap<>();
        hashMap.putIfAbsent(1, "Иванов Иван Иванович 28 м");
        hashMap.putIfAbsent(2, "Петров Петр Петрович 31 м");
        hashMap.putIfAbsent(3, "Сидорова Снежана Сергеевна 18 ж");
        hashMap.putIfAbsent(4, "Егорова Екатерина Егоровна 25 ж");
        hashMap.putIfAbsent(5, "Васильев Василий Васильевич 55 м");

        for (Integer k : hashMap.keySet()) {
            String oldValue = hashMap.get(k);
            String newValue = oldValue.substring(0, oldValue.length() - 1)
                    + oldValue.substring(oldValue.length() - 1).toUpperCase();
            hashMap.put(k, newValue);
            System.out.println(newValue);
        }

        for (Integer k : hashMap.keySet()) {
            String value = hashMap.get(k);
            String[] arr = value.split(" ");
            String fio = arr[0] + " " + arr[1].substring(0, 1) + "." + arr[2].substring(0, 1) + ".";
            System.out.println(fio);
        }

    }

}