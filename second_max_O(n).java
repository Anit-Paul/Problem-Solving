package programs;
import java.util.Scanner;
public class second_max {
	private static int get_max(int[] arr,int size) {
		int max=arr[0];
		int s_max=arr[0];
		for(int i=1;i<size;i++) {
			if(arr[i]>max) {
				s_max=max;
				max=arr[i];
			}
			else if(arr[i]<max && arr[i]>s_max) {
				s_max=arr[i];
			}
		}
		return s_max;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int size;
		System.out.println("array size : ");
		size=sc.nextInt();
		int[] arr=new int[size];
		for(int i=0;i<size;i++) {
			arr[i]=sc.nextInt();
		}
		int max=get_max(arr,size);
		System.out.println("the 2nd max is : "+max);
	}

}
