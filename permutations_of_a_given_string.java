class Solution {
    private static void compute_permutations(String s,String s1,int n,List<String> res){
        if(s1.length()==n){
            if(!res.contains(s1)){
                res.add(s1);
            }
            return;
        }
         for (int i = 0; i < s.length(); i++) {
            String newS1 = s1 + s.charAt(i);
            compute_permutations(s.substring(0, i) + s.substring(i + 1,n), newS1, n, res);
        }
    }
    public List<String> find_permutation(String s) {
        // Code here
        List<String>res=new ArrayList<>();
        int n=s.length();
        compute_permutations(s,"",n,res);
        Collections.sort(res);
        return res;
    }
}
