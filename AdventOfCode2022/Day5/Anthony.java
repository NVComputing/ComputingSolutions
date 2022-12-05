import java.util.*;
public class Anthony {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int rows = 9;
		ArrayList<Character>[] boxes = new ArrayList[rows];
		for (int i = 0; i < rows; i++)
		{
			boxes[i] = new ArrayList<Character>();
		}
		while (true)
		{
			String str = s.nextLine();
			if (str.equals("a"))
			{
				break;
			}
			if (str.length()>2&& (str.charAt(0) == '[' || str.substring(0, 2).equals(("  "))))
			{
				for (int i = 1; i < str.length(); i+=4)
				{
					if (str.charAt(i) != ' ')
					{
						boxes[(i-1)/4].add(str.charAt(i));
					}
				}
			}
			else if (str.length()>0&&str.charAt(0) == 'm')
			{
				String[] spl = str.split(" ");
				int count = Integer.parseInt(spl[1]);
				int start = Integer.parseInt(spl[3]) - 1;
				int end = Integer.parseInt(spl[5]) - 1;
				for (int i = 0; i < count; i++)
				{
					//boxes[end].add(0, boxes[start].remove(0)); part 1
					boxes[end].add(i, boxes[start].remove(0));
				}
			}
		}
		for (int i = 0; i < rows; i++)
		{
		System.out.print(boxes[i].get(0));
		}
	}
}
