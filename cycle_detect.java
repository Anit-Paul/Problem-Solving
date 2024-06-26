class Solution {
      private boolean dfs(int i, int v, ArrayList<ArrayList<Integer>> adj, ArrayList<Integer> res, ArrayList<Integer> visit) {
        res.set(i, 1);
        visit.set(i, 1);
        for (int neighbor : adj.get(i)) {
            if (res.get(neighbor) == 1) {
                return true;
            } else if (visit.get(neighbor) == 0) {
                if (dfs(neighbor, v, adj, res, visit)) {
                    return true;
                }
            }
        }
        res.set(i, 0);
        return false;
    }
    public boolean isCyclic(int v, ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Integer> visit = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            res.add(0);
            visit.add(0);
        }

        for (int i = 0; i < v; i++) {
            if (visit.get(i) == 0) {
                if (dfs(i, v, adj, res, visit)) {
                    return true;
                }
            }
        }
        return false;
    }
}
