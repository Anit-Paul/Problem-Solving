package programs;
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;
class Graph{
	private int[][] matrix;
	private Queue<Integer> q=new LinkedList<>();
	private ArrayList<Character>color=new ArrayList<>();
	private int edge;
	Graph(int edge, int[][] matrix) {
        this.edge = edge;
        this.matrix = matrix;
        for (int i = 0; i < edge; i++) {
            color.add('w');
        }
    }
	public ArrayList<Integer> bfs(){
		ArrayList<Integer> res=new ArrayList<>();
		for(int i=0;i<edge;i++) {
			if(color.get(i)=='w') {
				visit(i,res);
			}
		}
		return res;
	}
	private void visit(int i,ArrayList<Integer>res) {
		color.set(i, 'g');
		q.offer(i);
		while(!q.isEmpty()) {
			int x=q.poll();
			for(int j=0;j<edge;j++) {
				if(matrix[x][j]!=0 && color.get(j)=='w') {
					q.offer(j);
					color.set(j, 'g');
				}
			}
			color.set(x, 'b');
			res.add(x);
		}
	}
}
public class bfs_traversal {

	public static void main(String[] args) {
		int edge;
		System.out.print("no of edges : ");
		Scanner sc=new Scanner(System.in);
		edge=sc.nextInt();
		int[][] matrix = new int[edge][edge];
        System.out.println("Enter the adjacency matrix:");
        for (int i = 0; i < edge; i++) {
            for (int j = 0; j < edge; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        Graph graph = new Graph(edge, matrix);
        ArrayList<Integer> res = graph.bfs();
        System.out.println("the result of bfs traversal is");
		for(var i : res) {
			System.out.println(i);
		}
	}

}
