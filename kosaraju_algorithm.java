package programs;
import java.util.*;
public class kosaraju_algorithm {
	private static Stack<Integer> st=new Stack<>();
	private static ArrayList<Integer> res=new ArrayList<>();
	private static ArrayList<ArrayList<Integer>> arr=new ArrayList<>();
	private static void dfs(int i,int v,int[][] matrix,int[] visit) {
		visit[i]=1;
		res.add(i);
		for(int j=0;j<v;j++) {
			if(visit[j]==0 && matrix[i][j]>0) {
				dfs(j,v,matrix,visit);
			}
		}
		st.push(i);
	}
	private static void refresh(int v,int[] visit) {
		for(int i=0;i<v;i++) {
			visit[i]=0;
		}
	}
	private static int compute_kosaraju(int v,int[][] matrix) {
		int[] visit=new int[v];
		refresh(v,visit);
		//getting the stack after performing tropological sort
		for(int i=0;i<v;i++) {
			if(visit[i]==0) {
				dfs(i,v,matrix,visit);
			}
		}
		//transpose of the matrix
		for(int i=0;i<v;i++) {
			for(int j=i+1;j<v;j++) {
				int c=matrix[i][j];
				matrix[i][j]=matrix[j][i];
				matrix[j][i]=c;
			}
		}
		//compute dfs with stack
		refresh(v,visit);
		int count=0;
		while(!st.isEmpty()) {
			int i=st.pop();
			if(visit[i]==0) {
				res.clear();
				dfs(i,v,matrix,visit);
				count++;
				arr.add(new ArrayList(res));
				
			}
		}
		return count;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int v;
		System.out.print("no of vertices : ");
		v=sc.nextInt();
		int[][] matrix=new int[v][v];
		System.out.println("the graph matrix : ");
		for(int i=0;i<v;i++) {
			for(int j=0;j<v;j++) {
				matrix[i][j]=sc.nextInt();
			}
		}
		int res=compute_kosaraju(v,matrix);
		for(var i : arr) {
			System.out.println(i);
		}
		System.out.println("no of strongly connected components are "+res);
	}

}
