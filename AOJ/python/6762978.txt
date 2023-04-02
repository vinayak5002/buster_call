import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		while (s.hasNext()) {
			int a = s.nextInt();
			int b = s.nextInt();
			int g = gcd(a, b);
			int l = lcm(a, b, g);
			System.out.println(g + " " + l);
		}
	}
	static int gcd(int a, int b) {
		int x = Math.max(a, b);
		int y = Math.min(a, b);
		int temp;
		while (y != 0) {
			temp = x % y;
			x = y;
			y = temp;
		}
		return x;
	}
	static int lcm(int a, int b, int g) {
		return a / g * b;
	}
}

