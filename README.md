
# 🤖 Command-Line Chatbot with Hugging Face (Falcon-rw-1b)

This project is a lightweight, fully functional command-line chatbot built using Hugging Face's `transformers` library. It uses a sliding window memory to maintain conversational context and supports multi-turn dialogue.

The chatbot loads a small language model locally and runs without needing an instruction-specific format — perfect for quick, natural conversations like:

```
User: What is the capital of France?
Bot: The capital of France is Paris.
User: And what about Italy?
Bot: The capital of Italy is Rome.
```

---

## 📂 Project Structure

```
├── model_loader.py      # Loads model and tokenizer via Hugging Face pipeline
├── chat_memory.py       # Manages chatbot memory (last 3 turns)
├── interface.py         # Main CLI logic and interaction loop
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone or Download this Repository**

2. **Install Dependencies**

```bash
pip install transformers torch
```

3. **Run the Chatbot**

```bash
python interface.py
```

---

## 💬 Sample Interactions

### ⚡ Example 1:
![Example 1](Screenshot%202025-06-20%20161424.png)

### ⚡ Example 2:
![Example 2](Screenshot%202025-06-20%20163055.png)

---

## 🤔 Models Tried & Issues Faced

### 🔁 Tried:

1. **`distilgpt2`**
   - ✅ Very lightweight
   - ❌ Repetitive outputs
   - ❌ Poor factual accuracy (e.g., wrong capitals)

2. **`microsoft/phi-1_5`**
   - ✅ Instruction-tuned
   - ❌ Required very specific prompts like `Instruction: ... Response:`
   - ❌ Not suitable for `User: ... Bot:` style without fine-tuning

3. **`mistralai/Mistral-7B-Instruct-v0.1`**
   - ✅ High-quality responses
   - ❌ Too large for local testing or CPU environments
   - ❌ Required gated access & higher RAM/VRAM

---

## ✅ Final Model Chosen

### ✔️ `tiiuae/falcon-rw-1b`

- ✅ Lightweight (~1.3B parameters)
- ✅ Runs smoothly on CPU or GPU
- ✅ Supports conversational format:
  ```
  User: Question
  Bot: Answer
  ```
- ✅ No special prompt tokens required
- ✅ Best balance of speed, size, and quality

---

## 📈 For Improved Stability and Accuracy

For more consistent, factually accurate, and instruction-following results, especially in multi-turn conversations, you may switch to larger and instruction-tuned models like:

- 🔹 `mistralai/Mistral-7B-Instruct-v0.1`
- 🔹 `openchat/openchat-3.5-0106`

These models offer significantly better contextual understanding, but require GPUs and more memory to run smoothly.

---

## 🎥 Note on Demo Video

Due to a tight deadline and a facecam hardware issue on my laptop, I was unable to record and submit a demo video for this assignment. All code and interactions have been tested thoroughly in a local environment and are fully functional.

---

## 📬 Author

Akshay Bamnote  
B.Tech AI & ML | Final Year | MPSTME, NMIMS  
