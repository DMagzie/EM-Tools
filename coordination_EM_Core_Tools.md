# EM Core Tools – Dual-Account Development Coordination

This document outlines how development of the EM Core Tools Track is split between two ChatGPT accounts for efficiency, modularity, and safe release management.

---

## 👤 Account Roles

| ChatGPT Account | Role           | Responsibilities |
|-----------------|----------------|------------------|
| **This Account** | Canonical Owner | - Manage `v0.x/` version folders  
- Finalize logic, README, test runner  
- Push to GitHub + Dropbox |
| **Other Account** | Prototyper / Support | - Use `v0.x-dev/` folders for parallel development  
- Draft core logic and test cases  
- Prep modules for handoff |

---

## 📁 Folder Strategy

| Folder         | Purpose                       | Owner |
|----------------|-------------------------------|-------|
| `v0.4/`        | Finalized Dual Baseline Tool  | This Account |
| `v0.4-dev/`    | Prototype version for v0.4    | Other Account |
| `v0.5/`        | Manual J Explorer milestone   | This Account |
| `v0.5-dev/`    | Manual J development draft    | Other Account |
| `sandbox/`     | Shared utilities / experiments| Other Account |

---

## 🔁 Development Flow

1. Other account builds module in `v0.x-dev/`
2. When logic is ready:
    - Copy to `v0.x/` here
    - Update test runner, README
    - Finalize GitHub commit + Dropbox upload
3. Tag with `v0.x` in GitHub

---

## ✅ Version Tracking Checklist

- [ ] `v0.4/` scaffolded and test-ready
- [ ] `v0.4-dev/` completed and submitted from other account
- [ ] GitHub tag `v0.4` created
- [ ] Backup ZIP uploaded to Dropbox

---

## 🔒 Rules of Engagement

- `.env` always managed manually (not synced between accounts)
- GitHub repo is controlled by **this account**
- Dropbox sync handled only by **this account**
- Backups and tagging are versioned from this branch
