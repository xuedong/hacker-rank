import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
	public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String line = in.nextLine();
			
          	//Write your code here
            boolean flag = false;
            Pattern pattern = Pattern.compile("<(.+)>([^<>]+)</\\1>");
            Matcher matcher = pattern.matcher(line);
            
            while (matcher.find()) {
                System.out.println(matcher.group(2));
                flag = true;
            }
            if (!flag) {
                System.out.println("None");
            }
			
			testCases--;
		}
	}
}

