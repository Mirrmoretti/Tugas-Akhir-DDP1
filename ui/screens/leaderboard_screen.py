"""
Layar Papan Skor (Leaderboard Screen)
Menampilkan daftar skor tertinggi yang tersimpan 100% LOKAL di komputer (File I/O).
Bebas dari server / koneksi internet luar.
Menggunakan konsep OOP (tk.Frame).
"""

import tkinter as tk
from tkinter import messagebox
from config import (
    COLOR_SCREEN_BG, COLOR_STATUS_BAR, COLOR_CARD, COLOR_CARD_LIGHT,
    COLOR_PRIMARY, COLOR_PRIMARY_HOVER, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_MUTED,
    FONT_TITLE, FONT_SUBTITLE, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL, FONT_TINY
)
from models.game_state import GameState

class LeaderboardScreen(tk.Frame):
    """Layar papan skor dan riwayat permainan lokal."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_SCREEN_BG)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self, bg=COLOR_SCREEN_BG, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # Header
        lbl_icon = tk.Label(container, text="🏆", font=("Segoe UI Emoji", 30), bg=COLOR_SCREEN_BG)
        lbl_icon.pack(pady=(2, 0))

        lbl_title = tk.Label(
            container, 
            text="Papan Skor Lokal", 
            font=FONT_TITLE, 
            fg=COLOR_PRIMARY, 
            bg=COLOR_SCREEN_BG
        )
        lbl_title.pack(pady=(2, 2))

        # Badge Penyimpanan Lokal / Offline
        lbl_local_badge = tk.Label(
            container,
            text="💾 Tersimpan Lokal di File: data/local_highscores.json (Offline)",
            font=FONT_TINY,
            fg="#6EE7B7",
            bg="#064E3B",
            padx=8,
            pady=3
        )
        lbl_local_badge.pack(pady=(0, 10))

        # Kontainer List Skor
        self.scores_container = tk.Frame(container, bg=COLOR_CARD, padx=12, pady=12)
        self.scores_container.pack(fill="both", expand=True, pady=(0, 10))

        # Button row bawah
        bottom_frame = tk.Frame(container, bg=COLOR_SCREEN_BG)
        bottom_frame.pack(fill="x", side="bottom")

        # Tombol Reset Skor Lokal
        btn_reset = tk.Button(
            bottom_frame,
            text="🗑️ Reset Skor Lokal",
            font=FONT_SMALL,
            bg="#7F1D1D",
            fg="#FCA5A5",
            activebackground="#991B1B",
            activeforeground="#FFFFFF",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.confirm_reset_scores
        )
        btn_reset.pack(fill="x", ipady=4, pady=(0, 6))

        # Tombol Kembali
        btn_back = tk.Button(
            bottom_frame,
            text="⬅️ Kembali ke Menu Utama",
            font=FONT_BODY_BOLD,
            bg=COLOR_PRIMARY,
            fg="#0F172A",
            activebackground=COLOR_PRIMARY_HOVER,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.controller.show_start_screen
        )
        btn_back.pack(fill="x", ipady=8)

    def confirm_reset_scores(self):
        """Konfirmasi sebelum menghapus file skor lokal."""
        confirm = messagebox.askyesno(
            "Konfirmasi Reset",
            "Apakah kamu yakin ingin mengosongkan riwayat skor lokal dari komputermu?"
        )
        if confirm:
            GameState.clear_local_high_scores()
            self.refresh_scores()
            messagebox.showinfo("Berhasil", "Skor lokal berhasil dibersihkan!")

    def refresh_scores(self):
        """Membaca ulang skor dari JSON dan menampilkan ke layar."""
        for widget in self.scores_container.winfo_children():
            widget.destroy()

        scores = GameState.get_high_scores()

        if not scores:
            empty_lbl = tk.Label(
                self.scores_container,
                text="Belum ada catatan skor.\nJadilah yang pertama menyelesaikan simulasi!",
                font=FONT_BODY,
                fg=COLOR_TEXT_SECONDARY,
                bg=COLOR_CARD,
                justify="center"
            )
            empty_lbl.pack(expand=True, pady=40)
            return

        # Header Kolom
        header_row = tk.Frame(self.scores_container, bg=COLOR_CARD)
        header_row.pack(fill="x", pady=(0, 8))

        tk.Label(header_row, text="#", font=FONT_BODY_BOLD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=3, anchor="w").pack(side="left")
        tk.Label(header_row, text="Nama Pemain", font=FONT_BODY_BOLD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, anchor="w").pack(side="left", fill="x", expand=True)
        tk.Label(header_row, text="Skor", font=FONT_BODY_BOLD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=8, anchor="e").pack(side="right")
        tk.Label(header_row, text="Sisa Saldo", font=FONT_BODY_BOLD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=12, anchor="e").pack(side="right")

        # Garis Pembatas
        sep = tk.Frame(self.scores_container, bg="#475569", height=1)
        sep.pack(fill="x", pady=(0, 6))

        medals = ["🥇", "🥈", "🥉"]

        for idx, item in enumerate(scores[:8]):
            row = tk.Frame(self.scores_container, bg=COLOR_CARD)
            row.pack(fill="x", pady=4)

            # Rank
            rank_text = medals[idx] if idx < len(medals) else f" {idx+1}. "
            tk.Label(row, text=rank_text, font=FONT_BODY_BOLD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD, width=4, anchor="w").pack(side="left")

            # Nama
            name_text = item.get("name", "Anonim")
            tk.Label(row, text=name_text, font=FONT_BODY, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD, anchor="w").pack(side="left", fill="x", expand=True)

            # Skor
            score_text = f"{item.get('score', 0)}"
            tk.Label(row, text=score_text, font=FONT_BODY_BOLD, fg=COLOR_PRIMARY, bg=COLOR_CARD, width=8, anchor="e").pack(side="right")

            # Sisa Saldo
            savings = item.get("savings", 0)
            savings_text = f"Rp {savings:,.0f}".replace(",", ".")
            color_sav = COLOR_SUCCESS if savings > 0 else COLOR_DANGER
            tk.Label(row, text=savings_text, font=FONT_TINY, fg=color_sav, bg=COLOR_CARD, width=14, anchor="e").pack(side="right")
