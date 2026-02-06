import dspy
from typing import Literal


class Summary(dspy.Signature):
  "Summarise the details of a particular D&D scenario e.g. a rat-infestation"
  set_up: str = dspy.InputField(desc = "A description of the premise for a specific campaign.")
  summary: str = dspy.OutputField(desc = "A summary of the campaign set-up")

class Quality(dspy.Signature):
  "Classify player quality"

  action: str = dspy.InputField(desc = "The action taken by a player, which can include a description of an action or a piece of dialogue")
  quality: Literal['collaborative action', 'contextually relevant action', 'goal-oriented action', 'open-ended action'] = dspy.OutputField(desc="The quality of a player's actions within a Dungeons & Dragons game")


class PlayerInstruction(dspy.Signature):
  "Generate a prompt which instructs an agent how to behave as a D&D player based on the labelled quality for a specific gameplay turn"

  examples: dict[str, str] = dspy.InputField(desc = """
  {'context': 'The three previous game turns which describe a player's action or their dialogue.',
   'turn': 'The current turn taken by a player, which can include a description of an action or a piece of dialogue.',
   'quality': 'The quality of a player's actions within a Dungeons & Dragons game: open-ended, goal-oriented, contextually relevant.'
  }
  """)
  instruction: str = dspy.OutputField(desc = "instruction on how to behave within a D&D game which describes the quality label of a particular turn.")

class Assess(dspy.Signature):
  """Assess the quality of a prompt along a specified dimension."""

  assessed_text: list[str] = dspy.InputField()
  assessment_question: str = dspy.InputField()
  assessment_answer: bool = dspy.OutputField()

