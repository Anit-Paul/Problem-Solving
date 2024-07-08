class Solution {
    // Function to find maximum product subarray
    
    long maxProduct(int[] arr, int n) {
        // code here
        long max=Integer.MIN_VALUE;
        long suf=1;
        for(int i=0;i<n;i++){
            suf*=arr[i];
            if(max<suf){
                max=suf;
            }
            if(suf==0){
                suf=1;
            }
        }
            suf=1;
            for(int i=n-1;i>=0;i--){
                suf*=arr[i];
                if(max<suf){
                    max=suf;
                }
                if(suf==0){
                    suf=1;
                }
                //System.out.println(suf);
            }
        
        return max;
    }
}
