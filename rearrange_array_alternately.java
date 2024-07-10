class Solution{
    
    // temp: input array
    // n: size of array
    //Function to rearrange  the array elements alternately.
    public static void rearrange(long arr[], int n){
        
        // Your code here
        int min_idx=0;
        int max_idx=n-1;
        long max=arr[max_idx]+1;
        for(int i=0;i<n;i++){
            if((i&1)==0){
                arr[i]=(arr[max_idx--]%max)*max+arr[i];
            }
            else{
                arr[i]=(arr[min_idx++]%max)*max+arr[i];
            }
        }
        for(int i=0;i<n;i++){
            arr[i]/=max;
        }
    }
    
}
