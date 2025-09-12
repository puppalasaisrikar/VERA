# VERA - AI Compliance Co-Pilot
**Validation & Explanation for Regulatory Assurance**

VERA is an AI-powered compliance co-pilot that transforms messy lab results (CSV/XLSX) into instant, unit-aware **PASS/FAIL decisions** against materials standards like **ISO 527** or **ASTM D638**.  
Unlike a rules script, VERA combines deterministic checks with LLM intelligence to make compliance validation faster, explainable, and reproducible.

---

## 🚀 Features
- **Upload & Map** – Upload lab results; AI suggests column mappings and units.  
- **Natural Language → YAML** – Define compliance rules in plain English; VERA generates a machine-readable template.  
- **Validate** – Deterministic pass/fail validation with KPIs and color-coded results.  
- **Explain** – LLM-generated, grounded explanations with remediation tips.  
- **Export** – Generate a one-page PDF compliance report instantly.

---

## 📊 Demo Flow
1. Select a standard or describe rules in natural language.  
2. Upload results (CSV/XLSX).  
3. Validate and review pass/fail status.  
4. View explanations and remediation.  
5. Export a polished PDF report.

---

## ⚙️ Installation
```bash
# clone repo
git clone https://github.com/puppalasaisrikar/VERA.git
cd VERA

# create environment
conda create -n vera python=3.11 -y
conda activate vera

# install dependencies
pip install -r requirements.txt

