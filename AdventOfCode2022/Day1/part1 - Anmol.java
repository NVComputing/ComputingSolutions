import java.util.Scanner;
public class workspace4 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int largest= 0;
		int currsum = 0;
		String curinput;
		
		while(true) {
			curinput = input.nextLine();
			if(curinput.equals("no")) {
				if(largest<currsum) {
					largest = currsum;
				}
				currsum = 0;
				break;
			}
			if(curinput.isEmpty()) {
				if(largest<currsum) {
					largest = currsum;
				}
				currsum = 0;
			}else {
				currsum += Integer.parseInt(curinput);
			}
		}
		System.out.println(largest);
	}
}
