from __future__ import annotations

import argparse

from modules import AgentProfile, TwoAgentConversation, configure_lm

DEFAULT_SCENARIO = (
    "Charlie owns Wizard Tower Brewing Company and needs help with a rat infestation "
    "in the brewery basement. Alice and Bob are adventurers deciding how to proceed."
)
DEFAULT_OPENING = "I think we should ask Charlie what he has seen before we go downstairs."


def build_demo_conversation() -> TwoAgentConversation:
    return TwoAgentConversation(
        agent_a=AgentProfile(
            name="Alice",
            character="Alice, a direct dwarf barbarian who prefers practical action.",
            instructions="Use first-person limited perspective and push for concrete next steps.",
        ),
        agent_b=AgentProfile(
            name="Bob",
            character="Bob, a cautious but curious adventurer.",
            instructions="Use first-person limited perspective and ask useful questions before taking risks.",
        ),
        scenario=DEFAULT_SCENARIO,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run two DSPy D&D player agents in conversation.")
    parser.add_argument("--rounds", type=int, default=4, help="Number of generated turns after the opening.")
    parser.add_argument("--model", default="ollama_chat/qwen3:8b", help="DSPy model identifier.")
    parser.add_argument("--api-base", default="http://localhost:11434", help="Local model API base URL.")
    args = parser.parse_args()

    configure_lm(model=args.model, api_base=args.api_base)
    conversation = build_demo_conversation()
    for line in conversation.run(opening_message=DEFAULT_OPENING, rounds=args.rounds):
        print(line)


if __name__ == "__main__":
    main()
