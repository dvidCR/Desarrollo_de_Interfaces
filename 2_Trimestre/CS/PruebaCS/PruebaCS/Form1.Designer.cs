namespace PruebaCS
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.lbl1 = new System.Windows.Forms.Label();
            this.lbl2 = new System.Windows.Forms.Label();
            this.lbl3 = new System.Windows.Forms.Label();
            this.nombre = new System.Windows.Forms.TextBox();
            this.btnReservar = new System.Windows.Forms.Button();
            this.btnVer = new System.Windows.Forms.Button();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.hora = new System.Windows.Forms.DateTimePicker();
            this.SuspendLayout();
            // 
            // lbl1
            // 
            this.lbl1.AutoSize = true;
            this.lbl1.Location = new System.Drawing.Point(51, 62);
            this.lbl1.Name = "lbl1";
            this.lbl1.Size = new System.Drawing.Size(59, 16);
            this.lbl1.TabIndex = 0;
            this.lbl1.Text = "Nombre:";
            this.lbl1.Click += new System.EventHandler(this.lbl1_Click);
            // 
            // lbl2
            // 
            this.lbl2.AutoSize = true;
            this.lbl2.Location = new System.Drawing.Point(51, 105);
            this.lbl2.Name = "lbl2";
            this.lbl2.Size = new System.Drawing.Size(48, 16);
            this.lbl2.TabIndex = 1;
            this.lbl2.Text = "Fecha:";
            this.lbl2.Click += new System.EventHandler(this.lbl2_Click);
            // 
            // lbl3
            // 
            this.lbl3.AutoSize = true;
            this.lbl3.Location = new System.Drawing.Point(51, 144);
            this.lbl3.Name = "lbl3";
            this.lbl3.Size = new System.Drawing.Size(40, 16);
            this.lbl3.TabIndex = 2;
            this.lbl3.Text = "Hora:";
            this.lbl3.Click += new System.EventHandler(this.lbl3_Click);
            // 
            // nombre
            // 
            this.nombre.Location = new System.Drawing.Point(116, 56);
            this.nombre.Name = "nombre";
            this.nombre.Size = new System.Drawing.Size(229, 22);
            this.nombre.TabIndex = 4;
            this.nombre.TextChanged += new System.EventHandler(this.nombre_TextChanged);
            // 
            // btnReservar
            // 
            this.btnReservar.Location = new System.Drawing.Point(54, 226);
            this.btnReservar.Name = "btnReservar";
            this.btnReservar.Size = new System.Drawing.Size(114, 31);
            this.btnReservar.TabIndex = 5;
            this.btnReservar.Text = "Reservar";
            this.btnReservar.UseVisualStyleBackColor = true;
            this.btnReservar.Click += new System.EventHandler(this.btnReservar_Click);
            // 
            // btnVer
            // 
            this.btnVer.Location = new System.Drawing.Point(232, 226);
            this.btnVer.Name = "btnVer";
            this.btnVer.Size = new System.Drawing.Size(113, 31);
            this.btnVer.TabIndex = 6;
            this.btnVer.Text = "Ver";
            this.btnVer.UseVisualStyleBackColor = true;
            this.btnVer.Click += new System.EventHandler(this.btnVer_Click);
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(54, 297);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(291, 104);
            this.treeView1.TabIndex = 7;
            this.treeView1.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.treeView1_AfterSelect);
            // 
            // hora
            // 
            this.hora.Location = new System.Drawing.Point(98, 137);
            this.hora.Name = "hora";
            this.hora.Size = new System.Drawing.Size(247, 22);
            this.hora.TabIndex = 8;
            this.hora.ValueChanged += new System.EventHandler(this.hora_ValueChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.hora);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.btnVer);
            this.Controls.Add(this.btnReservar);
            this.Controls.Add(this.nombre);
            this.Controls.Add(this.lbl3);
            this.Controls.Add(this.lbl2);
            this.Controls.Add(this.lbl1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lbl1;
        private System.Windows.Forms.Label lbl2;
        private System.Windows.Forms.Label lbl3;
        private System.Windows.Forms.TextBox nombre;
        private System.Windows.Forms.Button btnReservar;
        private System.Windows.Forms.Button btnVer;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.DateTimePicker hora;
    }
}

