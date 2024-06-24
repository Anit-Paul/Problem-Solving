import java.io.*;
import java.util.*;

public class solution {
    
    private static int maximum_number_of_unique_integers(int[] arr,int n,int m){
        if(m>n){
            return 0;
        }
        Queue<Integer> q=new LinkedList<Integer>();
        Set<Integer>set=new HashSet<Integer>();
        int back=m-1;
        for(int i=0;i<=back;i++){
            q.offer(arr[i]);
        }
        set.addAll(q);
        int max=set.size();
        for(int i=back+1;i<n;i++){
            int x=q.poll();
            q.offer(arr[i]);
            set.add(arr[i]);
            if(!q.contains(x)){
                set.remove(x);
            }
            if(max<set.size()){
                max=set.size();
            }
        }
        return max;
    }

    public static void main(String[] args) {
      int m,n;
      Scanner sc=new Scanner(System.in);
      n=sc.nextInt();//Array Size
      m=sc.nextInt();//Subarray Size
      int arr[]=new int[n];
      for(int i=0;i<n;i++){
          arr[i]=sc.nextInt();
      }
      int max=maximum_number_of_unique_integers(arr,n,m);
      System.out.println(max);
    }
}