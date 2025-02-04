using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace PruebaCS
{
    public partial class Form1 : Form
    {
        List<Citas> citas = new List<Citas>();

        public Form1()
        {
            InitializeComponent();
        }

        private void lbl1_Click(object sender, EventArgs e)
        {

        }

        private void lbl2_Click(object sender, EventArgs e)
        {

        }
        private void lbl3_Click(object sender, EventArgs e)
        {

        }
        private void nombre_TextChanged(object sender, EventArgs e)
        {

        }
        private void hora_ValueChanged(object sender, EventArgs e)
        {

        }

        private void btnReservar_Click(object sender, EventArgs e)
        {
            var nuevaCita = new Citas
            {
                Nombre = nombre.Text,
                Fecha = datePicker.Value,
                Hora = hora.Value.ToShortTimeString()
            };
            citas.Add(nuevaCita);
            MessageBox.Show("Cita reservada.");
            ActualizarListaCitas();
        }

        private void btnVer_Click(object sender, EventArgs e)
        {

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }
        private void ActualizarListaCitas()
        {
            treeView1.Rows.Clear();
            foreach (var cita in citas)
            {
                treeView1.Rows.Add(cita.Nombre, cita.Fecha.ToShortDateString(), cita.Hora);
            }
        }
    }
}
