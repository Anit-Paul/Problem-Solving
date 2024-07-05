class Solution
{
    public int[][] overlappedInterval(int[][] Intervals)
    {
        ArrayList<int[]>arr=new ArrayList<>();
        Arrays.sort(Intervals,new Comparator<int[]>() {
	            @Override
	            public int compare(int[] a, int[] b) {
	                return a[0]-b[0];
	            }
	        });
        if(Intervals.length<=1){
            return Intervals;
        }
        for(int i=0;i<Intervals.length;i++){
            if(arr.size()==0 || arr.get(arr.size()-1)[1]<Intervals[i][0]){
                arr.add(Intervals[i]);
            }
            else{
                arr.get(arr.size()-1)[1]=Math.max(arr.get(arr.size()-1)[1],Intervals[i][1]);
            }
        }
        int[][] ans=new int[arr.size()][2];
        for(int i=0;i<arr.size();i++){
            ans[i][0]=arr.get(i)[0];
            ans[i][1]=arr.get(i)[1];
        }
        return ans;
    }
}
