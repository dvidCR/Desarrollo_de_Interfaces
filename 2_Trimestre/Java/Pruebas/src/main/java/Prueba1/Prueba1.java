package Prueba1;

import java.util.ArrayList;
import java.util.List;

public class Prueba1 {
	
	private static List<Integer> numeros = new ArrayList<Integer>();

	public static int sumarValoresPares(List<Integer> valores) {
		int numFinal = 0;
		
		for(int num : valores) {
			if(num % 2 == 0) {
				numFinal += num;
			}
		}
		return numFinal;
	}
	
	public static void main(String[] args) {
		numeros.add(2);
		numeros.add(5);
		numeros.add(7);
		numeros.add(9);
		numeros.add(10);
		numeros.add(80);
		numeros.add(151);
		
		
		Prueba1 p1 = new Prueba1();
		
		System.out.println(p1.sumarValoresPares(numeros));
		
	}

}
