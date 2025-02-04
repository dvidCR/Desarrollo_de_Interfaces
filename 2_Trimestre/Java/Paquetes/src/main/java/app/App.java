package app;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class App extends Application {
	@Override
    public void start(Stage primaryStage) {
        // Crear un botón
        Button button = new Button("Haz clic aquí");
        button.setOnAction(e -> System.out.println("¡Hola, mundo!"));

        // Configurar el diseño
        StackPane root = new StackPane();
        root.getChildren().add(button);

        // Crear la escena
        Scene scene = new Scene(root, 300, 200);

        // Configurar la ventana
        primaryStage.setTitle("Ejemplo JavaFX con Maven");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args); // Llama al método launch de JavaFX
    }
}