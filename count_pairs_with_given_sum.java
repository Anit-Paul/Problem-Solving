class Solution {
    int getPairsCount(int[] arr, int sum) {
        // code here
        HashMap<Integer,Integer>map=new HashMap<>();
        int count=0;
        for(int i : arr){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        for(int i : arr){
            int rem=sum-i;
            if(map.containsKey(rem)){
                count+=map.get(rem);
            }
            if(i==rem){
                count--;
            }
        }
        return count/2;
    }
}
