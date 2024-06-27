class Solution {
    private static void refresh(int n,int[] visit,int[] parent){
        for(int i=0;i<n;i++){
            visit[i]=0;
            parent[i]=-1;
        }
    }
    private static boolean dfs(int i,ArrayList<ArrayList<Integer>> adj,int[]visit,int[]parent,int v){
        visit[i]=1;
        ArrayList<Integer>arr=new ArrayList<>();
        arr=adj.get(i);
        for(var j : arr){
            if(visit[j]==1 && parent[i]!=j){
                return true;
            }
            else if(visit[j]==0){
                parent[j]=i;
                if(dfs(j,adj,visit,parent,v)){
                    return true;
                }
            }
        }
        return false;
    }
    // Function to detect cycle in an undirected graph.
    public boolean isCycle(int v, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        int[] parent=new int[v];
        int[] visit=new int[v];
        refresh(v, visit, parent);
        for (int i = 0; i < v; i++) {
            if (visit[i] == 0) {  
                if (dfs(i, adj, visit, parent,v)) {
                    return true;
                }
            }
        }
        return false;
    }
}
