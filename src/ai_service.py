from google import genai
from google.genai import errors

def gerar_plano_alimentar(objetivo: str, peso: float) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt = f"Crie um planejamento alimentar simples de 1 dag para uma pessoa que tem como objetivo: {objetivo} e pesa atualmente {peso}kg. Seja objetivo, amigável e focado em qualidade alimentar."

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        return response.text
    except errors.APIError as e:
        return f"Erro ao comunicar com a IA: {e}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"