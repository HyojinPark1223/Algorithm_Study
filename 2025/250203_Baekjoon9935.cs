// 25.02.03 처음 C#으로 코테를 준비해보는 중... 코드 트리는 자동으로 Git에 올라가던데 IDE를 사용하지 않고 문제 푸는 걸 할 땐 깃연동을 계속 잊어버린다..ㅠ

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Baekjoon.Gold
{
    class _9935
    {
        static void Main(string[] args)
        {
            // String은 참조 변수이므로 문자열을 조합할 때마다 새로운 클래스가 생성됨
            // 따라서 문자열 조합 때마다 부하가 발생하니 문자열 변경 횟수가 많을 경우임을 고려하여 StringBuilder를 사용.
            StringBuilder stb = new StringBuilder();
            string str = Console.ReadLine();
            string bomb = Console.ReadLine();

            Stack<char> stack = new Stack<char>();

            for(int i = str.Length-1; i>=0; i--)
            {
                stack.Push(str[i]);
                if (stack.Count >= bomb.Length)
                {
                    if(stack.Peek() == bomb[0])
                    {
                        string check = "";
                        for (int j = 0; j < bomb.Length; j++)
                            check += stack.Pop();

                        if (check != bomb)
                        {
                            for(int j = check.Length-1; j>=0; j--)
                                stack.Push(check[j]);
                        }
                    }
                }
            }

            if (stack.Count > 0)
                while (stack.Count > 0)
                    stb.Append(stack.Pop());
            else
                stb.AppendLine("FRULA");

            Console.WriteLine(stb);
        }
    }
}