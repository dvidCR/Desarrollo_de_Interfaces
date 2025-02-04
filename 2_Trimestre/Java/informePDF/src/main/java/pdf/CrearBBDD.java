package pdf;

import java.sql.*;

public class CrearBBDD {
    private Connection c = null;
    private Statement stmt = null;

    public void crearTabla() {
  
    try {
       Class.forName("org.sqlite.JDBC");
       c = DriverManager.getConnection("jdbc:sqlite:recetas.db");

       stmt = c.createStatement();
       String sql = "CREATE TABLE COMPANY " +
                      "(ID INT PRIMARY KEY     NOT NULL," +
                      " NAME           TEXT    NOT NULL )" ;

       stmt.executeUpdate(sql);
       stmt.close();
       
       stmt = c.createStatement();
       sql = "INSERT INTO COMPANY (ID,NAME) " +
                      "VALUES (1, 'Paul');"; 
       stmt.executeUpdate(sql);
       sql = "INSERT INTO COMPANY (ID,NAME) " +
                      "VALUES (2, 'Alfonso');"; 
       stmt.executeUpdate(sql);
       stmt.close();
       c.commit();
      

    } catch ( Exception e ) {
       System.err.println( e.getClass().getName() + ": " + e.getMessage() );
       System.exit(0);
    }
        System.out.println("Opened database successfully");
   } 

   public void cerrarBBDD() {
    try {
        c.close();
    } catch (SQLException e) {
        
        e.printStackTrace();
    }
   }
}