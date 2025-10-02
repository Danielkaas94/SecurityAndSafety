if [ “$1” == “” ]
then
echo “Type the IP address to scan.”
echo “Example: ./pingsweep.sh 192.168.2”
else
for ip in `seq 1 254` ; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d “:” &
done
fi