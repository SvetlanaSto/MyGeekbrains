//Задача 1: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

Console.Write("Input m integer numbers: ");
int num = Convert.ToInt32(Console.ReadLine());
int count = 0;

{
    while (num <= m)
    {
        Console.Write("Input next number: ");
        count ++;
    }
    
}

Console.WriteLine($"Count of pozitiv numbers is {count}");
