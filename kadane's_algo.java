class Solution {

    // arr: input array
    // Function to find the sum of contiguous subarray with maximum sum.
    long maxSubarraySum(int[] arr) {

        // Your code here
        int cur=0;
        int max=arr[0];
        for(int i=0;i<arr.length;i++){
            cur=cur+arr[i];
            if(max<cur){
                max=cur;
            }
            if(cur<0){
                cur=0;
            }
        }
        return max;
    }
}
