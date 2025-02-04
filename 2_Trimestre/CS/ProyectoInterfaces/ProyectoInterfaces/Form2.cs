using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class Form2 : Form
    {
        private string rutaArchivo = "eventos.json";

        public Form2()
        {
            InitializeComponent();
            cargarEventos();
        }

        private void cargarEventos()
        {
            if (!File.Exists(rutaArchivo))
            {
                MessageBox.Show("El archivo de eventos no existe.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            try
            {
                // Leer y deserializar el contenido del archivo JSON
                string json = File.ReadAllText(rutaArchivo);
                var eventos = JsonSerializer.Deserialize<Dictionary<string, Evento>>(json);

                if (eventos == null || eventos.Count == 0)
                {
                    richTextBox1.Text = "No hay eventos para mostrar.";
                    return;
                }

                // Formatear los eventos para mostrar
                var sb = new System.Text.StringBuilder();
                foreach (var kvp in eventos)
                {
                    string nombre = kvp.Key;
                    Evento evento = kvp.Value;

                    if (evento.Descripcion == "")
                    {
                        sb.AppendLine($"Evento: {nombre}\nFecha: {evento.FechaEvento}\n");
                    }
                    else
                    {
                        sb.AppendLine($"Evento: {nombre}\nFecha: {evento.FechaEvento}\nDesc: {evento.Descripcion}\n");
                    }
                    sb.AppendLine("--------------------------------------------------------------------------------------------\n\n");

                    // Mostrar el resultado en el RichTextBox
                    richTextBox1.Text = sb.ToString();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al leer el archivo: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnSalir_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Clase para deserializar los datos del JSON
        public class Evento
        {
            public string FechaEvento { get; set; }
            public string Descripcion { get; set; }
        }
    }
}
