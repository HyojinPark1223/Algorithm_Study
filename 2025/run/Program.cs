using System;
using System.Text;
using System.Collections.Generic;

namespace run;

class Program
{     
    static void Main(string[] args)
    {
        int N = 8;
        Console.WriteLine(pibo(N));
    }

    static int pibo(int n)
    {
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 1;
        }
        
        return(pibo(n-1) + pibo(n-2));
        
    }
}
