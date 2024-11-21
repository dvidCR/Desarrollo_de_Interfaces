package main;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Tooltip;
import javafx.scene.effect.DropShadow;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main extends Application {
	
	@Override
	public void start(Stage Stage) throws Exception {
		Label label = new Label("Ingerese su número: ");
		
		TextField campoTexto = new TextField();
		
		Button boton = new Button("Aceptar");
		
		// Para añadirle una leyenda que aparece cuando mantienes el raton en el boton
		Tooltip tp = new Tooltip("mensajito que le pongo al boton");
		boton.setTooltip(tp);
		
		// Para añadirle un sombreado al boton
		DropShadow sombra = new DropShadow();
		boton.setEffect(sombra);
		
		// Al tener el mouse en el boton cambia el color
		boton.setOnMouseEntered(e -> boton.setStyle("-fx-background-color: #ff0000;"));
		// Al NO tener el mouse en el boton cambia el color
		boton.setOnMouseExited(e -> boton.setStyle("-fx-background-color: #ffffff"));
		
		boton.setOnAction(e -> {
			System.out.println(campoTexto.getText());
		});
		
		VBox layoutV = new VBox(10); // El 10 son los pixeles de separacion entre elementos
		
		layoutV.getChildren().addAll(label, campoTexto, boton);
		
		Scene escena = new Scene(layoutV, 300, 200);
		
		Stage.setScene(escena);
		Stage.setTitle("Mi pantalla");
		Stage.show();
	}

	public static void main(String[] args) {
		launch(args);
	}

}
