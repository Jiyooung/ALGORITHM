/*
jungol 1328 : 빌딩
solved by JY
DATE : 2021.01.21
Stack 사용
*/
import java.io.BufferedReader;
// import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
public class JY_J1328_Main {
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        //System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        int N = Integer.parseInt(br.readLine().trim());
        Stack<Integer> s = new Stack<Integer>();
         
        int[] ans = new int[N];
        int[] arr = new int[N];
         
        for (int i=0; i<N; ++i) {
            arr[i] = Integer.parseInt(br.readLine().trim());
        }
         
        ans[N-1] = 0;
        s.push(N-1);
         
        for(int i=N-2;i>=0;--i) {
            while(!s.isEmpty() && arr[i] >= arr[s.peek()]) {
                s.pop();
            }
            if(!s.isEmpty()) ans[i] = s.peek()+1;
            else ans[i] = 0;
            s.push(i);
        }
         
        StringBuilder sb = new StringBuilder();
         
        for (int data:ans) {
//          System.out.println(data);
            sb.append(data).append("\n");
        }
        System.out.println(sb.toString());
         
        br.close();
    }
}