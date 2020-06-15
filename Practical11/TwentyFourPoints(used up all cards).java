import java.util.*;

public class TwentyFourPoints
{
	public static TwentyFourPoints practical11 = new TwentyFourPoints();
	static int times = 0;
	static Boolean found = false;
	public void calculate(Float [] cards,int length)
	{
		if(length == 1 && cards[0] > 23.999 && cards[0] < 24.001)
		{
			found = true;
			return;
		}
		if(length == 1)
			return;
		Float[] nextCalculation = new Float[10];
		for(int x = 0; x < length-1; x++)
			for(int y = x + 1; y < length; y++)
			{
				int t = 0;
				for(int i = 0; i < length; i++)
				{
					if(i != x && i != y)
					{
						nextCalculation[t]=cards[i];
						t++;
					}
				}
				if(found == false)
				{
					nextCalculation[length-2]=cards[x]+cards[y];
					practical11.calculate(nextCalculation,length-1);
					times+=1;
				}
				if(found == false)
				{
					if(cards[x]>cards[y])
						nextCalculation[length-2]=cards[x]-cards[y];
					else
						nextCalculation[length-2]=cards[y]-cards[x];
					practical11.calculate(nextCalculation,length-1);
					times+=1;
				}
				if(found == false)
				{
					nextCalculation[length-2]=cards[x]*cards[y];
					practical11.calculate(nextCalculation,length-1);
					times+=1;
				}
				if(found == false && cards[y] != 0)
				{
					nextCalculation[length-2]=cards[x]/cards[y];
					practical11.calculate(nextCalculation,length-1);
					times+=1;
				}
				if(found == false && cards[x] != 0)
				{
					nextCalculation[length-2]=cards[y]/cards[x];
					practical11.calculate(nextCalculation,length-1);
					times+=1;
				}
			}
	}
	
	public static void main(String[] args)
	{
		Float [] cards = new Float[10];
		int n;
		System.out.println("Please enter four numbers betweeen 1 and 23 and divide them with \",\"");
		Scanner s = new Scanner(System.in);
		while(true)
		{
			Boolean outRange = false;
			String input = s.nextLine();
			String [] strCards = new String[10];
			strCards = input.split(",");
			n = strCards.length;
			for(int i = 0; i<n;i++)
			{
				cards[i]=Float.valueOf(strCards[i]);
				if(cards[i]<1 | cards[i]>23)
				{
					outRange = true;
					System.out.println("Number(s) outrange(s). Please reenter your numbers");
					break;
				}
			}
			if(outRange == false) {
				break;
			}
		}
		s.close();
		practical11.calculate(cards,n);
		if(found == true)
			System.out.println("Yes");
		else
			System.out.println("No");
		System.out.println("Recusion times: "+times);	
	}
}