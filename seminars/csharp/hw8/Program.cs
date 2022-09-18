// Задача 1: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
/*
int[,] CreateRandom2dArray()
{
    Console.Write("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input number of columns: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input min possible value: ");
    int minValue = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input max possible value: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

    int[,] newArray = new int[rows, columns];

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            newArray[i, j] = new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void Show2dArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j] + " ");

        Console.WriteLine();
    }
    Console.WriteLine();
}

void SortElements(int[,] array)
{
    int temp;

    for (int i = 0; i < array.GetLength(0); i++)
        for (int j = 0; j < array.GetLength(1); j++)
            for (int k = j + 1; k < array.GetLength(1); k++)
            {
                if (array[i, k] > array[i, j])
                {
                    temp = array[i, k];
                    array[i, k] = array[i, j];
                    array[i, j] = temp;
                }
            }
}

int[,] myArray = CreateRandom2dArray();
Show2dArray(myArray);
SortElements(myArray);
Show2dArray(myArray);
*/

// Задача 2: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
/*
int[,] CreateRandom2dArray()
{
    Console.Write("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input number of columns: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input min possible value: ");
    int minValue = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input max possible value: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

    int[,] newArray = new int[rows, columns];

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            newArray[i, j] = new Random().Next(minValue, maxValue + 1);

    return newArray;
}

void Show2dArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j] + " ");

        Console.WriteLine();
    }
    Console.WriteLine();
}

int SumOfRow(int[,] array, int row)
{
    int sum = 0;
    for (int j = 0; j < array.GetLength(1); j++)
        sum += array[row, j];
    return sum;
}

int FindRowWithMaxSum(int[,] array)
{
    int maxSum = SumOfRow(array, 0);
    int maxRow = 0;
    for (int i = 1; i < array.GetLength(0); i++)
    {
        int iSum = SumOfRow(array, i);
        if (iSum > maxSum)
        {
            maxRow = i;
            maxSum = iSum;
        }
    }
    return maxRow;
}

int[,] myArray = CreateRandom2dArray();
Show2dArray(myArray);
int maxRow = FindRowWithMaxSum(myArray);
Console.WriteLine($"Row with max sum is {maxRow + 1}");
*/

// Задача 3: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
/*
int[,] CreateRandom2dArray()
{
    Console.Write("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input number of columns: ");
    int columns = Convert.ToInt32(Console.ReadLine());

    int[,] newArray = new int[rows, columns];

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            newArray[i, j] = new Random().Next(0, 10);

    return newArray;
}

void Show2dArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j] + " ");

        Console.WriteLine();
    }
    Console.WriteLine();
}

int[,] MultiplyMatrixes(int[,] mat1, int[,] mat2)
{
    int[,] result = new int[mat1.GetLength(0), mat2.GetLength(1)];
    for (int i = 0; i < mat1.GetLength(0); i++)
    {
        for (int j = 0; j < mat2.GetLength(1); j++)
        {
            for (int k = 0; k < mat2.GetLength(0); k++)
            {
                result[i, j] += mat1[i, k] * mat2[k, j];
            }
        }
    }
    return result;
}

Console.WriteLine("Create matrix 1:");
int[,] matrix1 = CreateRandom2dArray();
Show2dArray(matrix1);
Console.WriteLine("Create matrix 2:");
int[,] matrix2 = CreateRandom2dArray();
Show2dArray(matrix2);
int[,] result = MultiplyMatrixes(matrix1, matrix2);
Console.WriteLine("Result matrix:");
Show2dArray(result);
*/

// Задача 4: Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
/*
int[,,] CreateRandom3dArray()
{
    Console.Write("Input number of rows: ");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input number of columns: ");
    int columns = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input number of pages: ");
    int pages = Convert.ToInt32(Console.ReadLine());

    int[,,] newArray = new int[rows, columns, pages];

    int value = 10;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            for (int k = 0; k < pages; k++)
            {
                newArray[i, j, k] = value;
                value += new Random().Next(1, 4);
            }

    return newArray;
}

void Show3dArray(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
                Console.Write($"{array[i, j, k]}({i},{j},{k}) ");
            Console.WriteLine();
        }        
        Console.WriteLine();
    }
    Console.WriteLine();
}

int[,,] array = CreateRandom3dArray();
Show3dArray(array);
*/
