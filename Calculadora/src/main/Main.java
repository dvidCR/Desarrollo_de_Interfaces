package main;


import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main extends Application {
	
	@Override
	public void start(Stage Stage) throws Exception {
		String[][] botones = {
				{"C", "/", "*", "->"},
				{"7", "8", "9", "-"},
				{"4", "5", "6", "+"},
				{"1", "2", "3", "."},
				{"0", "(", ")", "="}
		};
		
		TextField tf = new TextField();
		
		GridPane grid = new GridPane();
		
		for (int i = 0; i < botones.length; i++) {
			for (int j = 0; j < botones[i].length; j++) {
				Button boton = new Button(botones[i][j]);
				grid.add(boton, i, j);
			}
		}
		
		Scene escena = new Scene(grid, 400, 400);
		Stage.setScene(escena);
		Stage.setTitle("Calculadora");
		Stage.show();
	}
	
	public static void main(String[] args) {
		launch(args);
	}

}
