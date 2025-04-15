// 25.04.14 Python에선 조합/순열이 lib가 있는데 C#은 없어서 한 번 만들어보기 연습
namespace SelfStudy;

class Combinations
{
    static int[] arr = new int[] {};
    static bool[] isVisit = new bool[4];

    static List<List<int>> answers = new List<List<int>> () {};
    
    static int N = 4;
    static int r = 2;
    
    static void Main(string[] args)
    {
        arr = [1, 2, 3, 4];
        List<int> select = new List<int>() {};
        Combination_function(0, select);
    }

    static void Combination_function(int start, List<int> select)
    {
        if(select.Count() == r)
        {
            answers.Add(select);
            print(select);
            return;
        }        

        for(int i = start ; i < N ; i++)
        {
            if (isVisit[i] == false)
            {
                isVisit[i] = true;
                select.Add(arr[i]);

                Combination_function(i + 1, select);
                
                select.Remove(arr[i]);
                isVisit[i] = false;
            }
        }
    }

    static void print(List<int> select){
        foreach(int i in select){
            Console.Write(i);
        }
        Console.WriteLine("\n");
    }
}