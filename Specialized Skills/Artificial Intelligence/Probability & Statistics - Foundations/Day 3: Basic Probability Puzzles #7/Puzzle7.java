import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        // P(a|d) = P(d|a)P(a) / P(d)
        //        = P(d|a)P(a) / (P(d|a)P(a) + P(d|b)P(b) + P(d|c)P(c))
        float pa = 1/7;
        float pb = 2/7;
        float pc = 4/7;
        float pda = 1/200;
        float pdb = 1/125;
        float pdc = 1/100;
        
        System.out.println("5/61");   
    }
}

