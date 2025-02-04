using System;
using System.Data;
using System.IO;
using System.Windows.Forms;

namespace Formulario
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            CargarDatos();
        }

        private void CargarDatos()
        {
            string rutaArchivo = "datos.csv";

            if (!File.Exists(rutaArchivo))
            {
                MessageBox.Show("El archivo de datos no existe.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            try
            {
                DataTable tabla = new DataTable();
                string[] lineas = File.ReadAllLines(rutaArchivo);

                if (lineas.Length > 0)
                {
                    // Añadir columnas a la tabla desde la primera línea
                    string[] encabezados = lineas[0].Split(',');
                    foreach (string encabezado in encabezados)
                    {
                        tabla.Columns.Add(encabezado);
                    }

                    // Añadir filas a la tabla desde las líneas restantes
                    for (int i = 1; i < lineas.Length; i++)
                    {
                        string[] datos = lineas[i].Split(',');
                        tabla.Rows.Add(datos);
                    }
                }

                dataGridView1.DataSource = tabla;
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error al cargar los datos: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnCerrar_Click(object sender, EventArgs e)
        {
            this.Close(); // Cierra el formulario
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
