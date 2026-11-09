"""
Manajemen Status Permainan (Game State) & Logika Skor.
Mencakup File I/O untuk memuat skenario dan menyimpan leaderboard.
"""

import json
import os
from datetime import datetime
from config import (
    INITIAL_SAVINGS, INITIAL_AWARENESS, MAX_AWARENESS, MIN_AWARENESS,
    DATA_SCENARIOS_PATH, DATA_HIGHSCORES_PATH
)
from models.scenario import Scenario, Choice

class GameState:
    """Mengelola status pemain, alur permainan, dan persistensi data (File I/O)."""
    
    def __init__(self, player_name: str = "Pemain"):
        self.player_name = player_name
        self.savings = INITIAL_SAVINGS
        self.awareness = INITIAL_AWARENESS
        self.score = 0
        
        self.current_index = 0
        self.scenarios = []
        self.history = []  # Menyimpan riwayat setiap keputusan pemain
        
        self.correct_choices = 0
        self.traps_triggered = 0
        self.cautious_choices = 0
        
        self.is_game_over = False
        self.end_reason = ""  # 'bankrupt', 'zero_awareness', 'completed'
        
        self.load_scenarios()

    def load_scenarios(self):
        """Membaca skenario kasus dari file JSON (Materi File I/O)."""
        if not os.path.exists(DATA_SCENARIOS_PATH):
            raise FileNotFoundError(f"File skenario tidak ditemukan di {DATA_SCENARIOS_PATH}")
            
        with open(DATA_SCENARIOS_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.scenarios = [Scenario.from_dict(item) for item in data]

    @property
    def current_scenario(self) -> Scenario:
        """Mengambil skenario yang sedang aktif."""
        if 0 <= self.current_index < len(self.scenarios):
            return self.scenarios[self.current_index]
        return None

    @property
    def total_scenarios(self) -> int:
        return len(self.scenarios)

    def apply_choice(self, choice: Choice) -> dict:
        """
        Mengeksekusi pilihan pemain, menghitung dampak saldo, awareness, dan skor.
        Mengembalikan ringkasan hasil tindakan.
        """
        # Update Saldo
        old_savings = self.savings
        self.savings += choice.money_change
        if self.savings < 0:
            self.savings = 0
            
        # Update Awareness
        self.awareness = max(MIN_AWARENESS, min(MAX_AWARENESS, self.awareness + choice.awareness_change))
        
        # Hitung Penambahan Skor
        score_gain = 0
        if choice.outcome_type == "success":
            self.correct_choices += 1
            score_gain = 100 + (self.awareness // 2)
        elif choice.outcome_type == "cautious":
            self.cautious_choices += 1
            score_gain = 40
        else:  # trap
            self.traps_triggered += 1
            score_gain = 0
            
        self.score += score_gain

        # Catat Riwayat
        log_entry = {
            "scenario_id": self.current_scenario.id if self.current_scenario else "",
            "category": self.current_scenario.category if self.current_scenario else "",
            "choice_text": choice.text,
            "outcome_type": choice.outcome_type,
            "money_delta": choice.money_change,
            "awareness_delta": choice.awareness_change,
            "score_gain": score_gain
        }
        self.history.append(log_entry)

        # Cek Kondisi Game Over
        if self.savings <= 0:
            self.is_game_over = True
            self.end_reason = "bankrupt"
        elif self.awareness <= 0:
            self.is_game_over = True
            self.end_reason = "zero_awareness"
            
        return {
            "choice": choice,
            "score_gain": score_gain,
            "is_game_over": self.is_game_over,
            "end_reason": self.end_reason
        }

    def next_scenario(self) -> bool:
        """Pindah ke skenario berikutnya. Return True jika masih ada skenario."""
        self.current_index += 1
        if self.current_index >= len(self.scenarios):
            self.is_game_over = True
            self.end_reason = "completed"
            return False
        return True

    def calculate_final_rating(self) -> tuple:
        """Menghitung evaluasi gelar literasi keamanan digital pemain."""
        if self.end_reason == "bankrupt":
            return ("Korban Penipuan Digital", "🔴 Kamu kehilangan seluruh tabungan karena tergiur atau tertipu modus siber.")
        elif self.end_reason == "zero_awareness":
            return ("Sangat Rentan Kejahatan Siber", "🟠 Kewaspadaanmu habis dan terlalu mudah mempercayai pesan asing.")
        elif self.traps_triggered == 0 and self.correct_choices >= 6:
            return ("Cyber Security Sentinel (Ahli Anti-Scam)", "🌟 Sempurna! Kamu memiliki insting tajam dan tidak terkecoh oleh modus apapun.")
        elif self.traps_triggered <= 1:
            return ("Warga Digital Waspada", "🟢 Sangat baik! Kamu mengenali sebagian besar red flags dengan cerdas.")
        else:
            return ("Perlu Banyak Belajar Waspada", "🟡 Kamu masih sempat terjebak pada beberapa modus penipuan.")

    def save_high_score(self):
        """Menyimpan skor ke file highscores.json (File I/O)."""
        scores = self.get_high_scores()
        
        new_entry = {
            "name": self.player_name,
            "score": self.score,
            "savings": self.savings,
            "awareness": self.awareness,
            "correct": self.correct_choices,
            "traps": self.traps_triggered,
            "status": self.end_reason,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        scores.append(new_entry)
        # Urutkan berdasarkan skor tertinggi
        scores.sort(key=lambda x: x["score"], reverse=True)
        
        # Simpan maksimal 10 skor teratas
        scores = scores[:10]
        
        os.makedirs(os.path.dirname(DATA_HIGHSCORES_PATH), exist_ok=True)
        with open(DATA_HIGHSCORES_PATH, "w", encoding="utf-8") as file:
            json.dump(scores, file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_high_scores() -> list:
        """Membaca daftar leaderboard dari file JSON."""
        if not os.path.exists(DATA_HIGHSCORES_PATH):
            return []
        try:
            with open(DATA_HIGHSCORES_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return []
