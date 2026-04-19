import os
from dotenv import load_dotenv

load_dotenv()


def _detect_provider(provider=None):
    if provider:
        return provider.lower()

    configured = os.getenv("AI_PROVIDER", "").strip().lower()
    if configured in {"openai", "google", "anthropic"}:
        return configured

    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    if os.getenv("GOOGLE_API_KEY"):
        return "google"
    if os.getenv("ANTHROPIC_API_KEY"):
        return "anthropic"

    raise RuntimeError("Nenhuma API key encontrada. Configure OPENAI_API_KEY, GOOGLE_API_KEY ou ANTHROPIC_API_KEY.")


def ask_llm(prompt, system=None, provider=None, temperature=0.3, max_tokens=1200):
    selected = _detect_provider(provider)

    if selected == "openai":
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return {
            "provider": "openai",
            "text": response.choices[0].message.content,
            "usage": getattr(response, "usage", None),
        }

    if selected == "google":
        import google.generativeai as genai

        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        model_name = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
        model = genai.GenerativeModel(model_name)

        full_prompt = prompt if not system else f"Instrucoes de sistema:\n{system}\n\nPedido:\n{prompt}"
        response = model.generate_content(full_prompt)
        text = getattr(response, "text", "") or ""
        return {
            "provider": "google",
            "text": text,
            "usage": None,
        }

    if selected == "anthropic":
        from anthropic import Anthropic

        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model=os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307"),
            system=system or "",
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        text_parts = []
        for chunk in response.content:
            if getattr(chunk, "type", "") == "text":
                text_parts.append(getattr(chunk, "text", ""))
        return {
            "provider": "anthropic",
            "text": "\n".join(text_parts).strip(),
            "usage": getattr(response, "usage", None),
        }

    raise RuntimeError(f"Provider nao suportado: {selected}")
