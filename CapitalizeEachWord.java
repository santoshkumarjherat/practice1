package com.techmedevted;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//hello guys whats up

public class CapitalizeEachWord
{
	public static void main(String args[]) throws IOException
{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter line");
	String input=br.readLine();
	StringBuilder sb=new StringBuilder(input.length());

	String[] words=input.split("\\ ");

	for(int i=0; i<words.length; i++)
{
	sb.append(Character.toUpperCase(words[i].charAt(0))).append(words[i].substring(1)).append(" ");
}
	System.out.println(sb);
}
}