import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double l = sc.nextDouble();
        double s1 = sc.nextDouble();
        double s2 = sc.nextDouble();

        int n = sc.nextInt();
        while (n-- > 0) {
            double query = sc.nextDouble();
            double result = Math.sqrt(2) * (l - Math.sqrt(query)) / Math.abs(s1-s2);
            System.out.println(result);
        }
    }
}

