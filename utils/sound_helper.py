"""
Modul Efek Suara (Audio Feedback) untuk CyberShield.
Menggunakan modul bawaan Windows (winsound) dengan fallback aman
agar tetap berjalan lancar di macOS/Linux tanpa error.
"""

import threading

try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False


def _play_async(func):
    """Menjalankan suara di thread terpisah agar tampilan GUI tidak lag."""
    threading.Thread(target=func, daemon=True).start()


def play_notification():
    """Suara notifikasi chat masuk / pilihan hati-hati."""
    def _beep():
        if HAS_WINSOUND:
            winsound.Beep(880, 110)
            winsound.Beep(1175, 160)
    _play_async(_beep)


def play_success():
    """Nada positif saat pemain mengambil keputusan aman."""
    def _beep():
        if HAS_WINSOUND:
            winsound.Beep(523, 100)  # C5
            winsound.Beep(659, 100)  # E5
            winsound.Beep(784, 180)  # G5
    _play_async(_beep)


def play_trap():
    """Suara peringatan bahaya saat pemain terjebak scam."""
    def _beep():
        if HAS_WINSOUND:
            winsound.Beep(320, 220)
            winsound.Beep(220, 350)
    _play_async(_beep)