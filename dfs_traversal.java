package programs;
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;
class my_Graph{
	private int[][] matrix;
	private ArrayList<Character>color=new ArrayList<>();
	private int edge;
	my_Graph(int edge, int[][] matrix) {
        this.edge = edge;
        this.matrix = matrix;
        for(int i=0;i<edge;i++) {
        	color.add('w');
        }
    }
	public ArrayList<Integer> dfs(){
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
		for(int j=0;j<edge;j++) {
			if(color.get(j)=='w' && matrix[i][j]!=0) {
				visit(j,res);
			}
		}
		res.add(i);
	}
}
public class dfs_traversal {

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

        my_Graph graph = new my_Graph(edge, matrix);
        ArrayList<Integer> res = graph.dfs();
        System.out.println("the result of dfs traversal is");
		for(var i : res) {
			System.out.println(i);
		}
	}

}
