package javaDoc;

/**
 * @author David
 *
 *  
*/
public class Persona {
    private String nombre;
    private int edad;
 
 
    /**
     *
     * @param nombre es el nombre de la Persona
     * @param edad es la edad de la Persona
     */
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
 
    /**
     *
     * @return devuelve una cadena Nombre y Edad de la Persona
     */
    public String obtenerInformacion() {
        return "Nombre: " + nombre + ", Edad: " + edad;
    }
 
 
    public void actualizarEdad(int nuevaEdad) {
        if (nuevaEdad > 0) {
            this.edad = nuevaEdad;
        } else {
            System.out.println("La edad tiene que ser positiva.");
        }
    }
 
    public static void main(String[] args) {
        Persona persona = new Persona("Juan", 25);
        System.out.println(persona.obtenerInformacion());
 
        persona.actualizarEdad(30);
        System.out.println(persona.obtenerInformacion());
    }
}