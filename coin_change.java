class Solution {
    public static long get_combinations(int idx,int[] arr,int sum,long[][] help) {
		if(idx==0) {
			return (sum%arr[0]==0)?1:0;
		}
		if(help[idx][sum]!=-1) {
			return help[idx][sum];
		}
		long notake=get_combinations(idx-1,arr,sum,help);
		long take=0;
		if(arr[idx]<=sum) {
			take=get_combinations(idx,arr,sum-arr[idx],help);
		}
		return help[idx][sum]=notake+take;
	}
    public long count(int arr[], int N, int sum) {
        // code here.
        long[][] help=new long[arr.length][sum+1];
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<=sum;j++) {
				help[i][j]=-1;
			}
		}
		return get_combinations(arr.length-1,arr,sum,help);
    }
}
