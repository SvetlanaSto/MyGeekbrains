//Задача 1. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
/*
int GetSecondDigit(int number)
{
    int last2digits = number % 100;
    int result = last2digits / 10;
    return result;
}

Console.Write("Input three-digit integer number: ");
int num = Convert.ToInt32(Console.ReadLine());
int secondDigit = GetSecondDigit(num);
Console.WriteLine(secondDigit);
*/

//Задача 2. Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
/*
void CheckThirdDigit(int number)
{
    if (number < 100)
    {
        Console.WriteLine("There is no third digit");
    }
    else
    {
        while (number > 999)
        {
            number = number / 10;
        }
        int result = number % 10;
        Console.WriteLine(result);
    }
}

Console.Write("Input integer number: ");
int num = Convert.ToInt32(Console.ReadLine());
CheckThirdDigit(num);
*/

//Задача 3. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
/*
bool CheckWeekend(int dayOfWeek)
{
    if (dayOfWeek > 5)
        return true;
    else
        return false;
}

Console.Write("Input day of week as a number (1-7): ");
int num = Convert.ToInt32(Console.ReadLine());

bool isWeekend = CheckWeekend(num);

if (isWeekend == true)
    Console.WriteLine("It is weekend");
else
    Console.WriteLine("It is not weekend");
*/