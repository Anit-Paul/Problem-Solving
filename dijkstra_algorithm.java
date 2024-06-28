package programs;
import java.util.*;

public class dijkstra_algorithm {
	public static class Pair implements Comparable<Pair>{
		int node;
		int dist;
		public Pair(int n,int d) {
			this.node=n;
			this.dist=d;
		}
		@Override
		public int compareTo(Pair p) {
			return this.dist-p.dist;//asc order
		}
	}
	private static int[] compute_dijkstra(int[][] matrix,int v,int src) {
		int[] dist=new int[v];
		dist[src]=0;
		for(int i=0;i<v;i++) {
			if(i!=src) {
				dist[i]=Integer.MAX_VALUE;
			}
		}
		boolean[] visit=new boolean[v];
		PriorityQueue<Pair>pq=new PriorityQueue<>();
		pq.offer(new Pair(src,dist[src]));
		while(!pq.isEmpty()) {
			Pair cur=pq.poll();
			if(!visit[cur.node]) {
				visit[cur.node]=true;
				for(int i=0;i<v;i++) {
					if(matrix[cur.node][i]>0) {
						int u=cur.node;
						int v1=i;
						//relaxation
						if(dist[v1]>dist[u]+matrix[u][v1]) {
							dist[v1]=dist[u]+matrix[u][v1];
							pq.offer(new Pair(v1,dist[v1]));
						}
					}
				}
			}
				
		}
		return dist;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int v;
		System.out.print("no of vertices : ");
		v=sc.nextInt();
		System.out.println("enter the graph ");
		int[][] matrix=new int[v][v];
		for(int i=0;i<v;i++) {
			for(int j=0;j<v;j++) {
				matrix[i][j]=sc.nextInt();
			}
		}
		int source;
		System.out.print("enter the source : ");
		source=sc.nextInt();
		int[] res=compute_dijkstra(matrix,v,source);
		for(int i : res) {
			System.out.println(i);
		}
	}
}
//in the Pair class, we use the Comparable interface to enable natural ordering of Pair objects based on their dist field. This is essential for using the Pair objects in a PriorityQueue, which relies on the natural ordering to function correctly.
