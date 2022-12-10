import java.util.*;
public class part2Anthony {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		Set<List<Integer>> visited = new HashSet<List<Integer>>();
		List<Integer> start = new LinkedList<Integer>();
		start.add(0);
		start.add(0);
		visited.add(start);
		int[][] snake = new int[10][2];

		while (true)
		{
			String str = s.nextLine();
			if (str.equals("a"))
			{
				break;
			}
			char dir = str.charAt(0);
			int count = Integer.parseInt(str.split(" ")[1]);
			for (int i = 0; i < count; i++)
			{
				if (dir == 'R')
				{
					snake[0][0]++;
				}
				else if (dir == 'L')
				{
					snake[0][0]--;
				}
				else if (dir == 'U')
				{
					snake[0][1]++;
				}
				else if (dir == 'D')
				{
					snake[0][1]--;
				}
				
				for (int k = 1; k < snake.length; k++)
				{
					snake[k] = updateT(snake[k-1][0], snake[k-1][1], snake[k][0], snake[k][1]);
				}
				List<Integer> temp = new LinkedList<Integer>();
				temp.add(snake[9][0]);
				temp.add(snake[9][1]);
				visited.add(temp);
			}
		}
		System.out.println(visited.size());

	}
	public static int[] updateT(int headx, int heady, int tailx, int taily)
	{
		int[] tailpos = new int[2];
		int xdif = headx - tailx;
		int ydif = heady - taily;
		if (Math.pow(xdif, 2) + Math.pow(ydif, 2) == 5)
		{
			tailx += xdif / Math.abs(xdif);
			taily += ydif / Math.abs(ydif);
		}
		else if (Math.pow(xdif, 2) + Math.pow(ydif, 2) == 4 || Math.pow(xdif, 2) + Math.pow(ydif, 2) == 8)
		{
			tailx += xdif / 2;
			taily += ydif / 2;
		}
		tailpos[0] = tailx;
		tailpos[1] = taily;
		return tailpos;
	}
	
}

