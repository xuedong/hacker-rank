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

    public static int sumDigits(int number) {
        int sum = 0;
        while(number > 0) {
            int digit = number % 10;
            sum = sum + digit;
            number = number / 10;  
        }
        return sum;
    }

    /*
     * Complete the 'canConstruct' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static String canConstruct(List<Integer> a) {
    // Return "Yes" or "No" denoting whether you can construct the required number.
        int total = 0;
        for (int number : a) {
            int sum = sumDigits(number);
            total += sum;
        }
        if (total % 3 == 0) return "Yes";
        return "No";
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                    .map(Integer::parseInt)
                    .collect(toList());

                String result = Result.canConstruct(a);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

