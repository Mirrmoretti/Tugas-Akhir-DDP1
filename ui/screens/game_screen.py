"""
Layar Permainan Utama (Game Screen)
Simulasi smartphone interaktif dengan chat bubble, status bar, dan feedback edukasi.
Menggunakan konsep OOP (tk.Frame).
"""

import tkinter as tk
from tkinter import ttk
from config import (
    COLOR_SCREEN_BG, COLOR_STATUS_BAR, COLOR_CARD, COLOR_CARD_LIGHT,
    COLOR_PRIMARY, COLOR_PRIMARY_HOVER, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY, COLOR_TEXT_MUTED,
    FONT_TITLE, FONT_SUBTITLE, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL, FONT_TINY
)

class GameScreen(tk.Frame):
    """Layar utama permainan simulasi smartphone."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_SCREEN_BG)
        self.controller = controller
        self.game_state = None

        # Build UI Container
        self.create_widgets()

    def set_game_state(self, game_state):
        self.game_state = game_state
        self.render_current_scenario()

    def create_widgets(self):
        # 1. Phone Top Bar (Status HP & Indikator Saldo/Awareness)
        self.status_bar_frame = tk.Frame(self, bg=COLOR_STATUS_BAR, padx=12, pady=6)
        self.status_bar_frame.pack(fill="x")

        # Top row: Jam, Sinyal, Baterai
        top_meta = tk.Frame(self.status_bar_frame, bg=COLOR_STATUS_BAR)
        top_meta.pack(fill="x")
        
        self.time_label = tk.Label(top_meta, text="14:30", font=FONT_TINY, fg=COLOR_TEXT_SECONDARY, bg=COLOR_STATUS_BAR)
        self.time_label.pack(side="left")

        battery_label = tk.Label(top_meta, text="📶 4G  🔋 92%", font=FONT_TINY, fg=COLOR_TEXT_SECONDARY, bg=COLOR_STATUS_BAR)
        battery_label.pack(side="right")

        # Bottom row: Saldo Tabungan & Awareness Bar
        stats_frame = tk.Frame(self.status_bar_frame, bg=COLOR_STATUS_BAR)
        stats_frame.pack(fill="x", pady=(4, 2))

        # Indikator Saldo
        self.lbl_savings = tk.Label(
            stats_frame, 
            text="💰 Saldo: Rp 5.000.000", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_SUCCESS, 
            bg=COLOR_STATUS_BAR
        )
        self.lbl_savings.pack(side="left")

        # Indikator Awareness
        self.lbl_awareness = tk.Label(
            stats_frame, 
            text="🛡️ Waspada: 70%", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_PRIMARY, 
            bg=COLOR_STATUS_BAR
        )
        self.lbl_awareness.pack(side="right")

        # Indikator Progress Kasus
        self.lbl_progress = tk.Label(
            self.status_bar_frame,
            text="Kasus 1 dari 8",
            font=FONT_TINY,
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_STATUS_BAR
        )
        self.lbl_progress.pack(pady=(2, 0))

        # 2. Chat Header (Info Pengirim Chat)
        self.chat_header = tk.Frame(self, bg=COLOR_CARD, padx=12, pady=8)
        self.chat_header.pack(fill="x")

        self.lbl_avatar = tk.Label(
            self.chat_header, 
            text="👤", 
            font=("Segoe UI Emoji", 20), 
            bg=COLOR_CARD
        )
        self.lbl_avatar.pack(side="left", padx=(0, 10))

        header_text_frame = tk.Frame(self.chat_header, bg=COLOR_CARD)
        header_text_frame.pack(side="left", fill="both", expand=True)

        self.lbl_sender_name = tk.Label(
            header_text_frame, 
            text="Nama Pengirim", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_CARD, 
            anchor="w"
        )
        self.lbl_sender_name.pack(fill="x")

        sender_sub_frame = tk.Frame(header_text_frame, bg=COLOR_CARD)
        sender_sub_frame.pack(fill="x")

        self.lbl_sender_number = tk.Label(
            sender_sub_frame, 
            text="+62 8xx-xxxx-xxxx", 
            font=FONT_TINY, 
            fg=COLOR_TEXT_SECONDARY, 
            bg=COLOR_CARD,
            anchor="w"
        )
        self.lbl_sender_number.pack(side="left")

        self.lbl_sender_tag = tk.Label(
            sender_sub_frame, 
            text="[Nomor Asing]", 
            font=FONT_TINY, 
            fg=COLOR_WARNING, 
            bg=COLOR_CARD,
            padx=4
        )
        self.lbl_sender_tag.pack(side="left", padx=(6, 0))

        # 3. Chat Messages Area (Scrollable Canvas)
        self.chat_container = tk.Frame(self, bg=COLOR_SCREEN_BG)
        self.chat_container.pack(fill="both", expand=True, padx=10, pady=6)

        self.chat_canvas = tk.Canvas(self.chat_container, bg=COLOR_SCREEN_BG, highlightthickness=0)
        self.chat_scrollbar = tk.Scrollbar(self.chat_container, orient="vertical", command=self.chat_canvas.yview)
        self.scrollable_chat = tk.Frame(self.chat_canvas, bg=COLOR_SCREEN_BG)

        self.scrollable_chat.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
        )

        self.canvas_window = self.chat_canvas.create_window((0, 0), window=self.scrollable_chat, anchor="nw", width=420)
        self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)

        self.chat_canvas.pack(side="left", fill="both", expand=True)
        self.chat_scrollbar.pack(side="right", fill="y")

        # 4. Action Area (Pilihan Keputusan Pemain)
        self.action_frame = tk.Frame(self, bg=COLOR_STATUS_BAR, padx=12, pady=10)
        self.action_frame.pack(fill="x", side="bottom")

        self.lbl_action_prompt = tk.Label(
            self.action_frame, 
            text="💡 Tentukan Tindakanmu:", 
            font=FONT_BODY_BOLD, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_STATUS_BAR,
            anchor="w"
        )
        self.lbl_action_prompt.pack(fill="x", pady=(0, 6))

        self.choice_buttons_frame = tk.Frame(self.action_frame, bg=COLOR_STATUS_BAR)
        self.choice_buttons_frame.pack(fill="x")

    def format_rupiah(self, amount: int) -> str:
        """Helper untuk format mata uang Rupiah."""
        return f"Rp {amount:,.0f}".replace(",", ".")

    def render_current_scenario(self):
        """Memperbarui tampilan dengan skenario kasus saat ini."""
        if not self.game_state:
            return

        scenario = self.game_state.current_scenario
        if not scenario:
            return

        # Update Status Bar
        self.lbl_savings.config(text=f"💰 Saldo: {self.format_rupiah(self.game_state.savings)}")
        
        # Beri warna dinamis untuk awareness
        aw = self.game_state.awareness
        aw_color = COLOR_SUCCESS if aw >= 60 else (COLOR_WARNING if aw >= 30 else COLOR_DANGER)
        self.lbl_awareness.config(text=f"🛡️ Waspada: {aw}%", fg=aw_color)
        
        self.lbl_progress.config(
            text=f"Kasus {self.game_state.current_index + 1} dari {self.game_state.total_scenarios} • Kategori: {scenario.category}"
        )

        # Update Header Info
        self.lbl_avatar.config(text=scenario.avatar_icon)
        self.lbl_sender_name.config(text=scenario.sender_name)
        self.lbl_sender_number.config(text=scenario.sender_number)
        
        tag_color = COLOR_WARNING if "Asing" in scenario.sender_tag or "Palsu" in scenario.sender_tag or "Bukan" in scenario.sender_tag else COLOR_SUCCESS
        self.lbl_sender_tag.config(text=f"[{scenario.sender_tag}]", fg=tag_color)

        # Bersihkan pesan lama di chat frame
        for widget in self.scrollable_chat.winfo_children():
            widget.destroy()

        # Date separator bubble
        date_lbl = tk.Label(
            self.scrollable_chat, 
            text="— Hari Ini 14:15 —", 
            font=FONT_TINY, 
            fg=COLOR_TEXT_MUTED, 
            bg=COLOR_SCREEN_BG
        )
        date_lbl.pack(pady=(4, 8))

        # Render Chat Bubbles
        for msg in scenario.messages:
            bubble = tk.Frame(self.scrollable_chat, bg=COLOR_CARD, padx=12, pady=8)
            bubble.pack(anchor="w", pady=4, padx=(0, 25), fill="none")

            msg_label = tk.Label(
                bubble, 
                text=msg, 
                font=FONT_BODY, 
                fg=COLOR_TEXT_PRIMARY, 
                bg=COLOR_CARD, 
                wraplength=340, 
                justify="left"
            )
            msg_label.pack(anchor="w")

        # Render Attachment jika ada
        if scenario.attachment:
            att = scenario.attachment
            att_frame = tk.Frame(
                self.scrollable_chat, 
                bg="#0F172A", 
                highlightbackground="#E11D48" if att.get("type") == "apk" else COLOR_PRIMARY,
                highlightthickness=1, 
                padx=10, 
                pady=8
            )
            att_frame.pack(anchor="w", pady=6, padx=(0, 25), fill="x")

            icon_text = "📦⚠️" if att.get("type") == "apk" else "🔗🌐"
            att_icon = tk.Label(att_frame, text=icon_text, font=("Segoe UI Emoji", 16), bg="#0F172A")
            att_icon.pack(side="left", padx=(0, 8))

            att_info = tk.Frame(att_frame, bg="#0F172A")
            att_info.pack(side="left", fill="both", expand=True)

            att_name = tk.Label(
                att_info, 
                text=att.get("name", ""), 
                font=FONT_BODY_BOLD, 
                fg="#F87171" if att.get("type") == "apk" else COLOR_PRIMARY, 
                bg="#0F172A", 
                anchor="w",
                wraplength=280
            )
            att_name.pack(fill="x")

            att_size = tk.Label(
                att_info, 
                text=f"Ukuran: {att.get('size', '-')} • {att.get('type', '').upper()}", 
                font=FONT_TINY, 
                fg=COLOR_TEXT_MUTED, 
                bg="#0F172A",
                anchor="w"
            )
            att_size.pack(fill="x")

        # Update Action Buttons
        for widget in self.choice_buttons_frame.winfo_children():
            widget.destroy()

        for idx, choice in enumerate(scenario.choices):
            btn = tk.Button(
                self.choice_buttons_frame,
                text=choice.text,
                font=FONT_BODY,
                bg=COLOR_CARD,
                fg=COLOR_TEXT_PRIMARY,
                activebackground=COLOR_CARD_LIGHT,
                activeforeground=COLOR_TEXT_PRIMARY,
                bd=0,
                relief="flat",
                cursor="hand2",
                wraplength=390,
                justify="left",
                anchor="w",
                padx=10,
                pady=6,
                command=lambda c=choice: self.handle_choice_selected(c)
            )
            btn.pack(fill="x", pady=3)

        # Scroll ke paling atas
        self.chat_canvas.yview_moveto(0)

    def handle_choice_selected(self, choice):
        """Memproses pilihan pemain dan menampilkan modal penjelasan edukasi."""
        result = self.game_state.apply_choice(choice)
        self.show_feedback_modal(result)

    def show_feedback_modal(self, result: dict):
        """Menampilkan dialog edukasi (Red Flags & Tips Keamanan) setelah mengambil keputusan."""
        choice = result["choice"]
        is_game_over = result["is_game_over"]

        # Buat Toplevel Popup di atas jendela utama
        modal = tk.Toplevel(self)
        modal.title("Analisis Keputusan")
        modal.geometry("420x580")
        modal.configure(bg=COLOR_SCREEN_BG)
        modal.transient(self.winfo_toplevel())
        modal.grab_set()  # Modal lock

        # Pusatkan modal di atas window utama
        main_x = self.winfo_toplevel().winfo_x()
        main_y = self.winfo_toplevel().winfo_y()
        modal.geometry(f"+{main_x + 20}+{main_y + 60}")

        container = tk.Frame(modal, bg=COLOR_SCREEN_BG, padx=16, pady=16)
        container.pack(fill="both", expand=True)

        # Header Hasil (Trap / Success / Cautious)
        header_color = COLOR_SUCCESS if choice.outcome_type == "success" else (
            COLOR_WARNING if choice.outcome_type == "cautious" else COLOR_DANGER
        )

        title_lbl = tk.Label(
            container, 
            text=choice.feedback_title, 
            font=FONT_SUBTITLE, 
            fg=header_color, 
            bg=COLOR_SCREEN_BG,
            wraplength=380,
            justify="center"
        )
        title_lbl.pack(pady=(0, 10))

        # Dampak Stat Box (Saldo & Awareness)
        impact_frame = tk.Frame(container, bg=COLOR_STATUS_BAR, padx=12, pady=8)
        impact_frame.pack(fill="x", pady=(0, 10))

        money_text = f"Saldo: {self.format_rupiah(choice.money_change)}" if choice.money_change != 0 else "Saldo: Tidak Berubah"
        money_color = COLOR_DANGER if choice.money_change < 0 else COLOR_SUCCESS
        lbl_money = tk.Label(impact_frame, text=money_text, font=FONT_BODY_BOLD, fg=money_color, bg=COLOR_STATUS_BAR)
        lbl_money.pack(side="left")

        aw_sign = "+" if choice.awareness_change > 0 else ""
        aw_text = f"Waspada: {aw_sign}{choice.awareness_change}%" if choice.awareness_change != 0 else "Waspada: Tetap"
        aw_color = COLOR_SUCCESS if choice.awareness_change > 0 else (COLOR_DANGER if choice.awareness_change < 0 else COLOR_TEXT_SECONDARY)
        lbl_aw = tk.Label(impact_frame, text=aw_text, font=FONT_BODY_BOLD, fg=aw_color, bg=COLOR_STATUS_BAR)
        lbl_aw.pack(side="right")

        # Feedback Message
        msg_lbl = tk.Label(
            container, 
            text=choice.feedback_message, 
            font=FONT_BODY, 
            fg=COLOR_TEXT_PRIMARY, 
            bg=COLOR_SCREEN_BG,
            wraplength=380,
            justify="left"
        )
        msg_lbl.pack(fill="x", pady=(0, 10))

        # Red Flags Box
        if choice.red_flags:
            flags_frame = tk.Frame(container, bg=COLOR_CARD, padx=10, pady=8)
            flags_frame.pack(fill="x", pady=(0, 10))

            flags_title = tk.Label(
                flags_frame, 
                text="🚩 Tanda Bahaya (Red Flags):", 
                font=FONT_BODY_BOLD, 
                fg=COLOR_WARNING, 
                bg=COLOR_CARD,
                anchor="w"
            )
            flags_title.pack(fill="x", pady=(0, 4))

            for rf in choice.red_flags:
                rf_lbl = tk.Label(
                    flags_frame, 
                    text=f"• {rf}", 
                    font=FONT_SMALL, 
                    fg=COLOR_TEXT_SECONDARY, 
                    bg=COLOR_CARD,
                    wraplength=350,
                    justify="left",
                    anchor="w"
                )
                rf_lbl.pack(fill="x", pady=1)

        # Safety Tips Box
        if choice.safety_tip:
            tip_frame = tk.Frame(container, bg="#1E3A8A", padx=10, pady=8)
            tip_frame.pack(fill="x", pady=(0, 15))

            tip_title = tk.Label(
                tip_frame, 
                text="💡 Tips Keamanan Nyata:", 
                font=FONT_BODY_BOLD, 
                fg="#93C5FD", 
                bg="#1E3A8A",
                anchor="w"
            )
            tip_title.pack(fill="x", pady=(0, 4))

            tip_lbl = tk.Label(
                tip_frame, 
                text=choice.safety_tip, 
                font=FONT_SMALL, 
                fg=COLOR_TEXT_PRIMARY, 
                bg="#1E3A8A",
                wraplength=350,
                justify="left",
                anchor="w"
            )
            tip_lbl.pack(fill="x")

        # Tombol Lanjut
        btn_next_text = "Lihat Rapor Akhir 📊" if is_game_over else "Pesan Berikutnya ➔"
        btn_next = tk.Button(
            container,
            text=btn_next_text,
            font=FONT_BODY_BOLD,
            bg=COLOR_PRIMARY,
            fg="#0F172A",
            activebackground=COLOR_PRIMARY_HOVER,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda: self.on_close_modal_and_proceed(modal, is_game_over)
        )
        btn_next.pack(fill="x", ipady=8, side="bottom")

    def on_close_modal_and_proceed(self, modal, is_game_over):
        modal.destroy()
        if is_game_over:
            # Simpan skor ke leaderboard
            self.game_state.save_high_score()
            self.controller.show_end_screen(self.game_state)
        else:
            has_next = self.game_state.next_scenario()
            if has_next:
                self.render_current_scenario()
            else:
                self.game_state.save_high_score()
                self.controller.show_end_screen(self.game_state)
