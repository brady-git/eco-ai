from typing import Tuple, Dict, Any
from .prompts import ANSWER_PROMPT

def retrieve(query: str) -> list[dict]:
    return [{"text": "Stub context about Eco Battery."}]

def generate_answer(context: str, question: str) -> str:
    return f"(stub) Using context: {context[:60]}... -> Answer to: {question}"

def answer_question(q: str, meta: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    docs = retrieve(q)
    context = "\n\n".join(d["text"] for d in docs)
    prompt = ANSWER_PROMPT.format(context=context, question=q)
    ans = generate_answer(context, q)
    return ans, {"prompt_tokens": len(prompt), "k": len(docs)}
