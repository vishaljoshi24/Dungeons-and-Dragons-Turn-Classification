import dspy

lm = dspy.LM("ollama_chat/llama3.2:1b", api_base="http://localhost:11434", api_key="b229890ea0664f6193770b4b470f3e74.nJRqYf9TBF9MX24r4fUQQqqB")
dspy.configure(lm=lm)

