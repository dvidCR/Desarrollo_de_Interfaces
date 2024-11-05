package main;

import net.objecthunter.exp4j.Expression;
import net.objecthunter.exp4j.ExpressionBuilder;
import net.objecthunter.exp4j.tokenizer.UnknownFunctionOrVariableException;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.effect.Reflection;
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
		
		VBox layoutV = new VBox(10);
		HBox layoutH = new HBox(10);
		GridPane grid = new GridPane();
		
		for (int i = 0; i < botones.length; i++) {
			for (int j = 0; j < botones[i].length; j++) {
				Button boton = new Button(botones[i][j]);
				boton.setOnAction(e -> {
					if(boton.getText().equals("=")) {
						Expression calc = null;
						
						try {
							calc = (Expression) new ExpressionBuilder(tf.getText()).build();
							double resultado = calc.evaluate();
                            tf.setText(String.valueOf(resultado));
						} catch (UnknownFunctionOrVariableException ex) {
                            tf.setText("Función desconocida");
                            ex.printStackTrace();
                        } catch (Exception ex) {
                            tf.setText("Error");
                            ex.printStackTrace();
                        }
					} else if (boton.getText().equals("C")) {
						tf.clear();
					} else if (boton.getText().equals("->")) {
						String content = tf.getText();
						if (content.length() > 0) {
                            content = content.substring(0, content.length() - 1);
                            tf.setText(content);
						}
					} else {
						tf.setText(tf.getText() + boton.getText());
					}
					
				});
				grid.add(boton, j, i+1);
			}
		}
		
		layoutH.getChildren().add(tf);
		layoutV.getChildren().addAll(layoutH, grid);
		
		Scene escena = new Scene(layoutV, 400, 400);
		Stage.setScene(escena);
		Stage.setTitle("Calculadora");
		Stage.show();
	}
	
	public static void main(String[] args) {
		launch(args);
	}

}
