namespace InterfazLimpiaClase
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
            this.BarraDeTitulo = new System.Windows.Forms.Panel();
            this.btnCerrar = new System.Windows.Forms.PictureBox();
            this.btnMinimizar = new System.Windows.Forms.PictureBox();
            this.btnMaxRes = new System.Windows.Forms.PictureBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.submenu = new System.Windows.Forms.Panel();
            this.btnSubmenu2 = new System.Windows.Forms.Button();
            this.btnSubmenu1 = new System.Windows.Forms.Button();
            this.btn2 = new System.Windows.Forms.Button();
            this.btn1 = new System.Windows.Forms.Button();
            this.btnMenu = new System.Windows.Forms.Button();
            this.PanelContenedor = new System.Windows.Forms.Panel();
            this.BarraDeTitulo.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.btnCerrar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.btnMinimizar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.btnMaxRes)).BeginInit();
            this.panel1.SuspendLayout();
            this.submenu.SuspendLayout();
            this.SuspendLayout();
            // 
            // BarraDeTitulo
            // 
            this.BarraDeTitulo.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(200)))), ((int)(((byte)(255)))));
            this.BarraDeTitulo.Controls.Add(this.btnCerrar);
            this.BarraDeTitulo.Controls.Add(this.btnMinimizar);
            this.BarraDeTitulo.Controls.Add(this.btnMaxRes);
            this.BarraDeTitulo.Dock = System.Windows.Forms.DockStyle.Top;
            this.BarraDeTitulo.Location = new System.Drawing.Point(0, 0);
            this.BarraDeTitulo.Name = "BarraDeTitulo";
            this.BarraDeTitulo.Size = new System.Drawing.Size(800, 35);
            this.BarraDeTitulo.TabIndex = 0;
            this.BarraDeTitulo.MouseDown += new System.Windows.Forms.MouseEventHandler(this.BarraDeTitulo_MouseDown);
            // 
            // btnCerrar
            // 
            this.btnCerrar.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnCerrar.BackColor = System.Drawing.Color.Red;
            this.btnCerrar.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.btnCerrar.Location = new System.Drawing.Point(731, 0);
            this.btnCerrar.Name = "btnCerrar";
            this.btnCerrar.Size = new System.Drawing.Size(35, 35);
            this.btnCerrar.TabIndex = 3;
            this.btnCerrar.TabStop = false;
            this.btnCerrar.Click += new System.EventHandler(this.btnCerrar_Click);
            // 
            // btnMinimizar
            // 
            this.btnMinimizar.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnMinimizar.BackColor = System.Drawing.Color.Yellow;
            this.btnMinimizar.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.btnMinimizar.Location = new System.Drawing.Point(662, 0);
            this.btnMinimizar.Name = "btnMinimizar";
            this.btnMinimizar.Size = new System.Drawing.Size(35, 35);
            this.btnMinimizar.TabIndex = 2;
            this.btnMinimizar.TabStop = false;
            this.btnMinimizar.Click += new System.EventHandler(this.btnMinimizar_Click);
            // 
            // btnMaxRes
            // 
            this.btnMaxRes.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnMaxRes.BackColor = System.Drawing.Color.Lime;
            this.btnMaxRes.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.btnMaxRes.Location = new System.Drawing.Point(588, 0);
            this.btnMaxRes.Name = "btnMaxRes";
            this.btnMaxRes.Size = new System.Drawing.Size(35, 35);
            this.btnMaxRes.TabIndex = 1;
            this.btnMaxRes.TabStop = false;
            this.btnMaxRes.Click += new System.EventHandler(this.btnMaxRes_Click);
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.MediumTurquoise;
            this.panel1.Controls.Add(this.submenu);
            this.panel1.Controls.Add(this.btn2);
            this.panel1.Controls.Add(this.btn1);
            this.panel1.Controls.Add(this.btnMenu);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 35);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(200, 415);
            this.panel1.TabIndex = 1;
            // 
            // submenu
            // 
            this.submenu.Controls.Add(this.btnSubmenu2);
            this.submenu.Controls.Add(this.btnSubmenu1);
            this.submenu.Location = new System.Drawing.Point(12, 58);
            this.submenu.Name = "submenu";
            this.submenu.Size = new System.Drawing.Size(162, 100);
            this.submenu.TabIndex = 3;
            this.submenu.Visible = false;
            // 
            // btnSubmenu2
            // 
            this.btnSubmenu2.BackColor = System.Drawing.Color.MediumTurquoise;
            this.btnSubmenu2.FlatAppearance.BorderSize = 0;
            this.btnSubmenu2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnSubmenu2.Image = global::InterfazLimpiaClase.Properties.Resources.kirbo__1_;
            this.btnSubmenu2.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnSubmenu2.Location = new System.Drawing.Point(42, 63);
            this.btnSubmenu2.Name = "btnSubmenu2";
            this.btnSubmenu2.Size = new System.Drawing.Size(75, 23);
            this.btnSubmenu2.TabIndex = 4;
            this.btnSubmenu2.Text = "SubBotón2";
            this.btnSubmenu2.UseVisualStyleBackColor = false;
            // 
            // btnSubmenu1
            // 
            this.btnSubmenu1.BackColor = System.Drawing.Color.MediumTurquoise;
            this.btnSubmenu1.FlatAppearance.BorderSize = 0;
            this.btnSubmenu1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnSubmenu1.Image = global::InterfazLimpiaClase.Properties.Resources.kirbo__1_;
            this.btnSubmenu1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnSubmenu1.Location = new System.Drawing.Point(42, 15);
            this.btnSubmenu1.Name = "btnSubmenu1";
            this.btnSubmenu1.Size = new System.Drawing.Size(75, 23);
            this.btnSubmenu1.TabIndex = 3;
            this.btnSubmenu1.Text = "SubBotón1";
            this.btnSubmenu1.UseVisualStyleBackColor = false;
            // 
            // btn2
            // 
            this.btn2.BackColor = System.Drawing.Color.MediumTurquoise;
            this.btn2.FlatAppearance.BorderSize = 0;
            this.btn2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn2.Image = global::InterfazLimpiaClase.Properties.Resources.kirbo__1_;
            this.btn2.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn2.Location = new System.Drawing.Point(12, 239);
            this.btn2.Name = "btn2";
            this.btn2.Size = new System.Drawing.Size(75, 23);
            this.btn2.TabIndex = 2;
            this.btn2.Text = "Botón2";
            this.btn2.UseVisualStyleBackColor = false;
            // 
            // btn1
            // 
            this.btn1.BackColor = System.Drawing.Color.MediumTurquoise;
            this.btn1.FlatAppearance.BorderSize = 0;
            this.btn1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn1.Image = global::InterfazLimpiaClase.Properties.Resources.kirbo__1_;
            this.btn1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btn1.Location = new System.Drawing.Point(12, 191);
            this.btn1.Name = "btn1";
            this.btn1.Size = new System.Drawing.Size(75, 23);
            this.btn1.TabIndex = 1;
            this.btn1.Text = "Formulario";
            this.btn1.UseVisualStyleBackColor = false;
            this.btn1.Click += new System.EventHandler(this.btn1_Click);
            // 
            // btnMenu
            // 
            this.btnMenu.BackColor = System.Drawing.Color.MediumTurquoise;
            this.btnMenu.FlatAppearance.BorderSize = 0;
            this.btnMenu.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnMenu.Image = global::InterfazLimpiaClase.Properties.Resources.kirbo__1_;
            this.btnMenu.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnMenu.Location = new System.Drawing.Point(12, 29);
            this.btnMenu.Name = "btnMenu";
            this.btnMenu.Size = new System.Drawing.Size(75, 23);
            this.btnMenu.TabIndex = 0;
            this.btnMenu.Text = "Menú";
            this.btnMenu.UseVisualStyleBackColor = false;
            this.btnMenu.Click += new System.EventHandler(this.btnMenu_Click);
            // 
            // PanelContenedor
            // 
            this.PanelContenedor.Dock = System.Windows.Forms.DockStyle.Fill;
            this.PanelContenedor.Location = new System.Drawing.Point(200, 35);
            this.PanelContenedor.Name = "PanelContenedor";
            this.PanelContenedor.Size = new System.Drawing.Size(600, 415);
            this.PanelContenedor.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.PanelContenedor);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.BarraDeTitulo);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.BarraDeTitulo.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.btnCerrar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.btnMinimizar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.btnMaxRes)).EndInit();
            this.panel1.ResumeLayout(false);
            this.submenu.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel BarraDeTitulo;
        private System.Windows.Forms.PictureBox btnMaxRes;
        private System.Windows.Forms.PictureBox btnCerrar;
        private System.Windows.Forms.PictureBox btnMinimizar;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btn1;
        private System.Windows.Forms.Button btnMenu;
        private System.Windows.Forms.Button btn2;
        private System.Windows.Forms.Panel submenu;
        private System.Windows.Forms.Button btnSubmenu2;
        private System.Windows.Forms.Button btnSubmenu1;
        private System.Windows.Forms.Panel PanelContenedor;
    }
}

