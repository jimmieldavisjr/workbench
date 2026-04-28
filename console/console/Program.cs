namespace console;

internal class Program
{
    static void Main()
    {
        Console.WriteLine("** Drill 1 **");
        Console.WriteLine("Print Every Element");
        PrintEveryElement.printArray(PrintEveryElement.profile);

        Console.WriteLine();

        Console.WriteLine("**Drill 2**");
        Console.WriteLine("Find The Maximum Element");
        FindMaximumElement.FindMaxAge(FindMaximumElement.ages);

        Console.WriteLine();

        Console.WriteLine("**Drill 3**");
        Console.WriteLine("Find The Minimum Element");
        FindMinimumElement.FindMinAge(FindMinimumElement.ages);

        Console.WriteLine();

        Console.WriteLine("**Drill 4**");
        Console.WriteLine("Sum of All Elements");
        SumAllElements.Sum(SumAllElements.ages);

        Console.WriteLine();

        Console.WriteLine("**Drill 5**");
        Console.WriteLine("Reverse All Elements");
        ReverseArray_3.Reverse(ReverseArray_3.numbers);

        Console.WriteLine();

        Console.WriteLine("**Drill 6**");
        Console.WriteLine("Count All Occurrences");
        CountOccurrences.Count(CountOccurrences.ages, 7);

        Console.WriteLine();

        Console.WriteLine("**Drill 7**");
        Console.WriteLine("Sort If Array Sorted Ascending");
        CheckIfArraySorted.CheckSortAsc(CheckIfArraySorted.numbers);

        Console.WriteLine();

        Console.WriteLine("**Drill 8**");
        Console.WriteLine("Reverse The String");
        ReverseString.Reverse("diaper");

        Console.WriteLine();

        Console.WriteLine("**Drill 9**");
        Console.WriteLine("*Check If String Palindrome");
        CheckStringPalindrome.PalindromeCheck("level");

        Console.WriteLine();

        Console.WriteLine("**Drill 10**");
        Console.WriteLine("**First Non-Repeating Character");
        FindFirstNonRepeatingChar.RepeatCharCheck("pplpp");
    }
}

internal static class PrintEveryElement
{
    public static string[] profile = { "Jimmie", "Davis", "31", "2026", "Active", "Software Engineer" };

    public static void printArray(string[] profile)
    {
        foreach (string item in profile)
        {
            Console.WriteLine(item);
        }
    }
}

internal static class FindMaximumElement
{
    public static int[] ages = { 2, 17, 30, 55, 300, 57, 60, 35, 75, 80, 79, 81, 4, 18, 301 };

    public static int FindMaxAge(int[] ages)
    {
        int max = ages[0];

        for (int i = 0; i < ages.Length; i++)
        {
            if (ages[i] > max)
            {
                max = ages[i];
            }
        }
        Console.WriteLine($"Max is: {max}");

        return max;
    }
}

internal static class FindMinimumElement
{
    public static int[] ages = { 2, 17, 30, 55, 300, 57, 60, 35, 75, 80, 1, 79, 81, 4, 18, 301 };

    public static int FindMinAge(int[] ages)
    {
        int min = ages[0];

        for (int i = 0; i < ages.Length; i++)
        {
            if (ages[i] < min)
            {
                min = ages[i];
            }
        }
        Console.WriteLine($"Min age is: {min}");

        return min;
    }
}

internal static class SumAllElements
{
    public static int[] ages = { 2, 17, 30, 55, 300, 57, 60, 35, 75, 80, 79, 81, 4, 18, 301 };

    public static int Sum(int[] ages)
    {
        int sum = 0;

        foreach (int age in ages)
        {
            sum += age;
        }
        Console.WriteLine($"Sum of all ages: {sum}");

        return sum;
    }


}

internal static class ReverseArray_1
{
    public static int[] numbers = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

    public static int[] Reverse(int[] numbers)
    {
        Array.Reverse(numbers);
        return numbers;
    }
}

internal static class ReverseArray_2
{
    public static int[] numbers = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

    public static int[] Reverse(int[] numbers)
    {
        numbers.Reverse();
        return numbers;
    }
}

internal static class ReverseArray_3
{
    public static int[] numbers = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
    public static string Reverse(int[] numbers)
    {
        int temp = 0;
        string result;

        for (int i = 0; i < numbers.Length / 2; i++)
        {
            temp = numbers[i];
            numbers[i] = numbers[numbers.Length - (1 + i)];
            numbers[numbers.Length - (1 + i)] = temp;
        }

        result = string.Join(", ", numbers);

        Console.WriteLine($"Elements Reversed: {result}");

        return result;
    }
}

internal static class CountOccurrences
{
    public static int[] ages = { 4, 12, 7, 19, 4, 8, 15, 3, 12, 6, 9, 1, 15, 10, 7, 2, 18, 5, 9, 4 };

    public static int Count(int[] ages, int target)
    {
        int count = 0;

        foreach (int age in ages)
        {
            if (age == target)
            {
                count++;
            }
        }
        Console.WriteLine($"Total Occurrences of {target} is: {count}");

        return count;
    }
}

internal static class CheckIfArraySorted
{
    internal static int[] numbers =
    {
        42, -17, 88, -63, 5, -91, 27, -34, 100, -2,
        56, -78, 13, -45, 69, -12, 31, -99, 7, -60
    };

    internal static bool CheckSortAsc(int[] numbers)
    {
        for (int i = 0; i < numbers.Length - 1; i++)
        {
            if (numbers[i] > numbers[i + 1])
            {
                Console.WriteLine($"Is Array Sorted? FALSE");
                return false;
            }
        }

        Console.WriteLine($"Is Array Sorted? TRUE");
        return true;
    }
}

internal static class ReverseString
{
    internal static string Reverse(string text)
    {
        char[] currentArray = text.ToCharArray();
        char[] reversedArray = new char[currentArray.Length];
        string result;

        for (int i = currentArray.Length - 1, k = 0; i >= 0; i--, k++)
        {
            reversedArray[k] = currentArray[i];
        }

        result = new string(reversedArray);
        Console.WriteLine($"Reverse of {text} is: {result}");
        return result;
    }
}

internal static class CheckStringPalindrome
{
    internal static bool PalindromeCheck(string text)
    {
        char[] source = text.ToCharArray();
        char[] result = new char[source.Length];

        for (int i = source.Length - 1, k = 0; i >= 0; i--, k++)
        {
            result[k] = source[i];
        }

        if (new string(result) == text)
        {
            Console.WriteLine($"{true} - The word: {text} IS a Palindrome");
            return true;
        }

        else
        {
            Console.WriteLine($"{false} - The word: {text} IS NOT Palindrome");
            return false;
        }
    }
}

internal class FindFirstNonRepeatingChar
{
    internal static void RepeatCharCheck(string text)
    {
        char temp = text[0];
        
        foreach (char c in text)
        {
            if (c != temp)
            {
                Console.WriteLine($"First Non-Repeating Character is: {c}");
                break;
            }
            temp = c;
        }
    }
}