//Задача 1. Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом
/*
bool CheckPalindrom(int num)
{
    int temp = num;
    int reversed = 0;
    while (temp > 0)
    {
        reversed = reversed * 10 + temp % 10;
        temp = temp / 10;
    }
    if (reversed == num)
        return true;
    else
        return false;
}

Console.Write("Input integer number: ");
int num = Convert.ToInt32(Console.ReadLine());

bool isPalindrom = CheckPalindrom(num);

if (isPalindrom == true)
    Console.WriteLine("It is palindrom");
else
    Console.WriteLine("It is not palindrom");
*/

//Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
/*
double FindDistance(double x1, double y1, double z1, double x2, double y2, double z2)
{
    double result = Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2) + Math.Pow(z1 - z2, 2));
    return result;
}

Console.Write("Input x of point1: ");
double x1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input y of point1: ");
double y1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input z of point1: ");
double z1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input x of point2: ");
double x2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input y of point2: ");
double y2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input z of point2: ");
double z2 = Convert.ToDouble(Console.ReadLine());

double d = FindDistance(x1, y1, z1, x2, y2, z2);
Console.WriteLine($"Distance between two points is {d}");
*/

//Задача 3. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
/*
void TableOfCubes(int n)
{
    int i = 1;
    while (i <= n)
    {
        double cube = Math.Pow(i, 3);
        Console.WriteLine($"Cube of {i} is {cube}");
        i++;
    }
}

Console.Write("Input integer number: ");
int n = Convert.ToInt32(Console.ReadLine());
TableOfCubes(n);
*/