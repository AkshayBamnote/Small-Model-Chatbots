class ChatMemory:
    """
    Handles chatbot memory using a sliding window mechanism.
    """
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.history = []

    def update(self, user_input, bot_reply):
        self.history.append((user_input, bot_reply))
        if len(self.history) > self.window_size:
            self.history.pop(0)

    def format_prompt(self, new_input):
        prompt = ""
        for user, bot in self.history:
            prompt += f"User: {user}\nBot: {bot}\n"
        prompt += f"User: {new_input}\nBot:"
        return prompt
