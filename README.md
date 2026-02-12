### Background 

- According to Attardo 2019 (https://benjamins.com/catalog/pbns.302.08att) and Sridharan 2022 (https://studenttheses.uu.nl/handle/20.500.12932/41993), the default mode of communication within Dungeons & Dragons is "purposeful, goal-oriented, communicative cooperation" with disruptions to this mode being for humorous utterances.
- Players engaging in humour with each other would return to the default mode as soon as possible in a tendency described by the "least disruption" principle (Attardo 2019).
- This is different from conversational repair which targets undesirable conversational violations.
- In the context of  LLM-human hybrid roleplay, engaging in "open-ended" (not goal-oriented) conversations about e.g. backstories, ideals, anecdotes and general chit-chat demonstrates desirable conversation violation which should follow the "least disruption" principle. 
- Thus the features of D&D turns are split broadly two ways:
	- "purposeful, goal-oriented and communicative cooperation"
	- "open-ended" roleplay

### Data
- The dataset we use is the Critical Role Dungeons & Dragons Dataset (CRD3) which is the largest open-source dataset of D&D actual play comprising 398,682 transcribed dialogue turns. Specifically we use a modified version of CRD3 with the following columns:
	- Current turn: the present turn that a player takes during actual play.
	- Context: the three previous turns by other players or DM before the player takes their turn. 
### Formalising Turn Classification
- We classify features of player turns in CRD3 with the following categories (which apply to a player's role rather than the DM's role):
	- Goal-oriented turn: player takes an action or utters dialogue which aims at progressing the group towards their common goals. 
	- Cooperative turn: player aids another player directly by taking an action or uttering dialogue that provides helpful information
	- Open-ended turn: player engages in chit-chat, humour or non goal-oriented action or dialogue.
	- Conversational repair: player engages in returning conversation to the default mode of "purposeful, goal-oriented and communicative cooperation" after a disruption.
