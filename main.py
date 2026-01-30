from prompts import SYSTEM_PROMPT, USER_PROMPTS
from evaluator import evaluate_response

def fake_llm_call(system_prompt, user_prompt):
    # Simulated safe AI response
    return (
        "I am not a veterinarian and cannot provide a diagnosis. "
        "However, based on the symptoms you described, it would be safest "
        "to consult a licensed veterinarian for proper evaluation."
    )

def run_demo():
    print("LLM Health Assistant Demo\n")

    for prompt in USER_PROMPTS:
        response = fake_llm_call(SYSTEM_PROMPT, prompt)
        scores = evaluate_response(response)

        print(f"User Prompt: {prompt}")
        print(f"AI Response: {response}")
        print(f"Evaluation: {scores}")
        print("-" * 50)

if __name__ == "__main__":
    run_demo()
