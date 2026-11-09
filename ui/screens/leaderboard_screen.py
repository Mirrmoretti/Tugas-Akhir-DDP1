"""
Layar Papan Skor (Leaderboard Screen)
Menampilkan daftar skor tertinggi yang tersimpan di file data/highscores.json (File I/O).
Menggunakan konsep OOP (tk.Frame).
"""

import tkinter as tk
from config import (
    COLOR_SCREEN_BG, COLOR_STATUS_BAR, COLOR_CARD, COLOR_CARD_LIGHT,
    COLOR_PRIMARY, COLOR_PRIMARY_HOVER, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_MUTED,
    FONT_TITLE, FONT_SUBTITLE, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL, FONT_TINY
)
from models.game_state import GameState

class LeaderboardScreen(tk.Frame):
    """Layar papan skor dan riwayat permainan."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_SCREEN_BG)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self, bg=COLOR_SCREEN_BG, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # Header
        lbl_icon = tk.Label(container, text="🏆", font=("Segoe UI Emoji", 32), bg=COLOR_SCREEN_BG)
        lbl_icon.pack(pady=(5, 0))

        lbl_title = tk.Label(
            container, 
            text="Papan Skor Waspada Siber", 
            font=FONT_TITLE, 
            fg=COLOR_PRIMARY, 
            bg=COLOR_SCREEN_BG
        )
        lbl_title.pack(pady=(2, 12))

        # Kontainer List Skor
        self.scores_container = tk.Frame(container, bg=COLOR_CARD, padx=12, pady=12)
        self.scores_container.pack(fill="both", expand=True, pady=(0, 15))

        # Tombol Kembali
        btn_back = tk.Button(
            container,
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
        btn_back.pack(fill="x", ipady=8, side="bottom")

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
