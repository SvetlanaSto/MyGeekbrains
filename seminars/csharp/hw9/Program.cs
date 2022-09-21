// Задача 1: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
/*
void ShowNums(int m, int n)
{
    Console.Write(m + " ");
    if (n > m) ShowNums(m + 1, n);
}

Console.Write("Input m: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Input n: ");
int n = Convert.ToInt32(Console.ReadLine());

ShowNums(m, n);
Console.WriteLine();
*/

//Задача 2: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
/*
int SumNumbers(int m, int n)
{
    if (m == n) return n;
    else return n + SumNumbers(m, n - 1);
}

Console.Write("Input m: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Input n: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(SumNumbers(m, n));
*/

// Задача 3: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
/*
int Akk(int m, int n)
{
    if (m == 0) return n + 1;
    else if (m > 0 && n == 0) return Akk(m - 1, 1);
    else return Akk(m - 1, Akk(m, n - 1));
}

Console.Write("Input m: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Input n: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(Akk(m, n));

// Примечание к примеру в задаче 3: корректный ответ для Akk(2, 3) = 9; 29 возвращается для Akk(3, 2)
// https://qastack.ru/codegolf/40141/the-ackermann-function
*/
