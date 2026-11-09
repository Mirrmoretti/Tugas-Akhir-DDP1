"""
====================================================================
PROYEK TUGAS AKHIR DASAR-DASAR PEMROGRAMAN 1 (DDP 1)
CyberShield: Phone Simulator - Edukasi Kesadaran Anti-Scam & Siber
====================================================================
Entry Point Utama Aplikasi.
Jalankan file ini melalui terminal atau run langsung di PyCharm:
    python main.py
====================================================================
"""

import sys
import os

# Menambahkan direktori proyek ke PYTHONPATH agar impor modul berjalan lancar
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.app import CyberShieldApp

def main():
    """Fungsi utama untuk menginisialisasi dan menjalankan aplikasi Tkinter."""
    print("=" * 60)
    print(" Memulai CyberShield: Phone Simulator...")
    print(" Tugas Akhir Dasar-Dasar Pemrograman 1 (DDP 1)")
    print(" Tema: Edukasi & Pencegahan Penipuan Digital (Anti-Scam)")
    print("=" * 60)
    
    try:
        app = CyberShieldApp()
        app.mainloop()
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan saat menjalankan aplikasi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
