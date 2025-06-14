import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import content_types
from agno.agent import Agent

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

uxagent = Agent(name="UXAgent")

def analyze_image_ui(image_path: str, user_type: str) -> str:
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    prompt = f"""
    Masz przed sobą zrzut ekranu interfejsu aplikacji. Twoim zadaniem jest przeanalizowanie go jako **ekspert UX** z perspektywy użytkownika typu: **{user_type}**.

    Przedstaw analizę w czytelnej, uporządkowanej formie z nagłówkami i wypunktowaniami.

    🔍 Oceń:
    - Jakie elementy interfejsu rzucają się w oczy (np. pola, przyciski, kolory)?
    - Czy interfejs wygląda zrozumiale i zachęca do działania?
    - Co może sprawiać trudność lub być nieczytelne dla tego użytkownika?
    - Jakie są typowe potrzeby i ograniczenia tej grupy (np. dla seniora: większe fonty, prosty język)?

    ✅ Ułatwienia (co działa dobrze):
    - ...

    ⚠️ Potencjalne problemy (dla tego użytkownika):
    - ...

    💡 Rekomendacje UX – jak można poprawić dostępność i użyteczność tego interfejsu:
    - ...

    Forma odpowiedzi:
    - krótko,
    - konkretnie,
    - z nagłówkami i emoji,
    - unikaj ścian tekstu.
    """

    response = model.generate_content([
        prompt,
        {"mime_type": "image/png", "data": image_bytes}
    ])

    return response.text.strip()

def generate_html_wireframe(prompt: str) -> str:
    full_prompt = f"""
    Jesteś ekspertem UX i projektantem UI.
    Wygeneruj pełny kod HTML z osadzonym CSS (inline <style>) prezentujący nowoczesny, estetyczny wireframe interfejsu aplikacji opisanej poniżej.
    Weź pod uwagę najlepsze praktyki UX/UI, drogę użytkownika i dostępność.
    Przed generowaniem kodu, napisz w 5-6 zdaniach co jest najważniejsze w tym interfejsie i jakie są jego kluczowe funkcje. Napisz, co może jeszcze być dodane lub poprawione przez projektanta.

    Styl:
    - nowoczesny, minimalistyczny,
    - zaokrąglone inputy i przyciski,
    - padding, marginesy i odstępy między sekcjami,
    - font: system-ui lub Inter,
    - max 1 kolumna, czytelne nagłówki, buttony pełnej szerokości,
    - responsywny layout (max-width: 400–600px),
    - NIE używaj obrazów ani zewnętrznych bibliotek.

    Zwróć tylko poprawny, samodzielny kod HTML.

    Opis interfejsu:
    "{prompt}"
    """

    response = model.generate_content(full_prompt).text

    clean = response.strip()
    if clean.startswith("```html"):
        clean = clean.removeprefix("```html").strip()
    if clean.endswith("```"):
        clean = clean.removesuffix("```").strip()

    return clean

def chat(messages: list[tuple[str, str]]) -> str:
    """
    messages – lista wiadomości w formacie: [("Ty", "pytanie"), ("UXMentor", "odpowiedź"), ...]
    """
    intro_instruction = (
        "Jesteś doświadczonym asystentem UX o nazwie UXMentor. "
        "Pomagasz użytkownikom projektować interfejsy, analizować je, "
        "poprawiać dostępność, czytelność i hierarchię informacji. "
        "Odpowiadasz konkretnie, zwięźle i z empatycznym tonem."
    )

    history = [{"role": "user", "parts": [intro_instruction]}]

    for sender, text in messages:
        role = "user" if sender == "Ty" else "model"
        history.append({
            "role": role,
            "parts": [text]
        })

    response = model.generate_content(history)
    return response.text.strip()


uxagent.chat = chat
uxagent.analyze_image_ui = analyze_image_ui
uxagent.generate_html_wireframe = generate_html_wireframe
