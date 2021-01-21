/*
jungol 1810 : 백설공주(Snow White)
solved by JY
DATE : 2020.01.21
재귀 사용
*/
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

// 재귀 사용
public class JY_J1810_2_Main {
    static int pick[] = new int[7];
    static int[] arr = new int[9];
    static boolean[] b = new boolean[9];
    static boolean find = false;
 
    public static void main(String[] args) throws NumberFormatException, IOException {
//      System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine().trim());
        }
 
        check(0, 0);
 
        for (int j = 0; j < 7; j++) {
            System.out.println(pick[j]);
        }
    }
 
    public static void check(int idx, int cnt) {
        if (cnt == 7) {
            int sum = 0, p = 0;
            for (int i = 0; i < idx; i++) {
                if (b[i]) {
                    sum += arr[i];
                    pick[p++] = arr[i];
                }
            }
            if (sum == 100) find = true;
        }
        if (idx == 9) return;
 
        b[idx] = true;
        check(idx + 1, cnt + 1);
        if (find) return;
 
        b[idx] = false;
        check(idx + 1, cnt);
        if (find) return;
    }
}