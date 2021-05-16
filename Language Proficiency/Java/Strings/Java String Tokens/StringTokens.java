import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        // Write your code here.
        scan.close();
        
        if (s.length() > 0) {
            String delimiters = "[ !,?._'@]+";
            String[] tokens = s.split(delimiters);
        
            System.out.println(tokens.length);
            for (int i = 0; i < tokens.length; i++) {
                System.out.println(tokens[i]);
            }
        } else {
            System.out.println(0);
        }
    }
}

