# Deploy the Image + A+ Plan tool on Hetzner (Docker + auto-HTTPS)

Result: a private, password-gated URL `https://plans.equalice-academy.com` your team uses.
Code is already on GitHub: **git@github.com:JonasK01/equalice-plans.git** (private).
Only the account steps below remain (~15 min).

---

## 1. Create the server (Hetzner Cloud Console)
- **Add Server** → Location: Nuremberg/Falkenstein (DE) → Image: **Ubuntu 24.04**
- Type: **CX22** (2 vCPU / 4 GB, ~€4.5/mo) — plenty
- **SSH keys**: add your Mac key (the same one now on GitHub) so you can log in
- Create → note the **IPv4 address**
- Under **Firewall** (or later via ufw): allow inbound **22, 80, 443**

## 2. Point the domain
In your DNS provider (equalice-academy.com), add an **A record**:
`plans  →  <server IPv4>`   → gives `plans.equalice-academy.com` (wait a few min).

## 3. SSH in and install Docker
```bash
ssh root@<server IPv4>
curl -fsSL https://get.docker.com | sh
```

## 4. Give the server read access to the private repo (deploy key)
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub
```
Copy that line → add it at
**https://github.com/JonasK01/equalice-plans/settings/keys/new**
(Title: `hetzner`, leave "Allow write access" OFF) → **Add key**.

## 5. Clone, configure secrets, launch
```bash
git clone git@github.com:JonasK01/equalice-plans.git
cd equalice-plans
cp .env.example .env
nano .env
#   ANTHROPIC_API_KEY=sk-ant-...            <- your real key
#   APP_PASSWORD=<strong team password>
#   APP_DOMAIN=plans.equalice-academy.com   <- already correct
# save: Ctrl-O, Enter, Ctrl-X

docker compose up -d --build
```
First build takes ~2–3 min. Caddy fetches the HTTPS certificate automatically.

## 6. Done
Open **https://plans.equalice-academy.com** → enter the team password → create plans.
All brands are already there (seeded from each `config.json` on first boot).

---

## Update later (after you change brands/code on your Mac)
```bash
# Mac:     git add -A && git commit -m "update" && git push
# Server:  cd equalice-plans && git pull && docker compose up -d --build
```

## Handy
- Logs: `docker compose logs -f app`  ·  Restart: `docker compose restart`  ·  Stop: `docker compose down`
- Data (brands + generated PDFs) lives in the `app_data` volume → survives redeploys.
- Cost: server ~€4.5/mo + ~$0.10 Anthropic per generated plan.
- If Streamlit shows a websocket/"please wait" loop behind the proxy, add under the `app`
  service in `docker-compose.yml`:
  `command: sh -c "streamlit run tools/brief_app/app.py --server.headless=true --server.port=8501 --server.address=0.0.0.0 --server.enableCORS=false --server.enableXsrfProtection=false"`
  then `docker compose up -d`.
