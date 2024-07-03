class Solution
{
    public static void sort012(int a[], int n)
    {
        // code here 
        int low=0,high=n-1,mid=0,c;
        while(mid<=high){
            if(a[mid]==0){
                c=a[mid];
                a[mid]=a[low];
                a[low]=c;
                mid++;
                low++;
            }
            else if(a[mid]==1){
                mid++;
            }
            else{
                c=a[mid];
                a[mid]=a[high];
                a[high]=c;
                high--;
                
            }
            
        }
    }
}
