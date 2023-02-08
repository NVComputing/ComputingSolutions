import java.util.Scanner;
import java.util.ArrayList;
/*
THE LOGIC:
If you must contain every member of your kind, then your index must be the first
PLEZZZZ DONT READ THIS, THE ALGO IS OVERCOMPLICATED
*/
public class Main
{
    static int lowestH;
    static int lowestG;
    static int highestH;
    static int highestG;
    public static void main(String[] args) {
        //basic data input
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        String ord = input.nextLine();
        int[] arr = new int[n];
        for (int i = 0; i<n; i++){
            arr[i] = input.nextInt();
        }
        
        //
        lowestH = -1;
        lowestG = -1;
        highestH = n;
        highestG = n;
        boundFinder(ord,n);

        ArrayList<Integer> validH = new ArrayList<Integer>();
        ArrayList<Integer> validG = new ArrayList<Integer>();
        pureLeaders(validG, false, ord, arr);
        pureLeaders(validH, true, ord, arr);
        int count = validH.size() * validG.size();
        for(int i = 0; i<validG.size(); i++){
            for(int a = 0; a<validG.get(i); a++){
                if(ord.charAt(a) == 'H'){
                    if(arr[a]-1>=validG.get(i)){
                        count++;
                    }
                }
            }
        }
        for(int i = 0; i<validH.size(); i++){
            for(int a = 0; a<validH.get(i); a++){
                if(ord.charAt(i) == 'G'){
                    if(arr[a]-1>=validH.get(i)){
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
        
        
        
    }
    public static void boundFinder(String str, int n){
        int i = n-1;
        while(highestH == n){
           if(str.charAt(i) == 'H'){
               highestH = i;
           } 
           i--;
        }
        i = n-1;
        while(highestG == n){
           if(str.charAt(i) == 'G'){
               highestG = i;
           } 
           i--;
        }
        i = 0;
        while(lowestH == -1){
           if(str.charAt(i) == 'H'){
               lowestH = i;
           } 
           i++;
        }
        i = 0;
        while(lowestG == -1){
           if(str.charAt(i) == 'G'){
               lowestG = i;
           } 
           i++;
        }
    }
    public static void pureLeaders(ArrayList<Integer> loc, boolean isH, String str, int[] arr){
        if(isH){
            for(int i = 0; i<=lowestH;i++){
                if(str.charAt(i) == 'H' && arr[i]-1>=highestH){
                    loc.add(i);
                }
            }
        }else{
            for(int i = 0; i<=lowestG;i++){
                if(str.charAt(i) == 'G' && arr[i]-1>=highestG){
                    loc.add(i);
                }
            }
        }
    }
}
