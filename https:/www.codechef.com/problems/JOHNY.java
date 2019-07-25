/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner in=new Scanner(System.in);
		int tc=in.nextInt();
		for(int i=0;i<tc;i++){
		    int s=in.nextInt();
		    int arr[]=new int[s];
		    for(int j=0;j<s;j++){
		        arr[j]=in.nextInt();
		    }
		    int ele=arr[in.nextInt()-1];
		    Arrays.sort(arr);
		    for(int k=0;k<s;k++){
		        if(ele==arr[k]){
		            System.out.println(k+1);
		        }
		        else;
		    }
		    
		}
	}
}
