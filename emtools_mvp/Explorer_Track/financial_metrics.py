# emtools_mvp/Explorer_Track/financial_metrics.py

import streamlit as st
import json
import os

MODEL_PATH = "test_files/sample_model.json"
RATES_PATH = "test_files/rates_and_costs.json"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def calc_financial_metrics(area_m2, capital_cost_per_m2, o_and_m_percent, energy_cost, discount_rate=0.05, years=20):
    capex = area_m2 * capital_cost_per_m2
    o_and_m_annual = capex * o_and_m_percent
    npv = -capex
    for t in range(1, years + 1):
        npv += (energy_cost + o_and_m_annual) / ((1 + discount_rate) ** t)
    opex = o_and_m_annual * years
    payback = capex / energy_cost if energy_cost else None
    roi = ((energy_cost * years) - capex) / capex * 100 if capex else None
    return capex, opex, npv, payback, roi

def run_financial_ui():
    st.header("💰 Financial Metrics Calculator")

    model = load_json(MODEL_PATH)
    rates = load_json(RATES_PATH)

    building = model.get("building", {})
    area = building.get("area_m2", 1000)

    st.markdown(f"**Building Area:** {area} m²")

    cost_m2 = st.number_input("Capital Cost per m² ($)", value=rates.get("capital_cost_per_m2", 2000.0))
    o_and_m = st.number_input("O&M as % of CapEx", value=rates.get("maintenance_percent", 0.01))
    energy_cost = st.number_input("Annual Energy Cost ($)", value=area * 1.5)
    discount_rate = st.slider("Discount Rate", 0.0, 0.15, value=0.05)

    if st.button("📈 Calculate Metrics"):
        capex, opex, npv, payback, roi = calc_financial_metrics(area, cost_m2, o_and_m, energy_cost, discount_rate)

        st.markdown("### 💹 Results")
        st.write(f"**Capital Cost:** ${capex:,.2f}")
        st.write(f"**20-Year O&M:** ${opex:,.2f}")
        st.write(f"**NPV (Discounted at {discount_rate*100:.1f}%):** ${npv:,.2f}")
        st.write(f"**Simple Payback:** {payback:.1f} years")
        st.write(f"**ROI:** {roi:.2f}%")

if __name__ == "__main__":
    run_financial_ui()
