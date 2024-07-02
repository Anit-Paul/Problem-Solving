class Solution {
    
     private static void get_paths(int i, int j, String s, int[][] visit, int n, int[][] m, ArrayList<String> arr) {
    
        if (m[i][j] == 0 || visit[i][j] == 1) {
            return;
        }
        visit[i][j] = 1;
        if (i == n - 1 && j == n - 1) {
            if(!arr.contains(s)){
                arr.add(s);
            }
            visit[i][j]=0;
            return;
        }
        //Move Up
        if (i > 0) {
            get_paths(i - 1, j, s + 'U', visit, n, m,arr);
        }
        // Move down
        if (i < n - 1) {
            get_paths(i + 1, j, s + 'D', visit, n, m,arr);
        }
        // Move left
        if (j > 0) {
            get_paths(i, j - 1, s + 'L', visit, n, m,arr);
        }
        // Move right
        if (j < n - 1) {
            get_paths(i, j + 1, s + 'R', visit, n, m,arr);
        }

        visit[i][j] = 0;
    }
    public static ArrayList<String> findPath(int[][] m, int n) {
         ArrayList<String> arr=new ArrayList<>();
        int[][] visit=new int[n][n];
        get_paths(0,0,"",visit,n,m,arr);
        return arr;
    }
}
