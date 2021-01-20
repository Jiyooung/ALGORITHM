import java.util.Scanner;
import java.io.FileInputStream;

public class JY_2072 {
    public static void main(String args[]) throws Exception{
        // System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
         
        int T = sc.nextInt();
         
        for (int i=0; i<T; i++) {
            int answer = 0;
            for (int j=0; j<10; j++) {
                int num = sc.nextInt();
                if (num % 2 == 1) {
                    answer += num;
                }
            }
            System.out.printf("#%d %d\n", i+1, answer);         
        }
    }
}