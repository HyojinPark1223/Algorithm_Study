// 25.02.04 Baekjoon 알고리즘 기초 공부

using System;
using System.Collections.Generic;

namespace Baekjoon.Gold
{
    class _31246
    {
        static void Main(string[] args)
        {
            string nums = Console.ReadLine();
            string[] numList = nums.Split(' ');

            // N, K를 받아줌
            int n = Int32.Parse(numList[0]);
            int k = Int32.Parse(numList[1]);

            // 지면을 낙찰받으려면 숫자의 크기가 더 커야하므로 두 입찰 가격의 차이를 구해서 K번째로 작은 수를 Return하면 된다.
            // 이때 0이하의 숫자가 나오면 0으로 반환하도록 조정 필요.
            List<int> result = new List<int>();

            for(int i=0; i<n; i++){
                string st = Console.ReadLine();
                string[] stList = st.Split(' ');
                
                // 두 입찰가의 차이를 구해서 List에 담아줌.
                result.Add(Int32.Parse(stList[1]) - Int32.Parse(stList[0]));
            } 
            // 정렬
            result.Sort();
            int answer = result[k-1];
            if(answer < 0){
                Console.WriteLine(0);
            }
            else{
                Console.WriteLine(answer);
            }
        }
    }
}