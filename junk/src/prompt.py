def build_prompt(backstory, passages):
    context = "\n\n".join(passages)

    return f"""
You are a narrative consistency checker.

BACKSTORY:
{backstory}

EVIDENCE FROM NOVEL:
{context}

Question:
Does the backstory violate constraints established in the novel?

Answer ONLY:
CONSISTENT or CONTRADICT
"""

