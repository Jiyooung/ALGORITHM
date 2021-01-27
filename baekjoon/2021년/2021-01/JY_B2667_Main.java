/*
baekjoon 2667 : 색종이 만들기
solved by JY
DATE : 2021.01.22
DFS
*/
import java.io.BufferedReader;
// import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class JY_B2667_Main {
	static int N;
	static int[][] area;
	static int cnt = 0;
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	static ArrayList<Integer> ans = new ArrayList<Integer>();
	static int count = 0;
	public static void main(String[] args) throws IOException {
		// System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		area = new int[N][N];
		for (int i=0; i<N; i++) {
			String tmp = br.readLine().trim();
			for (int j=0; j<tmp.length(); j++) {
				area[i][j] = tmp.charAt(j) - '0';
			}
		}
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				if (area[i][j] == 1) {
					count = 0;
					cnt++;
					dfs(i, j, cnt+1);
					ans.add(count);
				}
			}
		}
		System.out.println(cnt);
        ans.sort(null);
		ans.forEach(i -> System.out.println(i));
	}
	public static void dfs(int y, int x, int num) {
		area[y][x] = num;
		count++;
		for (int i=0; i<4; i++) {
			int yy = y + dy[i];
			int xx = x + dx[i];
			
			if (yy >= 0 && yy < N && xx >= 0 && xx < N) {
				if (area[yy][xx] == 1) {
					dfs(yy, xx, num);
				}
			}
		}
	}
}
