import java.util.*;
import java.lang.*;
import java.io.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int S = sc.nextInt();
		System.out.println(S / 3600 + ":" + (S / 60) % 60 + ":" + S % 60);
	}
}
