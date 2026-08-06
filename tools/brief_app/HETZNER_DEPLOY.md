# Deploy the Image + A+ Plan tool on Hetzner (Docker + auto-HTTPS)

Result: a private, password-gated URL like `https://plans.equalice-academy.com` your team uses.
Everything is prepared — this is copy/paste. ~15 minutes.

## 0. What you provide
- A **Hetzner Cloud** account
- An **Anthropic API key** (https://console.anthropic.com/)
- A **domain/subdomain** you can point (e.g. `plans.equalice-academy.com`)
- The code pushed to a **private GitHub repo** (steps below)

---

## 1. Push the code to GitHub (from your Mac)
The repo is already committed locally. Create an EMPTY private repo on github.com
(e.g. `equalice-plans`), then:
```bash
cd /Users/jonask/Desktop/CLAUDE/Claude_Code
git remote add origin git@github.com:<your-user>/equalice-plans.git
git push -u origin main
```

## 2. Create the server (Hetzner Console)
- **Add Server** → Location: Nuremberg/Falkenstein (DE) → Image: **Ubuntu 24.04**
- Type: **CX22** (2 vCPU / 4 GB) is plenty (~€4.5/mo)
- Add your **SSH key** → Create.
- Note the server **IP**.

## 3. Point your domain
In your DNS provider, add an **A record**:
`plans.equalice-academy.com  →  <server IP>`  (wait a few min for it to propagate)

## 4. On the server (SSH in)
```bash
ssh root@<server IP>

# install Docker
curl -fsSL https://get.docker.com | sh

# get the code (private repo -> use a GitHub Personal Access Token as password,
# or add a deploy key). HTTPS clone:
git clone https://github.com/<your-user>/equalice-plans.git
cd equalice-plans

# create the secrets file from the template
cp .env.example .env
nano .env      # paste ANTHROPIC_API_KEY, set APP_PASSWORD, set APP_DOMAIN=plans.equalice-academy.com

# launch (builds the image, gets HTTPS automatically)
docker compose up -d --build
```

Open the Hetzner **Firewall** (or ufw) for inbound **80 + 443**.

## 5. Done
Visit `https://plans.equalice-academy.com` → enter the team password → create plans.
All your brands are already there (seeded from each `config.json` on first boot).

---

## Updating later (after you change brands/code locally)
```bash
# on your Mac
git add -A && git commit -m "update" && git push
# on the server
cd equalice-plans && git pull && docker compose up -d --build
```

## Notes
- Data (brands + generated PDFs) lives in the `app_data` Docker volume → survives redeploys.
- Cost: server ~€4.5/mo + ~$0.10 Anthropic usage per generated plan.
- Logs: `docker compose logs -f app`   ·   Restart: `docker compose restart`
- If Streamlit shows a websocket/CORS error behind the proxy, add to the `app` service
  `command:` an override with `--server.enableCORS=false --server.enableXsrfProtection=false`
  (usually not needed on a single domain).
