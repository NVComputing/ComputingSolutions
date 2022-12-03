import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.*;
public class workspace4 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int largest1 = 0;
		int largest2 = 0;
		int largest3 = 0;
		int currsum = 0;
		String curinput;
		while(true) {
			curinput = input.nextLine();
			if(curinput.isEmpty()) {
				largest1 = currsum;
				currsum = 0;
				break;
			}else {
				currsum += Integer.parseInt(curinput);
			}
		}
		while(true) {
			curinput = input.nextLine();
			if(curinput.isEmpty()) {
				if(currsum>largest1) {
					int swap = largest1;
					largest1 = currsum;
					largest2 = swap;
				}else {
					largest2 = currsum;
				}
				currsum = 0;
				break;
			}else {
				currsum += Integer.parseInt(curinput);
			}
		}

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
				if(largest1<currsum) {
					largest3 = largest2;
					largest2 = largest1;
					largest1 = currsum;
				}else if(largest2<currsum) {
					largest3 = largest2;
					largest2 = currsum;
				}else if(largest3<currsum) {
					largest3 = currsum;
				}
				currsum = 0;
			}else {
				currsum += Integer.parseInt(curinput);
			}
		}
		System.out.println(largest1+ largest2 + largest3);
	}
}
