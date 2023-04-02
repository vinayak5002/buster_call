import java.util.Scanner;

public class Main {

	public static final int BIG_NUM  = 2000000000;
	public static final int MOD  = 1000000007;

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();

		int array[] = new int[N];
		for(int i = 0; i < N; i++)array[i] = scanner.nextInt();

		out_put(array);

		int base_value,loc;
		for(int i = 1; i < N; i++){
			base_value = array[i];
			loc = i-1;
			while(loc >= 0 && array[loc] > base_value){
				array[loc+1] = array[loc];
				loc--;
			}
			array[loc+1] = base_value;

			out_put(array);
		}
	}

	private static void out_put(int array[]){

		System.out.printf("%d", array[0]);

		for(int i = 1; i < array.length; i++){
			System.out.printf(" %d", array[i]);
		}
		System.out.printf("\n");
	}
}

