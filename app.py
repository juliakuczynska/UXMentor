import streamlit as st
from agent.uxagent import uxagent

st.set_page_config(page_title="UXMentor", page_icon="🧠", layout="wide")

st.markdown("""
<style>
/* Global font and background */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
    background-color: #f9f9fb;
    color: #333;
}

/* Main title */
h1 {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 2rem;
    color: #222;
}

/* Markdown text */
section, p {
    font-size: 1.1rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

/* Upload and select widgets */
.css-1cpxqw2, .stSelectbox {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #ccc;
    padding: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* Buttons */
button[kind="primary"] {
    background-color: #4b8bf4;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.75rem 1.5rem;
    font-size: 1.1rem;
    border: none;
    transition: background-color 0.3s ease-in-out;
}

button[kind="primary"]:hover {
    background-color: #367af1;
    cursor: pointer;
}

/* Tabs styling */
.stTabs [role="tablist"] {
    justify-content: center;
    gap: 2rem;
}

/* Tło zakładek (nieaktywnych) */
.stTabs [data-baseweb="tab"] {
    font-size: 1.3rem;
    font-weight: 600;
    padding: 1rem 2rem;
    border: 2px solid #b0c4de;
    border-radius: 1rem 1rem 0 0;
    background-color: #e6f0ff;  /* pastelowy niebieski */
    transition: all 0.3s ease-in-out;
    color: #003366;
}

/* Hover efekt */
.stTabs [data-baseweb="tab"]:hover {
    background-color: #d0e7ff;
    cursor: pointer;
}

/* Zakładka aktywna */
.stTabs [aria-selected="true"] {
    background-color: white;
    border-bottom: 4px solid white;
    border-top: 4px solid #4b8bf4;
    color: #002244;
    font-weight: 700;
}

/* Component cards */
.block-container {
    padding: 2rem 3rem;
    max-width: 1200px;
    margin: auto;
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

/* Wireframe HTML preview */
iframe {
    border: 1px solid #ccc;
    border-radius: 12px;
}

/* Text area for code */
textarea {
    border-radius: 10px;
    border: 1px solid #bbb;
    padding: 1rem;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 UXMentor – Interaktywny Asystent UX")

st.markdown("""
Witaj w UXMentor!  
Projektowanie interfejsów użytkownika z naszą pomocą stanie się prostsze, bardziej intuicyjne i oparte na realnych potrzebach użytkowników.

UXMentor to interaktywny asystent, który wspiera Cię na każdym etapie pracy nad UI:

- 🔍 analizuje gotowe interfejsy, by ujawnić ich mocne strony, bariery i potrzeby użytkowników,  
- 📐 generuje przejrzyste wireframe’y i pomaga zaplanować logiczną strukturę oraz kluczowe elementy ekranu.
- 🧠 odpowiada na nurtujące pytania dotyczące projektowania UX/UI
            
Nie musisz projektować od zera.
Zacznij z UXMentor i buduj lepsze doświadczenia!
""")

tab1, tab2, tab3 = st.tabs([
    "🧪 Analiza interfejsu",
    "📐 Wygeneruj koncepcję interfejsu",
    "💬 Porozmawiaj z UXMentorem"
])

with tab1:
    st.header("🧪 Analiza interfejsu ze zrzutu ekranu")
    st.markdown("""
    Zaprojektowałes interfejs, ale nie wiesz, czy działa tak dobrze, jak mógłby?  
    Zastanawiasz się, jak widzi go dziecko, senior lub nowy użytkownik?

    📷 Wgraj zrzut ekranu (np. ekran logowania, formularz), a UXMentor:
    - 🔍 rozpozna widoczne elementy i sposób ich ułożenia,
    - ⚠️ zidentyfikuje potencjalne bariery w odbiorze,
    - 💡 zaproponuje konkretne usprawnienia z perspektywy wybranego użytkownika.

    Dzięki temu podejmiesz lepsze decyzje projektowe zanim zaczniesz zmieniać design!
    """)

    image = st.file_uploader("📁 Wybierz plik (PNG/JPG)", type=["png", "jpg", "jpeg"])
    user_type = st.selectbox("🧍 Z perspektywy jakiego użytkownika analizować?", [
        "Nowy użytkownik", "Senior", "Dziecko", "Osoba z zaburzeniem widzenia kolorów", "Osoba z dysleksją", "Użytkownik ogólny"
    ])

    if image:
        st.markdown("🖼️ Podgląd wgranego interfejsu:")
        st.image(image, width=400)

    if image and st.button("🔍 Przeanalizuj obraz"):
        with st.spinner("Analizuję interfejs..."):
            with open("temp_ui.png", "wb") as f:
                f.write(image.read())

            analysis = uxagent.analyze_image_ui("temp_ui.png", user_type)
            st.subheader("🧠 Analiza UX:")
            st.markdown(analysis)

with tab2:
    st.header("📐 Wygeneruj koncepcję interfejsu")
    st.markdown("""
    Chcesz zaprojektować aplikację, ale nie wiesz, od czego zacząć?  
    Podstawą dobrego UX jest logiczna struktura i świeże spojrzenie – a my pomożemy Ci to rozłożyć na części pierwsze.

    ✍️ Zacznij od opisu, jaką aplikację lub ekran chcesz skonceptualizować – np.  
    “formularz zamówienia jedzenia”,  
    “aplikacja finansowa dla dzieci”,  
    “rejestracja konta dla seniorów”.

    UXAgent:
    - 🔍 wskaże **kluczowe elementy interfejsu** oraz ich UX-owe uzasadnienie,
    - 📐 zaproponuje **strukturę i hierarchię informacji** zgodnie z dobrymi praktykami,
    - 💡 dostarczy **krótką refleksję UX** – na co warto zwrócić uwagę,
    - 🧱 stworzy **prosty wireframe** w HTML + CSS do podglądu i wykorzystania dalej.

    Pamiętaj: to **wstępna propozycja**, nie finalny projekt graficzny.
    """)

    html_prompt = st.text_input("📝 Opisz interfejs (np. 'aplikacja do zamawiania pizzy')")

    if html_prompt and st.button("Wygeneruj strukturę + wireframe"):
        with st.spinner("Projektuję układ..."):
            html_code = uxagent.generate_html_wireframe(html_prompt)

            lines = html_code.splitlines()
            html_start_index = next((i for i, line in enumerate(lines) if line.strip().startswith("<!DOCTYPE html>")), None)

            if html_start_index is not None:
                explanation = "\n".join(lines[:html_start_index])
                code = "\n".join(lines[html_start_index:])
            else:
                explanation = html_code
                code = ""

            cleaned_explanation = "\n".join(
                line for line in explanation.strip().splitlines()
                if not line.strip().startswith("3.")
            )

            st.subheader("🔍 Analiza kluczowych elementów interfejsu:")
            st.markdown(cleaned_explanation)

            if code:
                html_only = "<!DOCTYPE html>" + code

                st.subheader("💻 Podgląd wygenerowanego szkicu interfejsu:")
                st.components.v1.html(html_only, height=600, scrolling=True)

                st.subheader("📜 Kod HTML (do skopiowania):")
                st.text_area("Kliknij i skopiuj kod:", value=html_only, height=300)

with tab3:
    st.header("💬 Porozmawiaj z UXMentorem")
    st.markdown("""
    Masz pytanie o projektowanie UX/UI?  
    Potrzebujesz inspiracji, porady lub szybkiej konsultacji koncepcji?

    Zadaj pytanie poniżej, a UXMentor postara się pomóc!
    """)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.chat_input("Zadaj pytanie o UX/UI...")

    if user_question:
        with st.spinner("UXMentor myśli..."):
            chat_history = st.session_state.chat_history + [("Ty", user_question)]
            response = uxagent.chat(chat_history)
            st.session_state.chat_history.append(("Ty", user_question))
            st.session_state.chat_history.append(("UXMentor", response))

    for sender, message in st.session_state.chat_history:
        if sender == "Ty":
            st.chat_message("user").markdown(message)
        else:
            st.chat_message("assistant").markdown(message)
