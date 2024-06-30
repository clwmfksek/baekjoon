import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = 0;
        for(int i=1;i<N+1;i++){
            int[] arrNum = Stream.of(String.valueOf(i).split("")).mapToInt(Integer::parseInt).toArray();
            if(arrNum.length==1){
                C += 1;
            }else{
                if(arrNum[1]-arrNum[0] == arrNum[arrNum.length-1] - arrNum[arrNum.length-2]){
                    C += 1;
                }
            }
            }
        System.out.println(C);
        }
    }