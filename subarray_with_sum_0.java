class Solution{
    //Function to check whether there is a subarray present with 0-sum or not.
    static boolean findsum(int arr[],int n)
    {
        //Your code here
        HashMap<Integer,Integer>map=new HashMap<>();
        map.put(0,1);
        int sum=0;
        for(int i : arr){
            sum=sum+i;
            if(!map.containsKey(sum)){
                map.put(sum,1);
            }
            else{
                return true;
            }
        }
        return false;
    }
}
