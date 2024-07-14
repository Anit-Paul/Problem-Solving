class Tree {
    ArrayList<Integer> postOrder(Node root) {
        // code here
        ArrayList<Integer>res=new ArrayList<>();
        Stack<Node>st=new Stack<>();
        while(true){
            while(root!=null){
                if(root.right!=null){
                    st.push(root.right);
                }
                st.push(root);
                root=root.left;
            }
            if(st.isEmpty()){
                break;
            }
           root = st.pop();

            if (!st.isEmpty() && root.right == st.peek()) {
                Node temp = st.pop();
                st.push(root);
                root = temp;
            } else {
                res.add(root.data);
                root = null;
            }
        
        }
        return res;
    }
}
