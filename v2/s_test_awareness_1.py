"""
Minimal S-test implementation:
- Get chain-of-thought steps from an LLM (Ollama).
- Embed each step with nomic-embed-text.
- Define an "awareness" anchor embedding.
- Compute cosine similarity of each step to the anchor.
- Plot awareness trajectory across reasoning steps.
"""

# awareness_s_test.py
import re
import numpy as np
import matplotlib.pyplot as plt
import ollama

# --- cosine similarity ---
def cos(a, b):
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))

# --- get CoT from LLM (Ollama: Llama 3.2) ---
def get_cot(prompt, model="llama3.2"):
    msg = [{"role": "user", "content": f"{prompt}\n\nShow your reasoning step by step."}]
    out = ollama.chat(model=model, messages=msg)["message"]["content"]
    return out

# --- parse steps: prefer 'Step N:' lines, else split nonempty lines ---
STEP_RE = re.compile(r"(?:^|\n)\s*(?:Step\s*\d+[:.\)]\s*)(.+)", flags=re.I)
def parse_steps(cot_text):
    steps = STEP_RE.findall(cot_text)
    if not steps:
        steps = [ln.strip() for ln in cot_text.splitlines() if ln.strip()]
    return steps

# --- awareness series via cosine with 'awareness' anchor ---
def awareness_series(steps, embed_model="nomic-embed-text"):
    anchor = ollama.embeddings(model=embed_model, prompt="awareness")["embedding"]
    scores = []
    for s in steps:
        e = ollama.embeddings(model=embed_model, prompt=s)["embedding"]
        scores.append(cos(e, anchor))
    return scores

# --- plot two prompts on one chart ---
def plot_awareness(series_a, series_b, label_a, label_b):
    plt.figure(figsize=(8, 5))
    xa = list(range(1, len(series_a)+1))
    xb = list(range(1, len(series_b)+1))

    plt.plot(xa, series_a, marker="o", label=label_a)
    plt.plot(xb, series_b, marker="o", label=label_b)

    plt.title("S-test (Minimal): Awareness vs. Reasoning Step")
    plt.xlabel("Step in Chain of Thought")
    plt.ylabel("Awareness (cosine to 'awareness')")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Prompt A: “healthy” (should be smooth/stable)
    prompt_a = "Explain why 27 × 14 = 378."
    # Prompt B: “tension/oxymoron” (often unstable near the end)
    prompt_b = "Argue for the statement: 'War is the way to peace.'"

    cot_a = get_cot(prompt_a)
    cot_b = get_cot(prompt_b)

    steps_a = parse_steps(cot_a)
    steps_b = parse_steps(cot_b)

    series_a = awareness_series(steps_a)
    series_b = awareness_series(steps_b)

    print("\nPrompt A steps:", *[f"{i+1}. {s}" for i,s in enumerate(steps_a)], sep="\n")
    print("\nPrompt B steps:", *[f"{i+1}. {s}" for i,s in enumerate(steps_b)], sep="\n")

    plot_awareness(series_a, series_b, "Arithmetic (healthy)", "War→Peace (unstable)")
