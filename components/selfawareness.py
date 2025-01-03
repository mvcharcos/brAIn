class SelfAwareness:
    def get_state(self):
        return {
            "text": """
            Have two lamps in a room.
            Can turn on and off lamp1. This is an active action.
            Can turn on and off lamp2. This is an active action.
            Can measure consumption of lamp 1. This is a passive action.
            Can measure consumption of lamp 2. This is a passive action.
            Can measure the level of luminosity in the room. This is a passive action.
            """
        }
