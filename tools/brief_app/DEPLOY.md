# Deploy the Image + A+ Plan Generator as a hosted URL

The app is a Streamlit app and is already container-ready (`Dockerfile`, reads `$PORT`).
Below: the fastest hosted path + what secrets you must set.

## What you need

1. A Git repo the host can pull from (push this project, or just `tools/brief_app` + `tools/` deps).
2. An **Anthropic API key** — the AI writes the creative Image + A+ plans.
   Without it the app still runs but falls back to template copy (no AI creative).
3. (Recommended) a **team password** so the URL isn't open to the public.

### Environment variables (set these in the host's dashboard)

| Variable | Required | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | yes (for AI) | Claude writes the 7-image plan + 7 A+ modules + Q&A |
| `APP_PASSWORD` | recommended | Gate the hosted URL — team enters this once per session |
| `UNSPLASH_ACCESS_KEY` | optional | Real moodboard reference images |
| `PORT` | auto | Injected by Railway/Render; the app already reads it |

## Option A — Railway or Render (easiest hosted URL)

1. Create a new project → **Deploy from GitHub repo**.
2. It auto-detects the `Dockerfile` (path: `tools/brief_app/Dockerfile`, build context = repo root).
3. Add the env vars above (`ANTHROPIC_API_KEY`, `APP_PASSWORD`).
4. Add a **persistent volume** mounted at `/data` (so brands + generated plans survive redeploys).
5. Deploy → you get a public `https://…` URL. Share it + the password with the team.

## Option B — Any Docker host / small VPS

```bash
# from repo root
docker build -f tools/brief_app/Dockerfile -t equalice-plans .
docker run -d -p 8501:8501 \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  -e APP_PASSWORD=choose-a-team-password \
  -v equalice_data:/data \
  --name equalice-plans equalice-plans
```
Then put it behind your reverse proxy / domain (nginx, Caddy, Cloudflare Tunnel) for HTTPS.

## Option C — Local (single machine, no hosting)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
./tools/brief_app/run.sh        # opens http://localhost:8501
```

## Data & persistence

- Brand configs live under `customers/<slug>/` and generated PDFs under `briefs/<slug>/`.
- On a host, mount a volume at `/data` and point the app's data dir there
  (`BRIEF_APP_DATA=/data`, already set in the Dockerfile) so nothing is lost on redeploy.

## Notes

- Cost: ~$0.10 of Anthropic usage per plan (prompt caching on).
- The compliance scan + copy-length lint run on **every** build — the team sees ✅/⛔ before download.
- House rules (7 modules, "From the Brand" for new brands, no Comparison) are enforced by the
  builder automatically from each brand's `config.json`.
