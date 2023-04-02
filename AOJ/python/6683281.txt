import java.util.*;
import java.io.*;
 
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        int n = Integer.parseInt(br.readLine());
 
        LinkedList<Integer> list = new LinkedList<Integer>();
 
        for (int i=0; i<n; i++) {
            String str = br.readLine();
 
            if (str.startsWith("insert")) {
                list.addFirst(Integer.parseInt(str.substring(str.indexOf(" ")+1)));
            }else if (str.equals("deleteFirst")) {
                list.pollFirst();
            }else if (str.equals("deleteLast")){
                list.pollLast();
            }else {
                list.remove((Integer)Integer.parseInt(str.substring(str.indexOf(" ")+1)));
            }
        }
 
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        sb.append(list.poll());
        for (Integer s : list) {
            sb.append(" ");
            sb.append(s);
        }
        bw.write(sb.toString());
        bw.newLine();
        bw.close();
 
        br.close();
    }
}
