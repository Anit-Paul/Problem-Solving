package programs;
import java.util.*;
public class prims_algorithm {
	public static class Edge implements Comparable<Edge>{
		int src;
		int dst;
		int wt;
		Edge(int s,int d,int w){
			this.src=s;
			this.dst=d;
			this.wt=w;
		}
		@Override
		public int compareTo(Edge a) {
			return this.wt-a.wt;
		}
	}
	private static int compute_prims(int v,int[][] matrix) {
		PriorityQueue<Edge> pq=new PriorityQueue<>();
		ArrayList<Edge> arr=new ArrayList<>();
		pq.offer(new Edge(0,0,0));
		int[] visit=new int[v];
		for(int i=0;i<v;i++) {
			visit[i]=0;
		}
		int cost=0;
		while(!pq.isEmpty()) {
			Edge e=pq.poll();
			if(visit[e.dst]==0) {
				visit[e.dst]=1;
				cost+=e.wt;
				if(cost!=0) {
					arr.add(e);
				}
				for(int i=0;i<v;i++) {
					if(matrix[e.dst][i]>0 && visit[i]==0) {
						pq.offer(new Edge(e.dst,i,matrix[e.dst][i]));
						
					}
				}
			}
		}
		System.out.println("the edges are ");
		for(var i : arr) {
			System.out.println(i.src+" - "+i.dst);
		}
		return cost;
	}
	public static void main(String[] args) {
		int v;
		int e;
		int s,d;
		Scanner sc=new Scanner(System.in);
		System.out.print("no of vertices : ");
		v=sc.nextInt();
		System.out.print("no of edges : ");
		e=sc.nextInt();
		int[][] matrix=new int[v][v];
		for(int i=0;i<v;i++) {
			for(int j=0;j<v;j++) {
				matrix[i][j]=0;
			}
		}
		for(int i=0;i<e;i++) {
			System.out.print("source : ");
			s=sc.nextInt();
			System.out.print("destination : ");
			d=sc.nextInt();
			System.out.print("weight : ");
			int wt=sc.nextInt();
			matrix[s][d]=wt;
			matrix[d][s]=wt;
		}
		int cost=compute_prims(v,matrix);
		System.out.println("the cost of the mst is "+cost);
	}

}
