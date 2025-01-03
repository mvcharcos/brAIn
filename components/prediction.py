class Prediction:
    def __init__(self, memory, selfawareness, environment, reference):
        self.memory = memory
        self.selfawareness = selfawareness
        self.environment = environment
        self.reference = reference

    def generate_prompt(self):
        memory_data = "\n".join(
            f"{entry['date']}: {entry['text']}" for entry in self.memory.get_state()["entries"]
        )
        selfawareness_text = self.selfawareness.get_state()["text"]
        reference_text = self.reference.get_state()["text"]
        environment_state = self.environment.get_state()

        prompt = (
            f"What are the individual active actions (no consecutive actions) that I can take "
            f"from the current state to learn something new from the system knowing the following, "
            f"rules, and initial state? Filter actions strictly based on the initial state rather than listing all possible actions. "
            f"Please make just a list without further comments.\n\n"
            f"The current state of the system is represented by the following json: {environment_state}\n\n"
            f"I am a system with the following functionalities: \n {selfawareness_text}\n\n"
            f"I always try to follow the following rules: \n {reference_text}\n\n"
            f"I know the following:\n{memory_data}"
        )
        return {"prompt": prompt}
