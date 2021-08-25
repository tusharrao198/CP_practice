import java.util.Scanner;
public class OrdinaryNumber {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int count;
        for(int i = 0; i<n; i++){
            int inputNo = s.nextInt();
            count = 0;
            for(int j = 1; j <= inputNo; j++){
                String inputNoStr = String.valueOf(j);
                if(inputNoStr.matches("(.)\\1+") || inputNoStr.length()==1){
                   count++;
                }
            }
            System.out.println(count);
        }
    }
}