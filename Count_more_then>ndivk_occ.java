class Solution 
{
    //Function to find all elements in array that appear more than n/k times.
    public int countOccurence(int[] arr, int n, int k) 
    {
        // your code here,return the answer
        Map<Integer,Integer>map=new HashMap<>();
        int count=0;
        for(int i : arr){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        for(Map.Entry<Integer,Integer>i:map.entrySet()){
            if(i.getValue()>(n/k)){
                count++;
            }
        }
        return count;
    }
}
