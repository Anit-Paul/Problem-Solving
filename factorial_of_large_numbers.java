import java.math.BigInteger;
class Solution {
    static ArrayList<Integer> factorial(int N) {
        // code here
        ArrayList<Integer>res=new ArrayList<>();
        BigInteger fact=BigInteger.ONE;
        for(int i=1;i<=N;i++){
            fact=fact.multiply(BigInteger.valueOf(i));
        }
        String s=""+fact;
        for(int i=0;i<s.length();i++){
            int a=s.charAt(i)-'0';
            res.add(a);
        }
        return res;
    }
}
