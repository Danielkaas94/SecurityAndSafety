using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.IO;

namespace FuckPython
{
    internal class Program
    {

        private static readonly HttpClient client = new HttpClient();

        static async Task Main(string[] args)
        {
            Console.WriteLine("Guido van Rossum - GO FUCK YOURSELF AND YOUR STUPID SNAKE! 🐍");

            await MakeGetRequestsAsync_SubDomain_v3(true, ConsoleColor.Magenta, "techdocs.dk");

            Console.WriteLine("Done");
        }

        static async Task MakeGetRequestsAsync_SubDomain_v3(bool isHttps = false, ConsoleColor Foregroundcolor = ConsoleColor.Green, string website = "supercool.dk")
        {
            string protocol;

            if (isHttps)
            {
                protocol = "https://";
            }
            else
            {
                protocol = "http://";
            }

            Console.WriteLine("############");
            Console.WriteLine(protocol);
            Console.WriteLine(protocol);
            Console.WriteLine(protocol);
            Console.WriteLine("############");

            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string fileName = "subdomains-10000.txt";

            string filePath = Path.Combine(desktopPath, fileName);

            string[] subDomains = File.ReadAllLines(filePath);

            foreach (var subDomain in subDomains)
            {
                try
                {
                    HttpResponseMessage response = await client.GetAsync(protocol + subDomain + "." + website); // This is working!

                    if (response.IsSuccessStatusCode)
                    {
                        string responseBody = await response.Content.ReadAsStringAsync();

                        //Console.WriteLine("Response from " + url + ": " + responseBody);

                        Console.ForegroundColor = Foregroundcolor;
                        Console.WriteLine(protocol + subDomain + "." + website);
                        Console.ResetColor();
                    }
                    else
                    {

                    }

                }
                catch (HttpRequestException ex)
                {
                    //Console.WriteLine("Error for " + subDomain + "." + website + ": " + ex.Message);
                    //Console.WriteLine(ex.ToString());
                    continue;
                }
                catch (Exception ex)
                {
                    //Console.WriteLine("Exception: " + ex.Message);
                    continue;
                }
            }
        }



        static async Task MakeGetRequestsAsync_SubDomain_v2()
        {

            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string fileName = "subdomains-10000.txt";

            string filePath = Path.Combine(desktopPath, fileName);

            string website = "supercool.dk";

            string[] subDomains = File.ReadAllLines(filePath);

            foreach (var subDomain in subDomains)
            {
                try
                {
                    //HttpResponseMessage response = await client.GetAsync("en" + "." + ".wikipedia.org/wiki/Cat");
                    //HttpResponseMessage response = await client.GetAsync("https://" + "en" + "." + "wikipedia.org/wiki/Cat"); // This is working! Prototype
                    //HttpResponseMessage response = await client.GetAsync("https://" + subDomain + "." + website); // This is working!
                    HttpResponseMessage response = await client.GetAsync("http://" + subDomain + "." + website); // This is working!

                    //Console.WriteLine(subDomain + "." + website);

                    if (response.IsSuccessStatusCode)
                    {
                        string responseBody = await response.Content.ReadAsStringAsync();

                        //Console.WriteLine("Response from " + url + ": " + responseBody);

                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.WriteLine(subDomain + "." + website);
                        Console.ResetColor();
                    }
                    else
                    {
                        Console.WriteLine("HELLO?????????");
                        //Console.WriteLine("Error for " + url + ": " + response.ReasonPhrase);
                    }

                }
                catch (HttpRequestException ex)
                {
                    Console.WriteLine("Error for " + subDomain + "." + website + ": " + ex.Message);
                    //Console.WriteLine(ex.ToString());
                    continue;
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Exception: " + ex.Message);
                    continue;
                }
            }
        }



        static async Task MakeGetRequestsAsync_SubDomain()
        {

            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string fileName = "subdomains-10000.txt";

            string filePath = Path.Combine(desktopPath, fileName);

            string website = "supercool.dk";

            try
            {
                string[] subDomains = File.ReadAllLines(filePath);

                foreach (var subDomain in subDomains)
                {
                    try
                    {
                        HttpResponseMessage response = await client.GetAsync(subDomain + "." + website);

                        Console.WriteLine(subDomain + "." + website);

                        if (response.IsSuccessStatusCode)
                        {
                            string responseBody = await response.Content.ReadAsStringAsync();

                            //Console.WriteLine("Response from " + url + ": " + responseBody);

                            Console.ForegroundColor = ConsoleColor.Cyan;
                            Console.WriteLine(subDomain + "." + website);
                            Console.ResetColor();
                        }
                        else
                        {
                            Console.WriteLine("HELLO?????????");
                            //Console.WriteLine("Error for " + url + ": " + response.ReasonPhrase);
                        }

                    }
                    catch (HttpRequestException ex)
                    {
                        Console.WriteLine("Error for " + subDomain + "." + website + ": " + ex.Message);
                        //Console.WriteLine(ex.ToString());
                        continue;
                    }

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: " + ex.Message);
            }


        }




        static async Task MakeGetRequestsAsync()
        {
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string fileName = "list-domains.txt";

            string filePath = Path.Combine(desktopPath, fileName);

            try
            {
                string[] urls = File.ReadAllLines(filePath);

                foreach (var url in urls)
                {
                    try
                    {

                        //HttpResponseMessage response = await client.GetAsync("https://" + url);       // result: 32
                        //HttpResponseMessage response = await client.GetAsync("http://" + url);        // result: 70
                        HttpResponseMessage response = await client.GetAsync(url);        // result: 0

                        if (response.IsSuccessStatusCode)
                        {
                            string responseBody = await response.Content.ReadAsStringAsync();

                            //Console.WriteLine("Response from " + url + ": " + responseBody);

                            Console.ForegroundColor = ConsoleColor.Cyan;
                            Console.WriteLine("www." + url);
                            Console.ResetColor();

                        }
                        else
                        {
                            //Console.WriteLine("Error for " + url + ": " + response.ReasonPhrase);
                        }

                    }
                    catch (HttpRequestException ex)
                    {
                        //Console.WriteLine(ex.ToString());
                    }

                }
            }
            catch (Exception ex)
            {
                //Console.WriteLine("Exception: " + ex.Message);
            }
        }
    }
}