class Curiosity:
    def __init__(self):
        self.rules = """Always looking for lowest consumption.
Always looking for lowest amount of actions.
Always looking for optimal luminosity in the room."""

    def generate_prompt(self, actions):
        actions_list = actions.split("\n")
        actions_list = [action.strip() for action in actions_list if action.strip()]

        prompt = (
            f"What actions would I choose among {actions_list} knowing that I always try to follow "
            f"the following rules? Please send just the list of actions that I will try without further "
            f"explanation. I do not want the list of possible actions but that you select randomly considering "
            f"the rules either one of the actions or the two.\n\n{self.rules}"
        )
        return {"prompt": prompt}
