"""
Layar Awal (Start Screen / Welcome Screen)
Menggunakan konsep OOP berbasis tk.Frame.
"""

import tkinter as tk
from tkinter import messagebox
from config import (
    COLOR_SCREEN_BG, COLOR_CARD, COLOR_PRIMARY, COLOR_PRIMARY_HOVER,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_SUCCESS, COLOR_WARNING,
    FONT_TITLE, FONT_SUBTITLE, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL
)

class StartScreen(tk.Frame):
    """Layar pembuka game simulasi smartphone anti-scam."""
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_SCREEN_BG)
        self.controller = controller
        
        self.create_widgets()

    def create_widgets(self):
        # Container utama dengan padding
        container = tk.Frame(self, bg=COLOR_SCREEN_BG)
        container.pack(expand=True, fill="both", padx=25, pady=30)

        # Ikon & Logo Header
        icon_label = tk.Label(
            container, 
            text="🛡️📱", 
            font=("Segoe UI Emoji", 42), 
            bg=COLOR_SCREEN_BG
        )
        icon_label.pack(pady=(10, 5))

        title_label = tk.Label(
            container, 
            text="CyberShield", 
            font=("Segoe UI", 22, "bold"), 
            fg=COLOR_PRIMARY, 
            bg=COLOR_SCREEN_BG
        )
        title_label.pack()

        subtitle_label = tk.Label(
            container, 
            text="Phone Simulator: Anti-Scam Awareness", 
            font=FONT_SUBTITLE, 
            fg=COLOR_TEXT_SECONDARY, 
            bg=COLOR_SCREEN_BG
        )
        subtitle_label.pack(pady=(2, 20))

        # Card Informasi & Aturan Main
        card_info = tk.Frame(container, bg=COLOR_CARD, bd=0, relief="flat", padx=16, pady=16)
        card_info.pack(fill="x", pady=10)

        info_title = tk.Label(
            card_info, 
            text="🎯 Misi Pelatihan Kamu:", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_CARD,
            anchor="w"
        )
        info_title.pack(fill="x", pady=(0, 8))

        rules = [
            "📩 Analisis pesan asing, tawaran kerja, & file yang masuk.",
            "💰 Lindungi Saldo Tabunganmu (Rp 5.000.000).",
            "🛡️ Jaga Skor Kewaspadaan (Awareness) agar tidak jebol.",
            "💡 Pelajari Red Flags & Tips Keamanan di setiap kasus!"
        ]

        for rule in rules:
            r_lbl = tk.Label(
                card_info, 
                text=rule, 
                font=FONT_SMALL, 
                fg=COLOR_TEXT_SECONDARY, 
                bg=COLOR_CARD, 
                wraplength=360, 
                justify="left",
                anchor="w"
            )
            r_lbl.pack(fill="x", pady=2)

        # Form Input Nama Pemain
        form_frame = tk.Frame(container, bg=COLOR_SCREEN_BG)
        form_frame.pack(fill="x", pady=(20, 15))

        name_label = tk.Label(
            form_frame, 
            text="Masukkan Nama Kamu:", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_SCREEN_BG,
            anchor="w"
        )
        name_label.pack(fill="x", pady=(0, 6))

        self.name_entry = tk.Entry(
            form_frame, 
            font=FONT_BODY, 
            bg=COLOR_CARD, 
            fg=COLOR_TEXT_PRIMARY, 
            insertbackground=COLOR_TEXT_PRIMARY,
            bd=0, 
            relief="flat",
            highlightthickness=1,
            highlightbackground="#475569",
            highlightcolor=COLOR_PRIMARY
        )
        self.name_entry.pack(fill="x", ipady=8, padx=2)
        self.name_entry.insert(0, "Mahasiswa DDP1")
        self.name_entry.focus_set()

        # Tombol Mulai Permainan
        self.btn_start = tk.Button(
            container, 
            text="🚀 Mulai Simulasi Ponsel", 
            font=FONT_BODY_BOLD, 
            bg=COLOR_PRIMARY, 
            fg="#0F172A",
            activebackground=COLOR_PRIMARY_HOVER,
            activeforeground="#0F172A",
            bd=0, 
            relief="flat", 
            cursor="hand2",
            command=self.on_start_clicked
        )
        self.btn_start.pack(fill="x", ipady=10, pady=(15, 8))

        # Tombol Leaderboard / Papan Skor
        self.btn_leaderboard = tk.Button(
            container, 
            text="🏆 Papan Skor (Leaderboard)", 
            font=FONT_BODY, 
            bg=COLOR_CARD, 
            fg=COLOR_TEXT_PRIMARY,
            activebackground="#475569",
            activeforeground=COLOR_TEXT_PRIMARY,
            bd=0, 
            relief="flat", 
            cursor="hand2",
            command=self.controller.show_leaderboard_screen
        )
        self.btn_leaderboard.pack(fill="x", ipady=8)

        # Footer DDP 1
        footer_label = tk.Label(
            container, 
            text="Tugas Akhir Dasar-Dasar Pemrograman 1 (DDP 1)", 
            font=FONT_SMALL, 
            fg="#64748B", 
            bg=COLOR_SCREEN_BG
        )
        footer_label.pack(side="bottom", pady=5)

    def on_start_clicked(self):
        player_name = self.name_entry.get().strip()
        if not player_name:
            messagebox.showwarning("Peringatan", "Silakan masukkan namamu terlebih dahulu!")
            return
            
        self.controller.start_new_game(player_name)
