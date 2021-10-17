import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER a
     *  2. INTEGER b
     *  3. LONG_INTEGER t
     */

    public static int solve(int a, int b, long t) {
    // Write your code here
        if (t == 1) {
            return (int) ((a+b)/2);
        }
        return (int) modPow((a+b)/2, t);
    }
    
    public static long modPow(long n, long t) {
        long ans = 1;
        long mod = 1000000007;
        while (t > 0) {
            if (t % 2 == 1) {
                ans = (ans * n) % mod;
            }
            n = (n * n) % mod;
            t = t >> 1;
        }
        
        return ans;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int a = Integer.parseInt(firstMultipleInput[0]);

        int b = Integer.parseInt(firstMultipleInput[1]);

        long t = Long.parseLong(firstMultipleInput[2]);

        int result = Result.solve(a, b, t);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

