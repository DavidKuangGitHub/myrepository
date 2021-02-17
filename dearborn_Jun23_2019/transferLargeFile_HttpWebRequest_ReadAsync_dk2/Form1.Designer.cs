
namespace transferLargeFile_HttpWebRequest_ReadAsync_dk2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.bt_start_server = new System.Windows.Forms.Button();
            this.tx_recv_data = new System.Windows.Forms.TextBox();
            this.bt_send = new System.Windows.Forms.Button();
            this.tx_data = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // bt_start_server
            // 
            this.bt_start_server.Location = new System.Drawing.Point(48, 47);
            this.bt_start_server.Name = "bt_start_server";
            this.bt_start_server.Size = new System.Drawing.Size(155, 39);
            this.bt_start_server.TabIndex = 0;
            this.bt_start_server.Text = "Start Server";
            this.bt_start_server.UseVisualStyleBackColor = true;
            this.bt_start_server.Click += new System.EventHandler(this.bt_start_server_Click);
            // 
            // tx_recv_data
            // 
            this.tx_recv_data.Location = new System.Drawing.Point(48, 127);
            this.tx_recv_data.Name = "tx_recv_data";
            this.tx_recv_data.Size = new System.Drawing.Size(695, 31);
            this.tx_recv_data.TabIndex = 1;
            // 
            // bt_send
            // 
            this.bt_send.Location = new System.Drawing.Point(618, 358);
            this.bt_send.Name = "bt_send";
            this.bt_send.Size = new System.Drawing.Size(125, 38);
            this.bt_send.TabIndex = 2;
            this.bt_send.Text = "Send Data";
            this.bt_send.UseVisualStyleBackColor = true;
            this.bt_send.Click += new System.EventHandler(this.bt_send_Click);
            // 
            // tx_data
            // 
            this.tx_data.Location = new System.Drawing.Point(48, 257);
            this.tx_data.Name = "tx_data";
            this.tx_data.Size = new System.Drawing.Size(695, 31);
            this.tx_data.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.tx_data);
            this.Controls.Add(this.bt_send);
            this.Controls.Add(this.tx_recv_data);
            this.Controls.Add(this.bt_start_server);
            this.Name = "Form1";
            this.Text = "TransferLargeFile_HttpWebRequest_ReadAsync_DK3";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_start_server;
        private System.Windows.Forms.TextBox tx_recv_data;
        private System.Windows.Forms.Button bt_send;
        private System.Windows.Forms.TextBox tx_data;
    }
}

