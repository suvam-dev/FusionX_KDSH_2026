def classify(llm_output):
    if "CONTRADICT" in llm_output.upper():
        return 0
    return 1

