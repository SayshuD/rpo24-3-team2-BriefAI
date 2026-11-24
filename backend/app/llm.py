import httpx

def make_summary(text: str) -> dict:
    # ЗАГЛУШКА: возвращаем готовый ответ
    return {
        "title": "Основы ИИ",
        "summary": "ИИ — область информатики для создания интеллектуальных систем.",
        "original_length": len(text)
    }

def ask_model(prompt: str) -> str:
    response = httpx.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma3:4b",
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]
