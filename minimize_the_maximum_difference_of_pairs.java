class Solution {
    private int helper(int[] nums,int dif,int p){
        int i=1,count=0;
        while(i<nums.length){

            if(nums[i]-nums[i-1]<=dif){
                count++;
                i++;
            }
            i++;
            if(count==p){
                return count;
            }
        }
        return count;
    }
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        int l=0,r=nums[nums.length-1]-nums[0];
        while(l<r){
            
            int mid=(l+r)/2;
            if(helper(nums,mid,p)>=p){
                r=mid;
            }
            else{
                l=mid+1;
            }
           
        }
        return l;
    }
}
