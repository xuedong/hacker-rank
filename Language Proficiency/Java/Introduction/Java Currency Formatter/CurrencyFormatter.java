import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        Locale indiaLocale = new Locale("en", "IN");

        // Write your code here.
        NumberFormat usNF = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usNF.format(payment);
        NumberFormat indiaNF = NumberFormat.getCurrencyInstance(indiaLocale);
        String india = indiaNF.format(payment);
        NumberFormat chinaNF = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chinaNF.format(payment);
        NumberFormat franceNF = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = franceNF.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}

