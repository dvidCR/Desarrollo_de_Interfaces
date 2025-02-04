using System;
using System.Drawing;
using System.Windows.Forms;
using System.Drawing.Drawing2D;
using System.ComponentModel;

namespace Custom_Toggle
{
    public class ToggleButton : CheckBox
    {
        private Color onBackColor = Color.MediumSlateBlue;
        private Color onToggleColor = Color.White;
        private Color offBackColor = Color.Gray;
        private Color offToggleColor = Color.WhiteSmoke;
        private bool solidStyle = true;

        public ToggleButton()
        {
            this.MinimumSize = new Size(45, 22); // Tamaño mínimo del botón.
        }

        private GraphicsPath GetFigurePath()
        {
            int arcSize = this.Height - 1;
            Rectangle leftArc = new Rectangle(0, 0, arcSize, arcSize);
            Rectangle rightArc = new Rectangle(this.Width - arcSize - 2, 0, arcSize, arcSize);

            GraphicsPath path = new GraphicsPath();
            path.StartFigure();
            path.AddArc(leftArc, 90, 180);
            path.AddArc(rightArc, 270, 180);
            path.CloseFigure();
            return path;
        }

        protected override void OnPaint(PaintEventArgs pevent)
        {
            Graphics graphics = pevent.Graphics;
            graphics.SmoothingMode = SmoothingMode.AntiAlias;
            graphics.Clear(this.Parent.BackColor);

            int toggleSize = this.Height - 5;
            Rectangle toggleRect;

            if (this.Checked) // Estado "ON"
            {
                graphics.FillPath(new SolidBrush(onBackColor), GetFigurePath());
                toggleRect = new Rectangle(this.Width - this.Height + 1, 2, toggleSize, toggleSize);
                graphics.FillEllipse(new SolidBrush(onToggleColor), toggleRect);
            }
            else // Estado "OFF"
            {
                graphics.FillPath(new SolidBrush(offBackColor), GetFigurePath());
                toggleRect = new Rectangle(2, 2, toggleSize, toggleSize);
                graphics.FillEllipse(new SolidBrush(offToggleColor), toggleRect);
            }
        }

        [Category("Toggle Button")]
        public Color OnBackColor
        {
            get => onBackColor;
            set { onBackColor = value; this.Invalidate(); }
        }

        [Category("Toggle Button")]
        public Color OnToggleColor
        {
            get => onToggleColor;
            set { onToggleColor = value; this.Invalidate(); }
        }

        [Category("Toggle Button")]
        public Color OffBackColor
        {
            get => offBackColor;
            set { offBackColor = value; this.Invalidate(); }
        }

        [Category("Toggle Button")]
        public Color OffToggleColor
        {
            get => offToggleColor;
            set { offToggleColor = value; this.Invalidate(); }
        }

        [Category("Toggle Button")]
        public bool SolidStyle
        {
            get => solidStyle;
            set { solidStyle = value; this.Invalidate(); }
        }
    }
}
