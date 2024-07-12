class Solution {
    private static int get_first_idx(int[] arr,int x){
        int low=0,high=arr.length-1;
        int res=-1;
        while(low<=high){
            int mid=(low+high)/2;
            if(arr[mid]==x){
                res=mid;
                high=mid-1;
            }
            else if(arr[mid]<x){
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }
        return res;
    }
    int rowWithMax1s(int arr[][], int n, int m) {
        // code here
        int count=0,mr=-1;
        for(int i=0;i<n;i++){
            int idx=get_first_idx(arr[i],1);
            if(idx>=0){
                if(count<m-idx){
                    count=m-idx;
                    mr=i;
                }
            }
        }
        return mr;
    }
}
