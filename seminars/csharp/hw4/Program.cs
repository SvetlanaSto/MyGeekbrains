// Задача 1: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B
/*
int Pow(int a, int b)
{
    int result = 1;
    for (int i = 1; i <= b; i++)
        result *= a;
    return result;
}

Console.Write("Input integer number: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Input integer number (power of first number): ");
int b = Convert.ToInt32(Console.ReadLine());
int res = Pow(a, b);
Console.WriteLine($"{a} to the power o{b} B is {res}");
*/

// Задача 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
/*
int SumOfDigits(int num)
{
    int sum = 0;
    while (num > 0)
    {
        sum += num % 10;
        num = num / 10;
    }
    return sum;
}

Console.Write("Input integer number: ");
int num = Convert.ToInt32(Console.ReadLine());
int result = SumOfDigits(num);
Console.WriteLine($"Sum of digits of {num} is {result}");
*/

//Задача 3: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран
/*
int[] CreateArray(int size)
{
    int[] arr = new int[size];
    for (int i = 0; i < size; i++)
    {
        Console.Write($"Input element #{i}: ");
        arr[i] = Convert.ToInt32(Console.ReadLine());
    }
    return arr;
}

void PrintArray(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
        Console.Write($"{arr[i]}, ");
    Console.WriteLine("\b\b]");
}

Console.Write("Input array size: ");
int size = Convert.ToInt32(Console.ReadLine());
PrintArray(CreateArray(size));
*/
