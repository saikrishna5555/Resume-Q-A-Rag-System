from rectriver import ask_question
from langchain.chat_models import init_chat_model
from datetime import date

def generation(question:str):
    llm=init_chat_model("groq:qwen/qwen3.6-27b")
    context=ask_question(question)
    prompt=f"""you are a helpful assistant
    Important rules:
    1. Use the retrieved context as the source of truth.
    2. Do not assume an answer before calculating it.
    3. For dates such as "Present", use today's date {date.today()}.
    4. Perform date calculations carefully.
    5. Do not blindly repeat conclusions from the context if they conflict
    with the actual date calculation.
    6. if the user ask abused question respond please ask proper questio6
    7. dont provide any irrelavant responses
    8. send only response match no need to send rules followed
    IMPORTANT:
    - Return ONLY the answer.
    - Do NOT show reasoning.
    - Do not show context text
    - Do NOT show analysis.
    - Do NOT use <think>,</think> tags.
    - Do NOT explain anything.
    {context}
    question:
    
    {question}
    if you dont find and context simply return answer not found
    """

    response=llm.invoke(prompt).content
    return response