class Solution{
    //Function to find the days of buying and selling stock for max profit.
    ArrayList<ArrayList<Integer> > stockBuySell(int a[], int n) {
        // code here
        ArrayList<ArrayList<Integer>> res=new ArrayList<>();
        int i=0;
        while(i<n-1){
            //find the local minima
            while(i<n-1 && a[i]>=a[i+1]){
                i++;
            }
            if(i==n-1){
                break;
            }
            int buy=i;
            i++;
            //find the local maxima
            while(i<n && a[i]>=a[i-1]){
                i++;
            }
            int sell=i-1;
            ArrayList<Integer>newlist=new ArrayList<>();
            newlist.add(buy);
            newlist.add(sell);
            res.add(new ArrayList<>(newlist));
        }
         return res;
    }
   
}
