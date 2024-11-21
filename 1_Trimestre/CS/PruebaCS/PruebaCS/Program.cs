using System;
using System.Windows.Forms;

namespace MiAplicacion
{
    public class MiFormulario : Form
    {
        private TextBox cuadroTexto;
        private Button boton1;
        private Button boton2;

        public MiFormulario()
        {
            this.Text = "Mi Ventana";
            this.Size = new System.Drawing.Size(400, 200);

            cuadroTexto = new TextBox();
            cuadroTexto.Location = new System.Drawing.Point(50, 30);
            cuadroTexto.Width = 300;

            boton1 = new Button();
            boton1.Text = "Aceptar";
            boton1.Location = new System.Drawing.Point(50, 80);
            boton1.Click += new EventHandler(Boton1_Click);

            boton2 = new Button();
            boton2.Text = "Cancelar";
            boton2.Location = new System.Drawing.Point(200, 80);
            boton2.Click += new EventHandler(Boton2_Click);

            this.Controls.Add(cuadroTexto);
            this.Controls.Add(boton1);
            this.Controls.Add(boton2);
        }

        private void Boton1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Texto ingresado: " + cuadroTexto.Text);
        }

        private void Boton2_Click(object sender, EventArgs e)
        {
            cuadroTexto.Clear();
        }

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MiFormulario());
        }
    }
}