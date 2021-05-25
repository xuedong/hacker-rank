import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> lines = new ArrayList<>();
        
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int d = sc.nextInt();
            ArrayList<Integer> line = new ArrayList<>();
            
            for (int j = 1; j <= d; j++) {
                line.add(sc.nextInt());
            }
            
            lines.add(line);
        }
        
        int q = sc.nextInt();
        for (int i = 1; i <= q; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            try {
                System.out.println(lines.get(x-1).get(y-1));
            } catch (Exception e) {
                System.out.println("ERROR!");
            }
        }
        
        sc.close();
    }
}

