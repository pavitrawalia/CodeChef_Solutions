/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class parent{
    public long exchange(long n){
        long dp;
    if(n<12)
        return n;

    dp=exchange(n/2)+exchange(n/3)+exchange(n/4);
    return dp;
}
};
class Codechef extends parent
{   
    	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		parent h=new parent();
		Scanner in=new Scanner(System.in);
		long[] a=new long[10];
		int i=0;
		while (in.hasNextLong()) {
    a[i] = in.nextLong();
    i++;
}
		for(int j=0;j<i;j++){
		System.out.println(h.exchange((a[j])));
		}
	}
}
