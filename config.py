"""
Konfigurasi Game CyberShield: Phone Simulator
Menyimpan konstanta warna, font, dimensi layar HP, dan aturan permainan.
"""

# Dimensi Layar Smartphone Simulator
PHONE_WIDTH = 460
PHONE_HEIGHT = 760

# Palette Warna (Modern Dark/Light Smartphone UI)
COLOR_BG_PHONE = "#0F172A"       # Slate 900 (Warna bodi HP)
COLOR_STATUS_BAR = "#090D16"     # Top bar status HP
COLOR_SCREEN_BG = "#1E293B"      # Slate 800 (Background layar chat)
COLOR_CARD = "#334155"           # Slate 700 (Card pesan/kontainer)
COLOR_CARD_LIGHT = "#475569"     # Slate 600

COLOR_TEXT_PRIMARY = "#F8FAFC"   # Putih terang
COLOR_TEXT_SECONDARY = "#94A3B8" # Abu-abu terang
COLOR_TEXT_MUTED = "#64748B"     # Abu-abu redup

COLOR_PRIMARY = "#38BDF8"        # Sky Blue (Aksen utama / tombol)
COLOR_PRIMARY_HOVER = "#0284C7"
COLOR_SUCCESS = "#22C55E"        # Hijau (Pilihan aman/berhasil)
COLOR_WARNING = "#F59E0B"        # Kuning/Amber (Hati-hati)
COLOR_DANGER = "#EF4444"         # Merah (Kena tipu / bahaya)

COLOR_BUBBLE_INCOMING = "#1E293B"# Bubble pesan lawan bicara
COLOR_BUBBLE_BORDER = "#334155"
COLOR_ATTACHMENT_BG = "#0F172A"

# Font Settings (Gunakan font standar Windows/Cross-platform)
FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 16, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 12, "bold")
FONT_BODY = (FONT_FAMILY, 10)
FONT_BODY_BOLD = (FONT_FAMILY, 10, "bold")
FONT_SMALL = (FONT_FAMILY, 9)
FONT_TINY = (FONT_FAMILY, 8)

# Konfigurasi Awal Permainan
INITIAL_SAVINGS = 5_000_000      # Rp 5.000.000 saldo awal
INITIAL_AWARENESS = 70           # 70% tingkat kewaspadaan awal (0 - 100)
MAX_AWARENESS = 100
MIN_AWARENESS = 0

# Path Data Lokal (100% Offline di Komputer / Mesin Pengguna)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_SCENARIOS_PATH = os.path.join(DATA_DIR, "scenarios.json")
DATA_HIGHSCORES_PATH = os.path.join(DATA_DIR, "local_highscores.json")

