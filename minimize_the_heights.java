class Solution {
    int getMinDiff(int[] arr, int n, int k) {
        // code here
        Arrays.sort(arr);
        int small,large,ans;
        ans=arr[arr.length-1]-arr[0];
        small=arr[0]+k;
        large=arr[arr.length-1]-k;
        for(int i=0;i<arr.length-1;i++){
            int s=Math.min(small,arr[i+1]-k);
            int l=Math.max(large,arr[i]+k);
            if(s>=0){
                ans=Math.min(ans,l-s);
            }
        }
        return ans;
    }
}
