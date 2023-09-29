class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack1 =new Stack<Character>();
        for (char c : s.toCharArray()){
            if (c == '('){
                stack1.push(')');
            }
            else if (c == '['){
                stack1.push(']');
            }
            else if (c == '{'){
                stack1.push('}');
            }
            else if (stack1.isEmpty() || stack1.pop() != c){
                return false;
            }
        }
        if (stack1.isEmpty()){
            return true;
        }
        return false;
    }
}