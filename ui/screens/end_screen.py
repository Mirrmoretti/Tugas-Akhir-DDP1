"""
Layar Akhir / Rapor Hasil (End Screen)
Menampilkan evaluasi literasi keamanan siber, skor akhir, dan opsi main lagi.
Menggunakan konsep OOP (tk.Frame).
"""

import tkinter as tk
from config import (
    COLOR_SCREEN_BG, COLOR_STATUS_BAR, COLOR_CARD, COLOR_CARD_LIGHT,
    COLOR_PRIMARY, COLOR_PRIMARY_HOVER, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_MUTED,
    FONT_TITLE, FONT_SUBTITLE, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL
)

class EndScreen(tk.Frame):
    """Layar rapor akhir setelah menyelesaikan simulasi."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_SCREEN_BG)
        self.controller = controller
        self.game_state = None

        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self, bg=COLOR_SCREEN_BG, padx=20, pady=20)
        self.container.pack(fill="both", expand=True)

    def set_game_state(self, game_state):
        self.game_state = game_state
        self.render_report()

    def format_rupiah(self, amount: int) -> str:
        return f"Rp {amount:,.0f}".replace(",", ".")

    def render_report(self):
        # Bersihkan container jika ada widget lama
        for widget in self.container.winfo_children():
            widget.destroy()

        if not self.game_state:
            return

        title_badge, description = self.game_state.calculate_final_rating()
        
        # Tentukan Ikon & Status Banner
        if self.game_state.end_reason == "bankrupt":
            status_icon = "💸💥"
            status_text = "SIMULASI BERAKHIR: SALDO HABIS!"
            badge_color = COLOR_DANGER
        elif self.game_state.end_reason == "zero_awareness":
            status_icon = "⚠️🔓"
            status_text = "SIMULASI BERAKHIR: PERANGKAT DIBOBOL!"
            badge_color = COLOR_WARNING
        else:
            status_icon = "🏆🛡️"
            status_text = "SIMULASI SELESAI DENGAN SUKSES!"
            badge_color = COLOR_SUCCESS

        # Icon
        lbl_icon = tk.Label(self.container, text=status_icon, font=("Segoe UI Emoji", 36), bg=COLOR_SCREEN_BG)
        lbl_icon.pack(pady=(5, 2))

        # Status text
        lbl_status = tk.Label(self.container, text=status_text, font=FONT_SUBTITLE, fg=badge_color, bg=COLOR_SCREEN_BG)
        lbl_status.pack()

        # Gelar / Badge Evaluasi
        lbl_badge = tk.Label(
            self.container, 
            text=f"🎖️ {title_badge}", 
            font=("Segoe UI", 13, "bold"), 
            fg=COLOR_PRIMARY, 
            bg=COLOR_SCREEN_BG
        )
        lbl_badge.pack(pady=(6, 2))

        lbl_desc = tk.Label(
            self.container, 
            text=description, 
            font=FONT_SMALL, 
            fg=COLOR_TEXT_SECONDARY, 
            bg=COLOR_SCREEN_BG,
            wraplength=380,
            justify="center"
        )
        lbl_desc.pack(pady=(0, 15))

        # Card Statistik Pemain
        stats_card = tk.Frame(self.container, bg=COLOR_CARD, padx=16, pady=12)
        stats_card.pack(fill="x", pady=(0, 15))

        card_title = tk.Label(
            stats_card, 
            text="📊 Rapor Hasil Pelatihan:", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_CARD,
            anchor="w"
        )
        card_title.pack(fill="x", pady=(0, 8))

        stat_items = [
            ("Nama Agen", self.game_state.player_name, COLOR_TEXT_PRIMARY),
            ("Total Skor", f"{self.game_state.score} Poin", COLOR_PRIMARY),
            ("Sisa Tabungan", self.format_rupiah(self.game_state.savings), COLOR_SUCCESS if self.game_state.savings > 0 else COLOR_DANGER),
            ("Tingkat Waspada", f"{self.game_state.awareness}%", COLOR_TEXT_PRIMARY),
            ("Keputusan Tepat", f"{self.game_state.correct_choices} Kasus", COLOR_SUCCESS),
            ("Jebakan Terkena", f"{self.game_state.traps_triggered} Kasus", COLOR_DANGER if self.game_state.traps_triggered > 0 else COLOR_SUCCESS)
        ]

        for label, val, color in stat_items:
            row = tk.Frame(stats_card, bg=COLOR_CARD)
            row.pack(fill="x", pady=2)

            l_lbl = tk.Label(row, text=label, font=FONT_SMALL, fg=COLOR_TEXT_SECONDARY, bg=COLOR_CARD)
            l_lbl.pack(side="left")

            v_lbl = tk.Label(row, text=val, font=FONT_BODY_BOLD, fg=color, bg=COLOR_CARD)
            v_lbl.pack(side="right")

        # Rangkuman Pembelajaran Utama (Edukatif)
        tips_box = tk.Frame(self.container, bg="#0F172A", padx=12, pady=10)
        tips_box.pack(fill="x", pady=(0, 15))

        t_title = tk.Label(
            tips_box, 
            text="📌 3 Prinsip Dasar Anti-Scam:", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_WARNING, 
            bg="#0F172A",
            anchor="w"
        )
        t_title.pack(fill="x", pady=(0, 4))

        principles = [
            "1. JANGAN PERNAH instal file berformat .apk dari chat.",
            "2. Kode OTP dan PIN perbankan adalah rahasia mutlak.",
            "3. Verifikasi ulang ke nomor lama sebelum transfer uang darurat."
        ]

        for p in principles:
            p_lbl = tk.Label(
                tips_box, 
                text=p, 
                font=FONT_TITLE, 
                fg=COLOR_TEXT_SECONDARY, 
                bg="#0F172A",
                anchor="w",
                justify="left"
            )
            p_lbl.pack(fill="x", pady=1)

        # Tombol Aksi
        btn_frame = tk.Frame(self.container, bg=COLOR_SCREEN_BG)
        btn_frame.pack(fill="x", side="bottom")

        btn_restart = tk.Button(
            btn_frame,
            text="🔄 Main Ulang (Tingkatkan Skor)",
            font=FONT_BODY_BOLD,
            bg=COLOR_PRIMARY,
            fg="#0F172A",
            activebackground=COLOR_PRIMARY_HOVER,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda: self.controller.show_start_screen()
        )
        btn_restart.pack(fill="x", ipady=8, pady=(0, 6))

        btn_leaderboard = tk.Button(
            btn_frame,
            text="🏆 Lihat Papan Skor (Leaderboard)",
            font=FONT_BODY,
            bg=COLOR_CARD,
            fg=COLOR_TEXT_PRIMARY,
            activebackground=COLOR_CARD_LIGHT,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.controller.show_leaderboard_screen
        )
        btn_leaderboard.pack(fill="x", ipady=6)
