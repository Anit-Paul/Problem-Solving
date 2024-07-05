class Solution
{
    //Function to merge the arrays.
    public static void merge(long arr1[], long arr2[], int n, int m) 
    {
        // code here 
        int p1=n-1;
        int p2=0;
        while(p1>=0 && p2<m){
            if(arr1[p1]>arr2[p2]){
                long c=arr1[p1];
                arr1[p1]=arr2[p2];
                arr2[p2]=c;
                p1--;
                p2++;
            }
            else{
                break;
            }
        }
        Arrays.sort(arr1);
        Arrays.sort(arr2);
    }
}
