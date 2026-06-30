import argparse

from modules import AgentProfile, TwoAgentConversation, configure_lm


DEFAULT_SCENARIO = (
    "Charlie owns the Wizard Tower Brewing Company. Alice and Bob are adventurers "
    "asked to investigate a rat infestation in the brewery basement. Charlie warns "
    "them that simply charging downstairs may be dangerous."
)


def build_conversation() -> TwoAgentConversation:
    alice = AgentProfile(
        name="Alice",
        character="Alice, a direct dwarf barbarian who prefers practical action.",
        instructions=(
            "Push the scene forward, cooperate with the other player, and suggest "
            "clear actions when the group needs momentum."
        ),
    )
    bob = AgentProfile(
        name="Bob",
        character="Bob, a careful wizard who asks questions before taking risks.",
        instructions=(
            "Respond thoughtfully, gather useful information, and collaborate with "
            "the other player before committing to dangerous actions."
        ),
    )
    return TwoAgentConversation(
        agent_a=alice,
        agent_b=bob,
        scenario=DEFAULT_SCENARIO,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run two D&D DSPy agents together.")
    parser.add_argument(
        "--opening-message",
        default="I think we should inspect the basement door before we rush in.",
        help="The first turn spoken by Alice.",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=4,
        help="Number of replies to generate after the opening message.",
    )
    parser.add_argument("--model", default="ollama_chat/qwen3:8b")
    parser.add_argument("--api-base", default="http://localhost:11434")
    args = parser.parse_args()

    configure_lm(model=args.model, api_base=args.api_base)
    conversation = build_conversation()
    for turn in conversation.run(args.opening_message, rounds=args.rounds):
        print(turn)


if __name__ == "__main__":
    main()
