import java.util.Scanner;

public class Main {

	public static final int BIG_NUM  = 2000000000;
	public static final int MOD  = 1000000007;

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int x = scanner.nextInt();
		int y = scanner.nextInt();

		System.out.println(gcd(Math.max(x, y),Math.min(x, y)));
	}

	public static int gcd(int a,int b){

		if(b == 0){
			return a;
		}else{
			return gcd(b,a%b);
		}
	}
}

