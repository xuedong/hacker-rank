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
     * The function is expected to return a DOUBLE.
     * The function accepts INTEGER_ARRAY P as parameter.
     */
    public static long factorial(int number) {
        long result = 1;

        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }

        return result;
    }

    public static double solve(List<Integer> P) {
    // Write your code here
        List<Integer> sortedP = P.stream().sorted().collect(Collectors.toList());
        if (P.equals(sortedP)) return 0;
        
        int n = P.size();
        double result = factorial(n);
        
        int current = sortedP.get(0);
        int count = 1;
        for (int i = 1; i < n; i++) {
            if (sortedP.get(i) == current) {
                count += 1;
            } else {
                result /= factorial(count);
                count = 1;
                current = sortedP.get(i);
            }
        }
        if (count > 1) {
            result /= factorial(count);
        }
        
        return result;
    }
}


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int PCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> P = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        double result = Result.solve(P);
        DecimalFormat df = new DecimalFormat("#.######");

        bufferedWriter.write(df.format(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

