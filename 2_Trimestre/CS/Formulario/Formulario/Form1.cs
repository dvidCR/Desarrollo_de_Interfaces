using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Formulario
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            // Datos a guardar
            string nombre = tbName.Text;
            string correo = tbEmail.Text;
            int telefono = int.Parse(tbPhone.Text);
            int edad = int.Parse(tbEdad.Text);

            // Validar que no estén vacíos
            if (string.IsNullOrWhiteSpace(nombre) || string.IsNullOrWhiteSpace(correo) || !int.TryParse(tbPhone.Text, out telefono) || !int.TryParse(tbEdad.Text, out edad))
            {
                MessageBox.Show("Por favor, completa todos los campos antes de guardar.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Ruta del archivo CSV
            string rutaArchivo = "datos.csv";

            try
            {
                // Verificar si el archivo existe para escribir el encabezado solo la primera vez
                bool archivoExiste = File.Exists(rutaArchivo);

                using (StreamWriter writer = new StreamWriter(rutaArchivo, true))
                {
                    // Escribir encabezado si es la primera vez
                    if (!archivoExiste)
                    {
                        writer.WriteLine("Nombre,Correo,Teléfono,Edad");
                    }

                    // Escribir datos
                    writer.WriteLine($"{nombre},{correo},{telefono},{edad}");
                }

                // Confirmación
                MessageBox.Show("Datos guardados correctamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Limpiar los campos del formulario
                tbName.Clear();
                tbEmail.Clear();
                tbPhone.Clear();
                tbEdad.Clear();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al guardar los datos: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnSalir_Click(object sender, EventArgs e)
        {
            // Cerrar la aplicación
            Application.Exit();
        }

        private void btnVerDatos_Click(object sender, EventArgs e)
        {
            Form2 form2 = new Form2();
            form2.Show(); // Muestra el segundo formulario
        }

        private void lblEdad_Click(object sender, EventArgs e)
        {

        }
    }
}
