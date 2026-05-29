from pathlib import Path
import json


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]
AI_OUTPUT_PATH = BASE_PATH / "data" / "ai_outputs"
AI_DOCUMENTS_PATH = AI_OUTPUT_PATH / "claim_ai_documents.json"


# ------------------------------------------------------------
# Load AI-ready claim documents
# ------------------------------------------------------------

def load_claim_documents():
    if not AI_DOCUMENTS_PATH.exists():
        raise FileNotFoundError(
            "claim_ai_documents.json not found. "
            "Please run notebooks/06_ai_claim_intelligence.py first."
        )

    with open(AI_DOCUMENTS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# ------------------------------------------------------------
# Simple local Q&A logic
# ------------------------------------------------------------

def answer_claim_question(question, documents):
    """
    A lightweight local Q&A agent over AI-ready claim documents.

    This does not use an LLM.
    It demonstrates how natural-language questions can be mapped
    to filters over trusted Gold/PIT claim data.
    """

    question_lower = question.lower()
    results = documents.copy()

    # Filter by claim status
    if "open" in question_lower:
        results = [
            doc for doc in results
            if doc.get("claim_status", "").lower() == "open"
        ]

    if "closed" in question_lower:
        results = [
            doc for doc in results
            if doc.get("claim_status", "").lower() == "closed"
        ]

    if "reopened" in question_lower:
        results = [
            doc for doc in results
            if doc.get("claim_status", "").lower() == "reopened"
        ]

    # Filter by severity
    if "high severity" in question_lower or "high-severity" in question_lower:
        results = [
            doc for doc in results
            if doc.get("severity", "").lower() == "high"
        ]

    if "medium severity" in question_lower or "medium-severity" in question_lower:
        results = [
            doc for doc in results
            if doc.get("severity", "").lower() == "medium"
        ]

    if "low severity" in question_lower or "low-severity" in question_lower:
        results = [
            doc for doc in results
            if doc.get("severity", "").lower() == "low"
        ]

    # Filter by review priority
    if "high review" in question_lower or "review priority" in question_lower or "management review" in question_lower:
        results = [
            doc for doc in results
            if doc.get("review_priority", "").lower() == "high"
        ]

    # Filter by region
    known_regions = ["europe", "north america", "apac", "middle east"]

    for region in known_regions:
        if region in question_lower:
            results = [
                doc for doc in results
                if doc.get("region", "").lower() == region
            ]

    # Filter by valuation date
    if "2024-06-30" in question_lower:
        results = [
            doc for doc in results
            if doc.get("valuation_date") == "2024-06-30"
        ]

    if "2024-12-31" in question_lower or "year end" in question_lower or "year-end" in question_lower:
        results = [
            doc for doc in results
            if doc.get("valuation_date") == "2024-12-31"
        ]

    # Filter by financial exposure keywords
    if (
        "high exposure" in question_lower
        or "financial exposure" in question_lower
        or "high incurred" in question_lower
        or "incurred amount above" in question_lower
        or "large incurred" in question_lower
    ):
        results = [
            doc for doc in results
            if float(doc.get("incurred_amount", 0)) >= 25000
        ]

    if "high reserve" in question_lower or "reserve exposure" in question_lower:
        results = [
            doc for doc in results
            if float(doc.get("reserve_amount", 0)) >= 15000
        ]

    # Sort by incurred amount descending
    results = sorted(
        results,
        key=lambda doc: float(doc.get("incurred_amount", 0)),
        reverse=True
    )

    return results


# ------------------------------------------------------------
# Format response
# ------------------------------------------------------------

def format_agent_response(question, results, max_records=5):
    if not results:
        return (
            "\nNo matching claims found for the question.\n"
            "Try asking about open claims, high severity claims, high review priority, "
            "Europe, year-end, high reserve, or high incurred claims.\n"
        )

    response_lines = []

    response_lines.append("\nQuestion:")
    response_lines.append(question)

    response_lines.append("\nAgent Response:")
    response_lines.append(
        f"I found {len(results)} matching claim record(s). "
        f"Showing top {min(len(results), max_records)} by incurred amount."
    )

    response_lines.append("\nTop Matching Claims:")

    for idx, doc in enumerate(results[:max_records], start=1):
        response_lines.append("")
        response_lines.append(f"{idx}. Claim Number: {doc['claim_number']}")
        response_lines.append(f"   Valuation Date: {doc['valuation_date']}")
        response_lines.append(f"   Status: {doc['claim_status']}")
        response_lines.append(f"   Severity: {doc['severity']}")
        response_lines.append(f"   Region: {doc['region']}")
        response_lines.append(f"   Paid Amount: {doc['paid_amount']:.2f}")
        response_lines.append(f"   Reserve Amount: {doc['reserve_amount']:.2f}")
        response_lines.append(f"   Incurred Amount: {doc['incurred_amount']:.2f}")
        response_lines.append(f"   Review Priority: {doc['review_priority']}")
        response_lines.append(f"   Summary: {doc['claim_summary']}")

    return "\n".join(response_lines)


# ------------------------------------------------------------
# Main interactive loop
# ------------------------------------------------------------

def main():
    documents = load_claim_documents()

    print("Local Claims Q&A Agent")
    print("----------------------")
    print("This agent answers questions using AI-ready PIT claim documents.")
    print("Type 'exit' to stop.")
    print("")
    print("Example questions:")
    print("- Which open claims have high financial exposure as of 2024-12-31?")
    print("- Show high severity claims requiring management review.")
    print("- Find claims in Europe with high reserve exposure.")
    print("- Which claims have high review priority?")
    print("- Show year-end claims with high incurred amount.")
    print("")

    while True:
        question = input("Ask a claims question: ").strip()

        if question.lower() in ["exit", "quit", "q"]:
            print("Exiting local claims Q&A agent.")
            break

        results = answer_claim_question(question, documents)
        response = format_agent_response(question, results)

        print(response)
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    main()