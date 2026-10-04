# src/theme.py
"""Lab-notebook visual theme. Everything cosmetic lives here."""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

/* Body text. Deliberately NOT [class*="st-"] -- that matches icon spans too. */
html, body, .stMarkdown, p, li, label, .stSelectbox, .stTextInput, .stCaption {
    font-family: 'IBM Plex Sans', system-ui, sans-serif;
}

/* Headings, including the span Streamlit wraps them in. */
h1, h2, h3, h4,
h1 span, h2 span, h3 span, h4 span,
[data-testid="stHeadingWithActionElements"] * {
    font-family: Spectral, Georgia, serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em;
    color: #1C1A17;
}
h1, h1 span { font-size: 2.7rem !important; }

/* Restore Streamlit's icon font -- must come AFTER the rules above. */
[data-testid="stIconMaterial"],
[data-testid="stExpanderToggleIcon"],
span[class*="material-symbols"],
.material-icons, .material-icons-outlined {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    font-weight: 400 !important;
}

.stApp { background: #F7F4ED; }

.vera-rule { border-bottom: 2px solid #1C1A17; margin: 0 0 1.6rem 0; }
.vera-sub {
    font-family: Spectral, Georgia, serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #62594A;
    margin: -0.4rem 0 0.9rem 0;
}

.stTabs [data-baseweb="tab-list"] { gap: 2rem; border-bottom: 1px solid #DCD5C6; }
.stTabs [data-baseweb="tab"] {
    font-family: Spectral, Georgia, serif;
    font-size: 1.05rem;
    background: transparent;
    padding: 0 0 0.6rem 0;
}
.stTabs [aria-selected="true"] {
    border-bottom: 2px solid #8A5A2B;
    color: #1C1A17 !important;
}

[data-testid="stMetric"] {
    background: #FFFDF8;
    border: 1px solid #DCD5C6;
    padding: 1rem 1.1rem;
}
[data-testid="stMetricLabel"] p {
    font-size: 0.72rem !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #62594A !important;
}
[data-testid="stMetricValue"] {
    font-family: Spectral, Georgia, serif !important;
    font-size: 2.2rem !important;
}

.stButton > button {
    border-radius: 0;
    border: 1px solid #1C1A17;
    background: transparent;
    color: #1C1A17;
    font-family: Spectral, Georgia, serif;
    font-size: 0.98rem;
    min-height: 44px;
}
.stButton > button:hover {
    background: #8A5A2B;
    border-color: #8A5A2B;
    color: #FFFDF8;
}

.stTextInput input, .stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 0;
    border-color: #DCD5C6;
    font-family: Spectral, Georgia, serif;
}

[data-testid="stDataFrame"] { border: 1px solid #DCD5C6; }
[data-testid="stExpander"] { border: 1px solid #DCD5C6; border-radius: 0; background: #FFFDF8; }

footer, #MainMenu, [data-testid="stToolbar"] { visibility: hidden; }
</style>
"""


def inject_theme():
    st.markdown(CSS, unsafe_allow_html=True)


def masthead(title: str, subtitle: str):
    st.markdown(f"# {title}")
    st.markdown(f'<p class="vera-sub">{subtitle}</p><div class="vera-rule"></div>',
                unsafe_allow_html=True)