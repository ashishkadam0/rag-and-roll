"""Small examples of core LLM concepts without calling a paid API."""


def estimate_tokens(text):
    """Use a rough estimate; production apps should use a model tokenizer."""
    return max(1, len(text) // 4)


def build_messages(user_question):
    """Create the role-based message structure used by chat APIs."""
    return [
        {
            "role": "system",
            "content": (
                "You are an AI engineering tutor. Answer concisely and return "
                "three bullet points."
            ),
        },
        {
            "role": "user",
            "content": user_question,
        },
    ]


question = "How does retrieval-augmented generation reduce hallucinations?"
messages = build_messages(question)

for message in messages:
    print(f"{message['role'].upper()}: {message['content']}")

input_text = " ".join(message["content"] for message in messages)
estimated_input_tokens = estimate_tokens(input_text)
maximum_context_tokens = 128000
reserved_output_tokens = 500

fits_context_window = (
    estimated_input_tokens + reserved_output_tokens <= maximum_context_tokens
)

print(f"\nEstimated input tokens: {estimated_input_tokens}")
print(f"Fits context window: {fits_context_window}")

# Important concepts:
# - Temperature controls randomness; lower values favor consistency.
# - Top-P limits generation to the most likely group of next tokens.
# - Structured output constrains a response to a required schema.
# - Embeddings represent meaning as vectors for semantic similarity searches.
# - RAG retrieves relevant knowledge and adds it to the model's prompt.
# - An agent combines an LLM with tools and a decision-making loop.
#
# Exercise:
# Update build_messages() with a one-shot example: add a user message containing
# an example question and an assistant message containing its expected answer
# before the final user question.
