//2025.02.04 C# softeer 알고리즘 기초 공부

using System;

namespace softeer
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            string answer = s.Replace("()", "(1)");
            answer = answer.Replace(")(", ")+(");

            Console.WriteLine(answer);
        }
    }
}