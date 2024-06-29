package programs;
import java.util.*;

public class bellmanford {
  public static class edge implements Comparable<edge>{
		public int src;
		public int dest;
		public int wt;
		edge(int src,int dest,int wt){
			this.src=src;
			this.dest=dest;
			this.wt=wt;
		}
		@Override
		public int compareTo(edge a) {
			return this.src-a.src;
		}
		
	}
	public static boolean compute_bellmanford(ArrayList<edge> graph,int v) {
		int[] d=new int[v];
		for(int i=0;i<v;i++) {
			d[i]=Integer.MAX_VALUE;
		}
		d[0]=0;
		Collections.sort(graph);
		for(int i=1;i<=v-1;i++) {
			for(var e : graph) {
				if(d[e.dest]>d[e.src]+e.wt) {
					d[e.dest]=d[e.src]+e.wt;
				}
			}
		}
		for(var e : graph) {
			if(d[e.dest]>d[e.src]+e.wt) {
				return true;
			}
		}
		for(int i : d) {
			System.out.println(i);
		}
		return false;
	}
	public static void main(String[] args) {
		ArrayList<edge> graph=new ArrayList<>();
		int v;
		Scanner sc=new Scanner(System.in);
		System.out.print("no. of vertices : ");
		v=sc.nextInt();
		System.out.print("no. of edges : ");
		int e=sc.nextInt();
		for(int i=0;i<e;i++) {
			System.out.print("source ");
			int s=sc.nextInt();
			System.out.print("dest:");
			int	d=sc.nextInt();
			System.out.print("weight : ");
			int w=sc.nextInt();
			edge a=new edge(s,d,w);
			graph.add(a);
		}
		boolean res=compute_bellmanford(graph,v);
		if(res) {
			System.out.println("-ve weight cycle present");
		}
	}

}
