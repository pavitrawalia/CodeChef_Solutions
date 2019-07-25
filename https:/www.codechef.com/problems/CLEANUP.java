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
		int t;
		Scanner in = new Scanner(System.in);
		t=in.nextInt();
		for(int i=0;i<t;i++){
		    int tn=in.nextInt();
		    int cn=in.nextInt();
            if (cn!=0){
		    int arr[]=new int[cn];
		    for(int j=0;j<cn;j++){
		        arr[j]=in.nextInt();
		    }
		    int arr1[]= new int[tn];
		    for(int m=0;m<tn;m++){
		        for(int n=0;n<cn;n++){
		            if(m!=arr[n]-1){
		            arr1[m]=1;}
		            else{
		            arr1[m]=0;
		            break;}
		        }
		    }
		    int arr2[]= new int[tn-cn];
		    int s=0;
		     for(int k=0;k<tn;k++){
		            if (arr1[k] == 1)
		            {
		                arr2[s++]=k+1;
		            }
		            else;
		         }
		    for(int o=0;o<(tn-cn);o=o+2){
		        System.out.print(arr2[o]+" ");
		    }  
         System.out.println("");
		    for(int q=1;q<(tn-cn);q=q+2){
		        System.out.print(arr2[q]+" ");
		    }
		    System.out.println("");
		}
        else{
            for(int z=1;z<=tn;z=z+2){
                System.out.print(z+" ");
            }
            System.out.println("");
            for(int z=2;z<=tn;z=z+2){
                System.out.print(z+" ");
            }
            System.out.println("");
        }
        }
	}
}
