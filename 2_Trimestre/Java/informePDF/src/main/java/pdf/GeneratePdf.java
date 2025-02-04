package pdf;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;
import com.itextpdf.layout.properties.HorizontalAlignment;
import com.itextpdf.layout.element.Image;
import com.itextpdf.io.image.ImageData;
import com.itextpdf.io.image.ImageDataFactory;
import com.itextpdf.layout.element.Table;
import com.itextpdf.layout.element.List;

public class GeneratePdf {
    public static void main(String[] args) {
		 try { 
			 String dbUrl = "jdbc:sqlite:recetas.db";// Asegúrate de usar la ruta correcta
			 CrearBBDD crearBBDD = new CrearBBDD();
			 crearBBDD.crearTabla();
			 crearBBDD.cerrarBBDD();
		 } catch (Exception e) {
			// TODO: handle exception
		}
	     String dest = "example.pdf"; // Nombre del archivo PDF a generar

         try {
             // Registrar el controlador JDBC de SQLite
             Class.forName("org.sqlite.JDBC");

             // Conectar a la base de datos SQLite
             Connection conn = DriverManager.getConnection(dbUrl);
             Statement stmt = conn.createStatement();
             
             // Ejecutar una consulta para obtener los datos de la tabla
             String sql = "SELECT * FROM recetas"; // Cambia "recetas" por el nombre de tu tabla
             ResultSet rs = stmt.executeQuery(sql);

             // Crear un escritor de PDF
             PdfWriter writer = new PdfWriter(dest);
             // Crear un documento PDF
             PdfDocument pdf = new PdfDocument(writer);
             Document document = new Document(pdf);             


             // Añadir un título al documento
             document.add(new Paragraph("Listado de Recetas:"));
             
             // Añadir imagen
             ImageData imageData = ImageDataFactory.create("src/main/resources/pepo.jpg");
             Image img = new Image(imageData);
             document.add(img);

             // Crear la tabla con los datos obtenidos de la base de datos
             Table table = new Table(3); // 3 columnas, ajusta según el número de columnas de tu tabla
             table.addCell("ID");
             table.addCell("Nombre");
             table.addCell("Tiempo");

             // Llenar la tabla con los datos de la base de datos
             while (rs.next()) {
                 table.addCell(rs.getString("id")); // Cambia "id" por el nombre de tu columna
                 table.addCell(rs.getString("nombre")); // Cambia "nombre" por el nombre de tu columna
                 table.addCell(rs.getString("Tiempo")+" min"); // Cambia "descripcion" por el nombre de tu columna
             }

             // Añadir la tabla al documento
             document.add(table);

             // Cerrar el documento y la conexión a la base de datos
             document.close();
             rs.close();
             stmt.close();
             conn.close();

             System.out.println("PDF creado en: " + dest);
         } catch (Exception e) {
             e.printStackTrace();
         }
     }
 }