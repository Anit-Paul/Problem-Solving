class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int c=0;
        for(int i : arr){
            if((i&1)==0){
                c=0;
            }
            else{
                c++;
            }
            if(c==3){
                return true;
            }
        }
        return false;
    }
}
