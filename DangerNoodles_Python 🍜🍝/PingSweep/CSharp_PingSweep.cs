using System.Net.NetworkInformation;

namespace PingSweep_v01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, Ping Sweep!");
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("Made by Daacals");
            Console.ForegroundColor = ConsoleColor.Green;
            /*
            if (args.Length != 1)
            {
                Console.WriteLine("Usage: PingSweep.exe <IP prefix>");
                return;
            }
             */
            //string ipPrefix = args[0];
            string ipPrefix = "192.168.56";
            for (int i = 1; i <= 254; i++)
            {
                string ipAddress = $"{ipPrefix}.{i}";
                Ping pingSender = new Ping();
                PingReply reply = pingSender.Send(ipAddress);

                if (reply.Status == IPStatus.Success)
                {
                    Console.WriteLine($"{ipAddress} is alive (Roundtrip Time: {reply.RoundtripTime}ms)");
                }
                else
                {
                    Console.WriteLine($"{ipAddress} is not responding");
                }
            }
            Console.ReadLine();
        }
    }
}