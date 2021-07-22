import java.util.Scanner;

public class SameDifference {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int n = s.nextInt();

        int count;
        int[] arr ;
        for (int i = 0; i < n; i++) {
            int arrSize = s.nextInt();
            arr = new int[arrSize];
            count = 0;
            for(int j = 0; j < arrSize; j++ ){
                arr[j] = s.nextInt();
            }
            int x = 0;
            for(int k = 0; k < arrSize; k++){
                for( int l = x; l < arrSize; l++){
                    if(k < l && (arr[l] - arr[k] == l - k) || l < k && (arr[k] - arr[l] == k - l)){
                        count++;
                    }
                }
                x++;
            }
            System.out.println(count);
        }
    }
}