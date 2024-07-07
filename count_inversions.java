class Solution {
    // arr[]: Input Array
    // N : Size of the Array arr[]
    // Function to count inversions in the array.
    public static long count;
    private static void merge(long[] arr,int low,int mid,int high,long[] b){
        int i=low,j=mid+1;
        
        int k=low;
        while(i<=mid && j<=high){
            if(arr[i]>arr[j]){
                count+=(mid-i)+1;
                b[k++]=arr[j++];
            }
            else{
                b[k++]=arr[i++];
            }
        }
        while(i<=mid){
            b[k++]=arr[i++];
        }
        while(j<=high){
            b[k++]=arr[j++];
        }
        for(k=low;k<=high;k++){
            arr[k]=b[k];
        }
    }
    private static void merge_sort(long[] arr,int low,int high,long[] b){
        int mid;
        if(low<high){
            mid=(low+high)/2;
            merge_sort(arr,low,mid,b);
            merge_sort(arr,mid+1,high,b);
            merge(arr,low,mid,high,b);
        }
    }
    static long inversionCount(long arr[], int n) {
        // Your Code Here
        count=0;
        long[] b=new long[n];
        merge_sort(arr,0,n-1,b);
        return count;
    }
}
