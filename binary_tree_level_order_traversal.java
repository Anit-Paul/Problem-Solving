class Solution {
    private static List<List<Integer>> level_traverse(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        ArrayList<Integer> l = new ArrayList<>();
        if (root == null) {
            return res;
        }
        q.offer(root);
        q.offer(null);
        while (!q.isEmpty()) {
            TreeNode temp = q.poll();
            if (temp == null) {
                if (l.size() != 0) {
                    res.add(new ArrayList<>(l));
                }
                if (q.size() != 0) {
                    q.add(null);
                }
                l.clear();
            } else {
                l.add(temp.val);
                if (temp.left != null) {
                    q.add(temp.left);
                }
                if (temp.right != null) {
                    q.add(temp.right);
                }
            }
        }
        return res;
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        return level_traverse(root);
    }
}
