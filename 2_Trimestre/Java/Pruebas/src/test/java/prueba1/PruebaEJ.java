package prueba1;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
 
import org.junit.Test;

import Prueba1.Prueba1;
 
public class PruebaEJ {
 
	
	@Test
	public void UnitTest1() {
		Random random = new Random();
		List<Integer> numeros = new ArrayList<Integer>();
		int sumaPares = 0;
		for (int i = 0; i<7;i++) {
			int numero= random.nextInt(0,9);
			if (numero%2 == 0) {
				sumaPares += numero;
			}
			numeros.add(numero);
		}
		assertEquals(sumaPares,Prueba1.sumarValoresPares(numeros));
	}
}