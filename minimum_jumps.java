class Solution {
    static int minJumps(int[] arr, int n) {
        // your code here
        if(n==0 || n==1){
            return 0;
        }
        int max=0,maxvalue=0,jump=0;;
        for(int i=0;i<n;i++){
            max=Math.max(max,i+arr[i]);
            if(i==maxvalue){
                maxvalue=max;
                jump++;
                if(maxvalue>=n-1){
                    return jump;
                }
            }
        }
        return -1;
    }
}
