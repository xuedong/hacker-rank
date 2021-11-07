import java.io.*;
import java.util.*;
import java.math.*;


public class Solution {

    static int[][] graph;
    static int[][] weights;
    static int[] neighbors;
    static long[] count;
    static long MOD = 1000000009;
    static int visited;

    static void dfs(int u, int p, int depth, long sum) {
        visited++;
        count[depth] += sum;
        for (int i = 0; i < neighbors[u]; ++i) {
            int v = graph[u][i];
            if (v == p) continue;
            dfs(v, u, depth + 1, sum + weights[u][i]);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        if (!(1 <= n && n <= 5000))
            throw new RuntimeException();

        graph = new int[n][n];
        weights = new int[n][n];

        count = new long[n];
        for (int i = 0; i < n; ++i)
            count[i] = 0;

        neighbors = new int[n];
        for (int i = 0; i < n; ++i)
            neighbors[i] = 0;

        for (int i = 0; i < n - 1; ++i) {
            int u, v, w;
            u = in.nextInt();
            v = in.nextInt();
            w = in.nextInt();

            if (!(1 <= u && u <= n))
                throw new RuntimeException();
            if (!(1 <= v && v <= n))
                throw new RuntimeException();
            if (!(1 <= w && w <= 1000000000))
                throw new RuntimeException();

            u--;
            v--;

            graph[u][neighbors[u]] = v;
            weights[u][neighbors[u]] = w;
            neighbors[u]++;

            graph[v][neighbors[v]] = u;
            weights[v][neighbors[v]] = w;
            neighbors[v]++;
        }

        for (int i = 0; i < n; ++i) {
            visited = 0;
            dfs(i, i, 0, 0);
            if (visited != n)
                throw new RuntimeException();
        }

        long[] mp = new long[n + 1];
        long[] sp = new long[n + 2];

        mp[0] = 1;
        for (int i = 1; i <= n; ++i)
            mp[i] = (mp[i - 1] * i) % MOD;

        sp[n + 1] = 1;
        for (int i = n; i >= 1; --i)
            sp[i] = (i * sp[i + 1]) % MOD;

        long res = 0;

        for (int i = 0; i < n; ++i) {
            count[i] %= MOD;
            long cur = (count[i] * ((mp[i] * sp[i + 2]) % MOD)) % MOD;
            res = (res + cur) % MOD;
        }

        System.out.println(res);

        in.close();
    }
}

