def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return (
        "You are a medical question answering system.\n"
        "Read the following abstract carefully and answer the question strictly with either "
        "yes, no, or maybe. Your final answer must always be written in LaTeX boxed format "
        "like this: \\boxed{yes}, \\boxed{no}, or \\boxed{maybe}.\n\n"
        "Abstract:\n{}\n\n"
        "Question: {}\n"
        "Answer:".format(ctxs, doc["QUESTION"])
    )
