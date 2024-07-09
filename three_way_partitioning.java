class Solution{
    //Function to partition the array around the range such 
    //that array is divided into three parts.
    public static void swap(int[] a,int i,int j){
        int c=a[i];
        a[i]=a[j];
        a[j]=c;
    }
    public void threeWayPartition(int array[], int a, int b)
    {
        // code here 
        int low=0,mid=0,high=array.length-1;
        while(mid<=high && mid<array.length){
            if(array[mid]<a){
                swap(array,low,mid);
                low++;
                mid++;
            }
            else if(array[mid]>b){
                swap(array,mid,high);
                high--;
            }
            else{
                mid++;
            }
        }
    }
}
