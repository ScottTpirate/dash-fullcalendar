# Dash FullCalendar

A lightweight Dash component library that wraps **[@fullcalendar/react](https://fullcalendar.io/docs/react)** and exposes *all* free FullCalendar features to Plotly Dash.

---

## Installation

### Stable release (from PyPI)

```bash
pip install dash-fullcalendar
```

> **No Node.js required at install time.**  
> Pre‑built JavaScript bundles ship inside the wheel.

---

## Quick start

```python
from dash import Dash, html
import dash_fullcalendar as dcal

app = Dash(__name__)

app.layout = html.Div([
    dcal.FullCalendar(
        id="cal",
        initialView="dayGridMonth",
        editable=True,
        selectable=True,
        events=[
            {"title": "Audit", "date": "2025-08-01"},
            {"title": "Go‑Live", "date": "2025-08-10"},
        ],
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

Open <http://127.0.0.1:8050> in your browser and enjoy a fully interactive calendar.

---

## Repository layout

| Path | Purpose |
|------|---------|
| `dash_fullcalendar/` | Python package published to PyPI. Contains generated Dash component classes and **pre‑compiled** JS/CSS assets (`_js_dist`, `_css_dist`). |
| `src/` | Raw React source for the wrapper. |
| `package.json`, `rollup.config.js` | JS build pipeline (`npm run build:all`). |
| `usage.py` | Minimal Dash demo used by tests. |
| `tests/` | Integration tests with `dash[testing]` & `pytest`. |
| `docs/` | Optional screenshots / GIFs shown in this README. |
| `.github/` | CI workflows that run tests and publish to PyPI + npm. |

Ignored via `.gitignore`:

* `node_modules/`
* `dist/`, `build/`, `coverage/`

---

## Development

1. **Clone** and install dependencies

   ```bash
   git clone https://github.com/YOUR_GH_USERNAME/dash-fullcalendar.git
   cd dash-fullcalendar
   npm install
   python -m venv venv && . venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt -r tests/requirements.txt
   ```

2. **Build** and run the example

   ```bash
   npm run build:all     # creates dash_fullcalendar/_dash_fullcalendar*.js
   pip install -e .
   python usage.py       # open http://localhost:8050
   ```

3. **Watch & develop**

   In one shell:

   ```bash
   npm start            # rebuild JS on change
   ```

   In another:

   ```bash
   python usage.py      # auto‑reload Dash
   ```

4. **Run tests**

   ```bash
   pytest -q
   ```

---

## Releasing

```bash
npm run build:all          # 1️⃣ compile JS
python -m build            # 2️⃣ build wheel + sdist
twine upload dist/*        # 3️⃣ publish to PyPI
npm publish                # 4️⃣ publish to npm (optional)
git tag vX.Y.Z && git push --tags
```

Because the wheel already contains the JS bundle (see `MANIFEST.in`), end users do **not** need Node or npm.

---

## Contributing

Pull requests welcome!  To get a change accepted:

1. **Open an issue** first for large changes.
2. Fork, create a descriptive branch name.
3. Follow [Conventional Commits](https://www.conventionalcommits.org/) in your commit messages.
4. `npm test` and `pytest` must pass locally—CI will enforce this.
5. Submit your PR; a maintainer will review and merge.

---

## License

MIT © 2025 YOUR NAME
