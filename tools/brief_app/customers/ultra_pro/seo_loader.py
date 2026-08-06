"""Shim — der echte SEO-Loader lebt jetzt in tools/brief_app/core/seo_loader.py.
Bestehende Ultra-PRO run.py machen `import seo_loader` (ultra_pro-Ordner auf sys.path);
dieser Shim re-exportiert alles aus dem core-Modul."""
from tools.brief_app.core.seo_loader import *          # noqa: F401,F403
from tools.brief_app.core.seo_loader import (           # explizite Namen für Tools/Editoren
    SeoListing, AplusData, load_seo, load_aplus,
    as_bullets_html, as_qa, qa_module, comparison_module,
)
