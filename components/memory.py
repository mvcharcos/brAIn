from datetime import datetime

class Memory:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append({
            "text": entry,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_state(self):
        return {"entries": self.entries}
