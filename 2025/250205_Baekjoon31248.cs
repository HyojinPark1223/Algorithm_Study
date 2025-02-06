// 25.02.05 Baekjoon C# 알고리즘 기초 공부
using System;
using System.Text;

namespace Baekjoon.Gold
{
    class _31248
    {
        static StringBuilder stb = new StringBuilder();
        static int M = 0;
        static void Main(string[] args)
        {
            int N = 2;
            d_Hanoi(N, 'A', 'D', 'B', 'C');
            Console.WriteLine(M);
            Console.WriteLine(stb);
        }

        static void Hanoi(int N, char from, char to, char rest){
            if(N == 1){
                move(from, to);
                return;
            }

            Hanoi(N - 1, from, rest, to);
            Hanoi(1, from, to, rest);
            Hanoi(N - 1, rest, to, from);
        }

        static void d_Hanoi(int N, char from, char to, char rest1, char rest2){
            if (N == 1) {
                move(from, to);
                return;
            } else if (N == 2) {
                move(from, rest2);
                move(from, to);
                move(rest2, to);
                return;
            }

            Hanoi(N - 2, from, rest1, rest2);  // 1. (N - 2)개를 D가 아닌 기둥으로 옮기기
            move(from, rest2);  // 2. 두 번째로 큰 원판을 D가 아닌 비어있는 기둥으로 옮기기
            move(from, to);	  // 3. 가장 큰 원판을 D로 옮기기
            move(rest2, to);  // 4. 두 번째로 큰 원판을 D로 옮기기
            d_Hanoi(N - 2, rest1, to, from, rest2);	
        }

        static void move(char from, char to){
            stb.Append($"{from} {to}\n");
            M++;
        }
    }
}