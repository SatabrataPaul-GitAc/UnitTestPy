import java.io.*;
import java.lang.*;
public class crc
{
public static void main(String args[]) throws IOException
{
int f[]=new int[25];
int gen[]=new int[10];
int rem[]=new int[10];
int flen,glen,rlen,i,j;
int p,sum,iframe,igen,irem;
String data;
BufferedReader in=new BufferedReader(new
InputStreamReader(System.in));
System.out.println("Enter the frame:");
data=in.readLine();flen=data.length()-1;
for(i=0;i<data.length();i++)
f[i]=(int)(data.charAt(i))-48;
System.out.println("Enter the generator:");
data=in.readLine();
glen=data.length()-1;
for(i=1;i<=glen;i++)
f[flen+i]=0;
flen=flen+glen;
for(i=0;i<data.length();i++)
gen[i]=((int)(data.charAt(i))-48);
p=0;
sum=0;
for(i=flen;i>=0;i--)
{
sum=sum+(f[i]*(int)Math.pow(2,p));
p=p+1;
}
iframe=sum;
p=0;
sum=0;
for(i=glen;i>=0;i--)
{
sum=sum+(gen[i]*(int)Math.pow(2,p));
p=p+1;
}
igen=sum;
irem=iframe%igen;
irem=igen-irem;
i=0;
while(iframe>0)
{
f[i]=iframe%2;
iframe=iframe/2;i++;
}
if(iframe == 1)
f[i]=iframe;
System.out.print("Transmitted string:");
for(i=flen;i>=0;i--)
System.out.print(f[i]);
System.out.print("\n\nEnter the received
string:");
data=in.readLine();
flen=data.length()-1;
for(i=0;i<data.length();i++)
f[i]=((int)(data.charAt(i)))-48;
p=0;
sum=0;
for(i=flen;i>=0;i--)
{
p=p+1;
}
iframe=sum;
irem=iframe%igen;
if(irem==0)
{
System.out.println("Message received with no error");
}
else
{
System.out.println("Message received with error");
}
}
}
