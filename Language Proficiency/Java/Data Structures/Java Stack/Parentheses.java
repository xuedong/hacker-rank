import java.util.*;

class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input = sc.next();
            //Complete the code
            Stack<Character> stack = new Stack<>();
            
            if (input == "") {
                System.out.println("true");
                continue;
            }
            
            int length = input.length();
            int n = 0;
            char ch = input.charAt(n);
            if (ch == ')' || ch == '}' || ch == ']') {
                System.out.println("false");
                continue;
            }
            
            stack.push(ch);
            boolean flag = true;
            while (n < length-1) {
                n++;
                
                ch = input.charAt(n);
                if (ch == '(' || ch == '[' || ch == '{') {
                    stack.push(ch);
                    continue;
                }
                if (stack.isEmpty()) {
                    if (ch == '}' || ch == ')' || ch == ']') {
                        flag = false;
                        break;
                    }
                }
                
                char p = stack.peek();
                if (p == '{' && ch == '}' || p == '(' && ch == ')' || p == '[' && ch == ']') {
                    stack.pop();
                } else {
                    flag = false;
                    break;
                }
            }
            if (!flag) {
                System.out.println("false");
                continue;
            }
            
            if (stack.isEmpty()) {
                System.out.println("true");
                continue;
            }
            System.out.println("false");
		}
	}
}

