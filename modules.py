import dspy
from signatures import TurnClassification, PlayerInstruction, Assess

class ClassifyTurns(dspy.Module):
  def __init__(self):
    self.classifier = dspy.ChainOfThought(TurnClassification, caching = False)
    #self.generator = dspy.ChainOfThought(PlayerInstruction, caching = False)

  def forward(self, examples, **kwargs):
    behaviour = self.classifier(examples=examples).behaviour_class
    #prompt = self.generator(examples=examples).instruction
    return prompt

class ScorePrompt(dspy.Module):
  def __init__(self):
    self.assessment = dspy.ChainOfThought(Assess, caching=False)

  def forward(self, prompt_list, **kwargs):
    score_list = []
    for i in prompt_list:
      assess_clarity = self.assessment(assessed_text=i, assessment_question="Is the assessed prompt specific, unambiguous and easy to interpret?").assessment_answer
      assess_relevance = self.assessment(assessed_text=i, assessment_question="Does the prompt align with the categorised quality of D&D player behaviour that it is trying to express?").assessment_answer
      assess_correctness = self.assessment(assessed_text=i, assessment_question="Is the assessed prompt correct with respect to the player quality that it is describing?").assessment_answer
      assess_completeness = self.assessment(assessed_text=i, assessment_question="Does the prompt fully express the quality of the player's behaviour, taking into account additional context or secondary queries that might have been implied or included in the prompt?").assessment_answer

      if assess_clarity == True:
        assess_clarity = 1
      else:
        assess_clarity = 0
      if assess_relevance == True:
        assess_relevance = 1
      else:
        assess_relevance = 0
      if assess_correctness == True:
        assess_correctness = 1
      else:
        assess_correctness = 0
      if assess_completeness == True:
        assess_completeness = 1
      else:
        assess_completeness = 0

      score = (assess_clarity + assess_relevance + assess_correctness + assess_completeness)/4
      score_list.append(score)

    return score_list
