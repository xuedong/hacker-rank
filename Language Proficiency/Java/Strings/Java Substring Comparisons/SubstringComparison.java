import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        int len = s.length();
        if (len < k) return "" + "\n" + "";
        
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        for (int i = 0; i <= len-k; i++) {
            String curr = s.substring(i, i+k);
            if (curr.compareTo(smallest) < 0) {
                smallest = curr;
                continue;
            }
            if (curr.compareTo(largest) > 0) {
                largest = curr;
                continue;
            }
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}

