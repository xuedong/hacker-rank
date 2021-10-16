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

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = BigDecimal.valueOf(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return a DOUBLE_ARRAY.
     * The function accepts INTEGER_ARRAY y as parameter.
     */

    public static List<String> solve(List<Integer> y) {
    // Write your code here
        double res = 0;
        Collections.sort(y);
        int n = y.size();
        double current = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || (i > 0 && y.get(i) > y.get(i-1))) {
                double k = n-i;
                current = (n+1)/(k+1);
            }
            res += current;
        }
        List<String> list = new ArrayList<String>();
        list.add(String.format("%.2f", round(res, 2)));
        return list;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int yCount = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> y = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                    .map(Integer::parseInt)
                    .collect(toList());

                List<String> result = Result.solve(y);

                bufferedWriter.write(
                    result.stream()
                        .map(Object::toString)
                        .collect(joining("\n"))
                    + "\n"
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

