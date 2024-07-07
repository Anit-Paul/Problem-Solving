class Solution{
    private static int find_max(int a,int s,int N,int[] arr){
        int idx=s;
        for(int i=s;i<N;i++){
            if(arr[i]>a && arr[i]<=arr[idx]){
                idx=i;
            }
        }
        return idx;
    }
    private static void riverse(int[] arr,int s,int e){
        int i=s,j=e-1;
        while(i<j){
            int c=arr[i];
            arr[i]=arr[j];
            arr[j]=c;
            i++;
            j--;
        }
    }
    static List<Integer> nextPermutation(int N, int arr[]){
        List<Integer>res=new ArrayList<>();
        int i=N-1;
        while(i>0 && arr[i]<=arr[i-1]){
            i--;
        }
        int brk=i-1;
        if(i>0){
            int m=find_max(arr[brk],i,N,arr);
            //System.out.println(arr[m]);
            //System.out.println(arr[brk]);
            int c=arr[brk];
            arr[brk]=arr[m];
            arr[m]=c;
            riverse(arr,brk+1,N);
        }
        else{
            riverse(arr,0,N);
        }
        for(int j : arr){
            res.add(j);
        }
        return res;
    }
}
