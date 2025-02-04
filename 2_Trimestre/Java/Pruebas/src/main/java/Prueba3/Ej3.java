package Prueba3;

import java.util.ArrayList;
import java.util.List;

public class Ej3 {
	
	private static List<Integer> edades = new ArrayList<Integer>();

	public static int obtenerPromedioEdades(List<Integer> edades) {
		int num = 0;
		
		for(int edad : edades) {
			num += edad;
		}
		
		return num / edades.size();
	}
	
	public static void main(String[] args) {
		edades.add(2);
		edades.add(50);
		edades.add(23);
		edades.add(84);
		edades.add(31);
		
		System.out.println(Ej3.obtenerPromedioEdades(edades));
		
	}

}
