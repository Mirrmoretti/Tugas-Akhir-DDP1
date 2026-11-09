"""
Aplikasi Utama CyberShield (App Controller)
Mewarisi tk.Tk dan mengontrol perpindahan antar layar (Screen Manager).
Mengimplementasikan arsitektur OOP murni.
"""

import tkinter as tk
from config import PHONE_WIDTH, PHONE_HEIGHT, COLOR_BG_PHONE
from models.game_state import GameState
from ui.screens.start_screen import StartScreen
from ui.screens.game_screen import GameScreen
from ui.screens.end_screen import EndScreen
from ui.screens.leaderboard_screen import LeaderboardScreen

class CyberShieldApp(tk.Tk):
    """Kelas controller utama aplikasi Tkinter."""

    def __init__(self):
        super().__init__()

        # Konfigurasi Window
        self.title("CyberShield: Phone Simulator | Edukasi Anti-Scam")
        self.geometry(f"{PHONE_WIDTH}x{PHONE_HEIGHT}")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG_PHONE)

        # Pusatkan window di tengah layar monitor
        self.center_window(PHONE_WIDTH, PHONE_HEIGHT)

        # Kontainer Utama untuk Layar
        self.main_container = tk.Frame(self, bg=COLOR_BG_PHONE)
        self.main_container.pack(fill="both", expand=True)

        # Inisialisasi Layar-layar
        self.start_screen = StartScreen(self.main_container, self)
        self.game_screen = GameScreen(self.main_container, self)
        self.end_screen = EndScreen(self.main_container, self)
        self.leaderboard_screen = LeaderboardScreen(self.main_container, self)

        # State aktif
        self.current_game_state = None

        # Tampilkan Layar Awal
        self.show_start_screen()

    def center_window(self, width: int, height: int):
        """Menempatkan jendela aplikasi di tengah layar pengguna."""
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) - 20
        self.geometry(f"{width}x{height}+{x}+{max(10, y)}")

    def hide_all_screens(self):
        """Menyembunyikan seluruh layar sebelum menampilkan layar yang dipilih."""
        self.start_screen.pack_forget()
        self.game_screen.pack_forget()
        self.end_screen.pack_forget()
        self.leaderboard_screen.pack_forget()

    def show_start_screen(self):
        """Menampilkan menu awal."""
        self.hide_all_screens()
        self.start_screen.pack(fill="both", expand=True)

    def start_new_game(self, player_name: str):
        """Membuat instance GameState baru dan memulai permainan."""
        self.current_game_state = GameState(player_name=player_name)
        self.hide_all_screens()
        self.game_screen.set_game_state(self.current_game_state)
        self.game_screen.pack(fill="both", expand=True)

    def show_end_screen(self, game_state: GameState):
        """Menampilkan layar evaluasi akhir / rapor permainan."""
        self.hide_all_screens()
        self.end_screen.set_game_state(game_state)
        self.end_screen.pack(fill="both", expand=True)

    def show_leaderboard_screen(self):
        """Menampilkan layar papan skor."""
        self.hide_all_screens()
        self.leaderboard_screen.refresh_scores()
        self.leaderboard_screen.pack(fill="both", expand=True)
