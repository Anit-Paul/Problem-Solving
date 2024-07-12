class Solution
{
    //Function to return a list of integers denoting spiral traversal of matrix.
    static ArrayList<Integer> spirallyTraverse(int arr[][], int r, int c)
    {
        // code here
        int top=0;
        int right=c-1;
        int bottom=r-1;
        int left=0;
        ArrayList<Integer>res=new ArrayList<>();
        while(left<=right && top<=bottom){
            if(top<=bottom){
                for(int i=left;i<=right;i++){
                res.add(arr[top][i]);
                }
                top++;
            }
            if(left<=right){
                    for(int i=top;i<=bottom;i++){
                res.add(arr[i][right]);
            }
            right--;
            }
            if(top<=bottom){
                for(int i=right;i>=left;i--){
                res.add(arr[bottom][i]);
            }
            bottom--;
            }
            if(right>=left){
                for(int i=bottom;i>=top;i--){
                res.add(arr[i][left]);
            }
            left++;
            }
        }
        return res;
    }
}
