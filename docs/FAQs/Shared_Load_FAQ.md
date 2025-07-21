
# Utility Analysis Track – FAQ

## ❓ Does CUAC calculate shared loads (like corridor lighting or central DHW)?

**No**, CUAC (California Utility Allowance Calculator) does not explicitly calculate or allocate shared loads as part of its official reporting process. However, understanding how shared loads are handled is important when building hybrid or cross-state tools.

---

## ✅ What *is* included in CUAC modeling?

| Item                        | Included? | Notes                                                                 |
|-----------------------------|-----------|-----------------------------------------------------------------------|
| Tenant unit energy use      | ✅ Yes     | Per-unit modeling includes HVAC, DHW, appliances, lighting, etc.     |
| Individual system types     | ✅ Yes     | Each unit can have distinct HVAC/DHW systems in the model            |
| Meter configurations        | ✅ Yes     | Tenant-paid vs. owner-paid utility handling is modeled               |

---

## ❌ What is *not* included in CUAC unit-level outputs?

| Shared Load Type            | Included in CUAC? | Notes                                                              |
|-----------------------------|-------------------|--------------------------------------------------------------------|
| Corridor or common lighting | ❌ No              | Considered owner-paid; not allocated to tenants                    |
| Central DHW or HVAC loads   | ❌ Not directly    | May exist in simulation, but not allocated to units in CUAC output |
| Recirculation pumps, PV, etc| ❌ No              | Ignored in tenant allocations unless submetered                    |

---

## 🧠 Why does this tool simulate shared loads?

This track extends CUAC logic to:
- Support mixed-meter and shared system scenarios
- Enable tenant-vs-owner cost analysis
- Comply with non-CA engineering method requirements (HUD, NYSERDA, etc.)

Shared loads are simulated and **allocated by floor area or other methods**, enabling hybrid or internal reporting — but this step is **distinct from CUAC** and should not be confused with regulatory CUAC submissions.

---

## 📌 Key Takeaway

> CUAC = Per-unit modeling only  
> This Track = CUAC + Optional Shared Load Simulation (for internal QA or cross-state modeling)
