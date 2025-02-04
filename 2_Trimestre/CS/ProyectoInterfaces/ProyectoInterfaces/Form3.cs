using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            string fechaEvento = dateTimePicker1.Value.ToString("yyyy-MM-dd");
            string nombre = tbName.Text;
            string descripcion = tbDesc.Text;

            if (string.IsNullOrWhiteSpace(nombre))
            {
                MessageBox.Show("Por favor, completa todos los campos antes de guardar.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            string rutaArchivo = "eventos.json";

            try
            {
                // Leer el archivo JSON existente o crear uno nuevo
                Dictionary<string, Evento> eventos = new Dictionary<string, Evento>();

                if (File.Exists(rutaArchivo))
                {
                    string json = File.ReadAllText(rutaArchivo);
                    eventos = JsonSerializer.Deserialize<Dictionary<string, Evento>>(json) ?? new Dictionary<string, Evento>();
                }

                // Agregar el nuevo evento
                if (eventos.ContainsKey(nombre))
                {
                    MessageBox.Show("Ya existe un evento con este nombre. Usa un nombre diferente.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                eventos[nombre] = new Evento
                {
                    FechaEvento = fechaEvento,
                    Descripcion = descripcion
                };

                // Guardar de nuevo en el archivo JSON
                string nuevoJson = JsonSerializer.Serialize(eventos, new JsonSerializerOptions { WriteIndented = true });
                File.WriteAllText(rutaArchivo, nuevoJson);

                MessageBox.Show("Datos guardados correctamente en el archivo JSON.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                this.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al guardar los datos: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnSalir_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Clase para representar un evento
        public class Evento
        {
            public string FechaEvento { get; set; }
            public string Descripcion { get; set; }
        }
    }
}
