class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        List<Integer> result = new ArrayList<>();
        boolean[] incomingEdges = new boolean[n]; 

        for (List<Integer> edge : edges) {
            incomingEdges[edge.get(1)] = true; 
        }

        for (int i = 0; i < n; i++) {
            if (!incomingEdges[i]) {
                result.add(i);
            }
        }

        return result;
    }
}
