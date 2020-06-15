using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TwentyFourPoints
{
    class TwentyFourPoints
    {
        public static bool found = false;
        public static int times = 0;
        static TwentyFourPoints practical11 = new TwentyFourPoints();
        public void Calculate(double [] Cards, int length)
        {
            if (length == 1 && Cards[0] > 23.99 && Cards[0] < 24.01)
            {
                found = true;
                return;
            }
            if (length == 1)
                return;
            double [] nextCards = new double[10];
            for (int x = 0; x < length - 1; x++)
                for (int y = x + 1; y < length; y++)
                {
                    int t = 0;
                    for(int i = 0; i < length; i++)
                        if(i!=x && i!=y)
                        {
                            nextCards[t] = Cards[i];
                            t++;
                        }
                    if (found == false)
                    {
                        times++;
                        nextCards[t] = Cards[x] + Cards[y];
                        practical11.Calculate(nextCards, length - 1);
                     }
                    if (found == false && Cards[x] > Cards[y])
                    {
                        times++;
                        nextCards[t] = Cards[x] - Cards[y];
                        practical11.Calculate(nextCards, length - 1);
                    }
                    if (found == false && Cards[y] >= Cards[x])
                    {
                        times++;
                        nextCards[t] = Cards[y] - Cards[x];
                        practical11.Calculate(nextCards, length - 1);
                    }
                    if (found == false)
                    {
                        times++;
                        nextCards[t] = Cards[x] * Cards[y];
                        practical11.Calculate(nextCards, length - 1);
                    }
                    if (found == false && Cards[y] != 0)
                    {
                        times++;
                        nextCards[t] = Cards[x] / Cards[y];
                        practical11.Calculate(nextCards, length - 1);
                    }
                    if (found == false && Cards[x] != 0)
                    {
                        times++;
                        nextCards[t] = Cards[y] / Cards[x];
                        practical11.Calculate(nextCards, length - 1);
                    }
                }

        }
        static void Main(string[] args)
        {
            String input;
            double[] Cards = new double[10];
            bool outrange = false;
            int n;
            Console.WriteLine("Please enter numbers between 1 and 23 and divided them with \",\".");
            while (true)
            {
                input = Console.ReadLine();
                string[] strCards = input.Split(',');
                n = strCards.Length;
                for (int i = 0; i < n; i++)
                {
                    Cards[i] = int.Parse(strCards[i]);
                    if (Cards[i] < 1 || Cards[i] > 23)
                    {
                        outrange = true;
                        Console.WriteLine("Number(s) outrange(s). Please reenter your numbers.");
                    }
                }
                if (outrange == false)
                        break;
            }
            practical11.Calculate(Cards, n);
            if (found == true)
                Console.WriteLine("Yes");
            else
                Console.WriteLine("NO");
            Console.WriteLine("Recursion times: {0}", times);
            Console.ReadKey();
        }
    }
}
