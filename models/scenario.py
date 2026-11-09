"""
Model data untuk Skenario dan Pilihan Aksi dalam game.
"""

class Choice:
    """Mewakili opsi tindakan yang dapat dipilih oleh pemain."""
    def __init__(self, text: str, outcome_type: str, feedback_title: str, 
                 feedback_message: str, money_change: int, awareness_change: int, 
                 red_flags: list, safety_tip: str):
        self.text = text
        self.outcome_type = outcome_type  # 'success', 'trap', 'cautious'
        self.feedback_title = feedback_title
        self.feedback_message = feedback_message
        self.money_change = money_change
        self.awareness_change = awareness_change
        self.red_flags = red_flags
        self.safety_tip = safety_tip

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            text=data.get("text", ""),
            outcome_type=data.get("outcome_type", "trap"),
            feedback_title=data.get("feedback_title", ""),
            feedback_message=data.get("feedback_message", ""),
            money_change=data.get("money_change", 0),
            awareness_change=data.get("awareness_change", 0),
            red_flags=data.get("red_flags", []),
            safety_tip=data.get("safety_tip", "")
        )


class Scenario:
    """Mewakili satu kasus/pesan penipuan atau pesan sah yang masuk."""
    def __init__(self, id_scenario: str, category: str, sender_name: str, 
                 sender_number: str, sender_tag: str, avatar_icon: str,
                 messages: list, attachment: dict, choices: list):
        self.id = id_scenario
        self.category = category
        self.sender_name = sender_name
        self.sender_number = sender_number
        self.sender_tag = sender_tag
        self.avatar_icon = avatar_icon
        self.messages = messages
        self.attachment = attachment  # Dict: {'name': ..., 'type': 'apk'/'link'/'image', 'size': ...}
        self.choices = [Choice.from_dict(c) if isinstance(c, dict) else c for c in choices]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_scenario=data.get("id", ""),
            category=data.get("category", "Umum"),
            sender_name=data.get("sender_name", "Anonim"),
            sender_number=data.get("sender_number", "-"),
            sender_tag=data.get("sender_tag", "Nomor Tidak Dikenal"),
            avatar_icon=data.get("avatar_icon", "👤"),
            messages=data.get("messages", []),
            attachment=data.get("attachment", None),
            choices=data.get("choices", [])
        )
