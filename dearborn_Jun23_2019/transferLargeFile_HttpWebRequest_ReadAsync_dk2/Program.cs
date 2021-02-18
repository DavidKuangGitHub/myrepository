using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace transferLargeFile_HttpWebRequest_ReadAsync_dk2
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            AddTheFolderIfNotExist();
            Application.Run(new Form1());
        }
        
        private static void AddTheFolderIfNotExist()
        {
            //throw new NotImplementedException();
            System.IO.Directory.CreateDirectory("C/temp_dk/");
        }
    }
}
