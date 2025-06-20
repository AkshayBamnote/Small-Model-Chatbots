from model_loader import load_model_and_tokenizer_pipeline
from chat_memory import ChatMemory

def main():
    print("🚀 Starting CLI Chatbot...")

    model_id = "tiiuae/falcon-rw-1b"
    text_generator = load_model_and_tokenizer_pipeline(model_id)

    memory = ChatMemory(window_size=3)

    print(f"Chatbot using '{model_id}' is running. Type '/exit' to stop.\n")

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        prompt = memory.format_prompt(user_input)
        response = text_generator(prompt, max_new_tokens=150, top_p=0.9, temperature=0.7)

        full_generated = response[0]["generated_text"]
        bot_reply = full_generated[len(prompt):].strip().split("\n")[0]

        print(f"Bot: {bot_reply}")
        memory.update(user_input, bot_reply)

if __name__ == "__main__":
    main()
