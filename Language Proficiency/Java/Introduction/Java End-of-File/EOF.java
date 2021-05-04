import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int index = 0;
        
        while (sc.hasNext()) {
            index++;
            String line = sc.nextLine();
            System.out.printf("%d %s%n", index, line);
        }
    }
}

