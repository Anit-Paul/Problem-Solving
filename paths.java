class Solution {
    private void dfs(int i,List<Integer>arr, List<List<Integer>>res,int n,int[][] graph){
       if(i==n){
            res.add(new ArrayList<>(arr));
            return;
        }
        else{
            for(int j=0;j<graph[i].length;j++){
                arr.add(graph[i][j]);
                dfs(graph[i][j],arr,res,n,graph);
                arr.remove(arr.size()-1);
            }
        }
    }
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n=graph.length-1;
        List<List<Integer>>res=new ArrayList<>();
        List<Integer>arr=new ArrayList<>();
        arr.add(0);
        dfs(0,arr,res,n,graph);
        return res;
    }
}
