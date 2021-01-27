/*
jungol 1335 : 색종이 만들기(영역구분)
solved by JY
DATE : 2021.01.22
DFS
*/
// import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class JY_J1335_Main {
	static int[] answer = {0, 0};
	public static void main(String[] args) throws NumberFormatException, IOException {
//		System.setIn(new FileInputStream("input.txt"));
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int [][] paper = new int[N][N];
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				paper[i][j] = sc.nextInt();
			}
		}
		
		int s_y = 0, s_x = 0, e_y = N-1, e_x = N-1;
		divide(paper, s_y, s_x, e_y, e_x, N);
		System.out.printf("%d\n%d", answer[0], answer[1]);
	}
	
	public static void divide(int[][] paper, int s_y, int s_x, int e_y, int e_x, int N) {
		int ret = check(paper, s_y, s_x, e_y, e_x);
		if (ret != -1) {
			answer[ret]++;
			return ;
		}
		
		divide(paper, s_y	 	, s_x		, e_y - N/2	, e_x - N/2	, N/2);
		divide(paper, s_y	 	, s_x + N/2	, e_y - N/2	, e_x		, N/2);
		divide(paper, s_y + N/2	, s_x		, e_y		, e_x - N/2	, N/2);
		divide(paper, s_y + N/2 , s_x + N/2	, e_y		, e_x		, N/2);
	}

	public static int check(int[][] paper, int s_y, int s_x, int e_y, int e_x) {
		int color = paper[s_y][s_x];
		for(int i=s_y; i<=e_y; i++) {
			for (int j=s_x; j<=e_x; j++) {
				if (paper[i][j] != color) return -1;
			}
		}
		return color;
	}
}
