import streamlit as st
from datetime import datetime, timedelta

# --- NASTAVENÍ STRÁNKY ---
st.set_page_config(page_title="Karta klienta UNIQA", layout="wide")

# Seznamy pro roletky
POJISTOVNY = ["-", "UNIQA", "Allianz", "Generali ČP", "Kooperativa", "ČPP", "ČSOB", "Pillow", "Direct", "MetLife", "KB"]
STATUSY = ["-", "Mám / OK", "Chci řešit", "Chci revizi", "Nezájem"]

# Styl pro UNIQA vzhled
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    h1 { color: #003399; }
    h3 { color: #003399; border-bottom: 2px solid #003399; padding-bottom: 5px; margin-top: 20px; }
    .stCheckbox { margin-bottom: -10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Digitální Karta Klienta")

with st.form("hlavni_formular"):
    # SEKCE 1: Osobní údaje
    st.subheader("👤 Osobní údaje a Plán")
    c1, c2, c3 = st.columns(3)
    with c1:
        jmeno = st.text_input("Jméno a příjmení")
        email = st.text_input("E-mail klienta")
    with c2:
        mobil = st.text_input("Mobilní telefon")
        povolani = st.text_input("Povolání / Zaměstnavatel")
    with c3:
        datum_schuzky = st.date_input("Datum schůzky", value=datetime.now())
        datum_kontaktu = st.date_input("Datum následného kontaktu", value=datetime.now() + timedelta(days=90))
        poradce = st.text_input("Poradce / Kód", value="Jan Miksa")

    st.divider()

    # SEKCE 2: Priority (Témata)
    st.subheader("🎯 Hlavní témata k řešení")
    ct1, ct2, ct3 = st.columns(3)
    with ct1:
        t_vlastni = st.checkbox("Vlastní zajištění (příjem)")
        t_rodina = st.checkbox("Zajištění rodiny")
        t_deti = st.checkbox("Zajištění dětí / Start do života")
    with ct2:
        t_bydleni = st.checkbox("Vlastní bydlení / Rekonstrukce")
        t_renta = st.checkbox("Renta / Budoucí rezerva")
        t_majetek = st.checkbox("Ochrana majetku a auta")
    with ct3:
        t_podnik = st.checkbox("Podnikatelská rizika")
        t_dane = st.checkbox("Daňové úspory a efektivita")
        t_uvery = st.checkbox("Optimalizace úvěrů / Dluhů")

    st.divider()

    # SEKCE 3: Analýza produktů
    st.subheader("📋 Analýza portfolia")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ochrana osob:**")
        r1, r2, r3 = st.columns([2, 1, 1]); ziv = r1.checkbox("Životní pojištění"); ziv_p = r2.selectbox("Poj.", POJISTOVNY, key="p1"); ziv_s = r3.selectbox("Stat.", STATUSY, key="s1")
        r1, r2, r3 = st.columns([2, 1, 1]); ura = r1.checkbox("Úraz / Nemoc"); ura_p = r2.selectbox("Poj.", POJISTOVNY, key="p2"); ura_s = r3.selectbox("Stat.", STATUSY, key="s2")
        r1, r2, r3 = st.columns([2, 1, 1]); inv = r1.checkbox("Invalidita / Péče"); inv_p = r2.selectbox("Poj.", POJISTOVNY, key="p3"); inv_s = r3.selectbox("Stat.", STATUSY, key="s3")
        st.write("**Majetek a Auto:**")
        r1, r2, r3 = st.columns([2, 1, 1]); maj = r1.checkbox("Dům / Byt / Odp."); maj_p = r2.selectbox("Poj.", POJISTOVNY, key="p4"); maj_s = r3.selectbox("Stat.", STATUSY, key="s4")
        r1, r2, r3 = st.columns([2, 1, 1]); aut = r1.checkbox("Auto (POV/HAV)"); aut_p = r2.selectbox("Poj.", POJISTOVNY, key="p5"); aut_s = r3.selectbox("Stat.", STATUSY, key="s5")

    with col2:
        st.write("**Finance a Podnikání:**")
        r1, r2, r3 = st.columns([2, 1, 1]); ins = r1.checkbox("Investice / DIP"); ins_p = r2.selectbox("Inst.", POJISTOVNY, key="p6"); ins_s = r3.selectbox("Stat.", STATUSY, key="s6")
        r1, r2, r3 = st.columns([2, 1, 1]); dps = r1.checkbox("Penzijko (DPS/PP)"); dps_p = r2.selectbox("Fond", POJISTOVNY, key="p7"); dps_s = r3.selectbox("Stat.", STATUSY, key="s7")
        r1, r2, r3 = st.columns([2, 1, 1]); pod = r1.checkbox("Podnikatelské poj."); pod_p = r2.selectbox("Poj.", POJISTOVNY, key="p8"); pod_s = r3.selectbox("Stat.", STATUSY, key="s8")
        prispevek = st.text_input("Příspěvek zaměstnavatele:")
        r1, r2, r3 = st.columns([2, 1, 1]); hyp = r1.checkbox("Hypotéka / Úvěr"); hyp_p = r2.selectbox("Banka", POJISTOVNY, key="p9"); hyp_s = r3.selectbox("Stat.", STATUSY, key="s9")

    st.divider()

    # SEKCE 4: Závěr
    st.subheader("🏁 Závěr a další kroky")
    cx1, cx2 = st.columns(2)
    with cx1:
        k_nabidka = st.checkbox("Připravit srovnávací nabídku")
        k_smlouva = st.checkbox("Sjednat/Dopojistit produkty")
    with cx2:
        k_revize = st.checkbox("Prověřit stávající smlouvy (audit)")
        k_servis = st.checkbox("Servisní schůzka / Aktualizace údajů")

    poznamky = st.text_area("Detailní poznámky k řešení...", height=150)
    odeslat = st.form_submit_button("💾 ULOŽIT KOMPLETNÍ ZÁZNAM")

# --- LOGIKA ULOŽENÍ ---
if odeslat:
    if not jmeno:
        st.error("Chyba: Vyplňte jméno klienta!")
    else:
        obsah = f"""==================================================
ZÁZNAM Z DIGITÁLNÍ KARTY KLIENTA
==================================================
PORADCE: {poradce}
DATUM SCHŮZKY: {datum_schuzky} | NÁSLEDNÝ KONTAKT: {datum_kontaktu}
--------------------------------------------------
KLIENT: {jmeno}
E-MAIL: {email} | MOBIL: {mobil}
POVOLÁNÍ: {povolani}

TÉMATA K ŘEŠENÍ:
- Vlastní zajištění: {'ANO' if t_vlastni else 'NE'}
- Zajištění rodiny: {'ANO' if t_rodina else 'NE'}
- Zajištění dětí: {'ANO' if t_deti else 'NE'}
- Bydlení: {'ANO' if t_bydleni else 'NE'}
- Renta/Rezerva: {'ANO' if t_renta else 'NE'}
- Ochrana majetku: {'ANO' if t_majetek else 'NE'}
- Podnikání: {'ANO' if t_podnik else 'NE'}
- Daně: {'ANO' if t_dane else 'NE'}
- Úvěry: {'ANO' if t_uvery else 'NE'}

ANALYÝZA PORTFOLIA:
- Životní: {'ZÁJEM' if ziv else 'Bez zájmu'} | Poj: {ziv_p} | Stat: {ziv_s}
- Úraz: {'ZÁJEM' if ura else 'Bez zájmu'} | Poj: {ura_p} | Stat: {ura_s}
- Invalidita: {'ZÁJEM' if inv else 'Bez zájmu'} | Poj: {inv_p} | Stat: {inv_s}
- Majetek: {'ZÁJEM' if maj else 'Bez zájmu'} | Poj: {maj_p} | Stat: {maj_s}
- Auto: {'ZÁJEM' if aut else 'Bez zájmu'} | Poj: {aut_p} | Stat: {aut_s}
- Podnikatelské poj.: {'ZÁJEM' if pod else 'Bez zájmu'} | Poj: {pod_p} | Stat: {pod_s}
- Investice / DIP: {'ZÁJEM' if ins else 'Bez zájmu'} | Inst: {ins_p} | Stat: {ins_s}
- Penzijko: {'ZÁJEM' if dps else 'Bez zájmu'} | Fond: {dps_p} | Stat: {dps_s}
- Příspěvek zaměstnavatele: {prispevek}
- Hypotéka: {'ZÁJEM' if hyp else 'Bez zájmu'} | Banka: {hyp_p} | Stat: {hyp_s}

DALŠÍ KROKY:
- Nabídka: {'ANO' if k_nabidka else 'NE'}
- Sjednat: {'ANO' if k_smlouva else 'NE'}
- Revize: {'ANO' if k_revize else 'NE'}
- Servis: {'ANO' if k_servis else 'NE'}

DETAILNÍ POZNÁMKY:
{poznamky}
--------------------------------------------------
Uloženo: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
"""
        soubor_jmeno = f"Karta_{jmeno.replace(' ', '_')}.txt"
        with open(soubor_jmeno, "w", encoding="utf-8") as f:
            f.write(obsah)
            
        st.success(f"✅ Záznam uložen: {soubor_jmeno}")
        st.download_button("📥 Stáhnout kompletní .txt", obsah, file_name=soubor_jmeno)