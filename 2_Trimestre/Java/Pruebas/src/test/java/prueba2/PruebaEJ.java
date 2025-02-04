package prueba2;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import Prueba2.Ej2;

public class PruebaEJ {
	
	@Test
	public void testObtenerNombresEnMayusculas() {
		List<String> nombres = new ArrayList<String>();
		nombres.add("DARIO");
		nombres.add("DAVID");
		
		Ej2.obtenerNombresEnMayuscula(nombres);
		
		List<String> nombresMayus = new ArrayList<String>();
		nombresMayus.add("dario".toUpperCase());
		nombresMayus.add("david".toUpperCase());
		
		assertEquals(nombres, nombresMayus);
	}
}
