using System;

// DFS 2차원 배열
class Graph
{
    int[,] adj = new int[6, 6]
    {
            { 0, 1, 0, 1, 0, 0},
            { 1, 0, 1, 1, 0, 0},
            { 0, 1, 0, 0, 0, 0},
            { 1, 1, 0, 0, 0, 0},
            { 0, 0, 0, 0, 0, 1},
            { 0, 0, 0, 0, 1, 0},
    };
    bool[] visited = new bool[6];

    //1) now부터 방문
    //2) now와 연결된 정점들을 하나씩 확인해서 [아직 미방문 상태라면]방문
    public void DFS(int now)
    {
        Console.WriteLine(now);
        visited[now] = true; //1) now부터 방문

        for (int next = 0; next < 6; next++)
        {
            if (adj[now, next] == 0)//연결된 정점이라면 스킵
                continue;
            if (visited[next])//이미 방문한 곳이라면 스킵
                continue;

            DFS(next);
        }
    }

    public void SearchAll()
    {
        visited = new bool[6];
        for (int now = 0; now < 6; now++)
        {
            if (visited[now] == false)
                DFS(now);
        }
    }
}


// DFS 리스트 사용
class Graph
{
    List<int>[] adj2 = new List<int>[]
    {
            new List<int>(){ 1, 3},
            new List<int>(){ 0, 2, 3 },
            new List<int>(){ 1 },
            new List<int>(){ 0, 1, 4 },
            new List<int>(){ 3, 5},
            new List<int>(){ 4 },
    };
    bool[] visited = new bool[6];
    public void DFS2(int now)
    {
        Console.WriteLine(now);
        visited[now] = true; //1) now부터 방문

        foreach (int next in adj2[now])
        {
            if (visited[next])//이미 방문한 곳이라면 스킵
                continue;

            DFS2(next);
        }
    }
}

// BFS
class Graph
{
    int[,] adj = new int[6, 6]
    {
            { 0, 1, 0, 1, 0, 0},
            { 1, 0, 1, 1, 0, 0},
            { 0, 1, 0, 0, 0, 0},
            { 1, 1, 0, 0, 0, 0},
            { 0, 0, 0, 0, 0, 1},
            { 0, 0, 0, 0, 1, 0},
    };


    public void BFS(int now)
    {
        bool[] visited = new bool[6];   //정점 방문 확인

        Queue<int> q = new Queue<int>();
        q.Enqueue(start);
        visited[start] = true;

        while(q.Count > 0)
        {
            int now =  q.Dequeue();
            Console.WriteLine(now);

            for(int next = 0; next < 6; next++){
                if (adj[now, next] == 0)
                    continue;
                if (visited[next])
                    continue;

                q.Enqueue(next);
                visited[next] = true;
            }
        }
    }
}