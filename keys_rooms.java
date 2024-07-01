class Solution {
    private static void dfs(int i,List<List<Integer>> rooms,int[] visit){
        visit[i]=1;
        List<Integer>arr=new ArrayList(rooms.get(i));
        for(int e:arr){
            if(visit[e]==0){
                 dfs(e,rooms,visit);
            }
        }
    }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int[] visit=new int[rooms.size()];
        for(int i=0;i<visit.length;i++){
            visit[i]=0;
        }
        dfs(0,rooms,visit);
        for(int i:visit){
            if(i==0){
                return false;
            }
        }
        return true;
    }
}
