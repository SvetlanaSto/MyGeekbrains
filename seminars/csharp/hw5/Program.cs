// Задача 1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
/*
int[] CreateThreeDiditArray(int size)
{
    int[] arr = new int[size];
    for (int i = 0; i < size; i++)
        arr[i] = new Random().Next(100, 1000);

    return arr;
}

void ShowArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        Console.Write(array[i] + " ");

    Console.WriteLine();
}

int CountEvenNumbers(int[] array)
{
    int count = 0;

    for (int i = 0; i < array.Length; i++)
        if (array[i] % 2 == 0) count++;

    return count;
}

Console.Write("Input array size: ");
int size = Convert.ToInt32(Console.ReadLine());

int[] newArray = CreateThreeDiditArray(size);
ShowArray(newArray);

Console.WriteLine($"Count of even numbers in array is {CountEvenNumbers(newArray)}");
*/

//Задача 2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
/*
int[] CreateRandomArray(int size, int minVal, int maxVal)
{
    int[] arr = new int[size];
    for (int i = 0; i < size; i++)
        arr[i] = new Random().Next(minVal, maxVal+1);

    return arr;
}

void ShowArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        Console.Write(array[i] + " ");

    Console.WriteLine();
}

int FindSumOfOddElements(int[] array)
{
    int sum = 0;

    for (int i = 1; i < array.Length; i += 2)
        sum += array[i];

    return sum;
}

Console.Write("Input array size: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min possible value: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max possible value: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] newArray = CreateRandomArray(size, min, max);
ShowArray(newArray);

Console.WriteLine($"Sum of odd elements in array is {FindSumOfOddElements(newArray)}");
*/

//Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

double[] CreateRandomArray(int size)
{
    double[] arr = new double[size];
    for (int i = 0; i < size; i++)
        arr[i] = new Random().Next(0, 1000) + new Random().NextDouble();

    return arr;
}

void ShowArray(double[] array)
{
    for (int i = 0; i < array.Length; i++)
        Console.Write(array[i] + " ");

    Console.WriteLine();
}

double DifferenceBetweenMaxAndMin(double[] array)
{
    double max = array[0];
    double min = array[0];

    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < min) min = array[i];
        if (array[i] > max) max = array[i];
    }

    return max - min;
}

Console.Write("Input array size: ");
int size = Convert.ToInt32(Console.ReadLine());

double[] newArray = CreateRandomArray(size);
ShowArray(newArray);

Console.WriteLine($"Difference between max & min is {DifferenceBetweenMaxAndMin(newArray)}");
