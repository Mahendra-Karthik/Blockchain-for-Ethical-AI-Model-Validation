from ai_model.factspeak_ai import get_fact_based_answer
from validator.truth_checker import check_truth
from blockchain.interact_with_contract import log_validation_result

def main():
    print("🧠 Welcome to FactSpeak AI Validator!")
    question = input("Enter your question: ")

    # Step 1: Get AI answerpython validate_and_view.py
    ai_answer = get_fact_based_answer(question)
    print(f"\n🤖 FactSpeak AI Answer:\n{ai_answer}\n")

    # Step 2: Validate truthfulness
    is_truthful, validation_message = check_truth(question, ai_answer)
    print(f"✅ Validation Result: {validation_message}\n")

    # Step 3: Log to blockchain
    log_validation_result(question, ai_answer, is_truthful)

if __name__ == "__main__":
    main()
