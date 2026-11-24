# University Course Portfolio Site (GitHub Pages)

Minimal, dark-mode static website built with plain HTML and CSS (no build step, no frameworks) for GitHub Pages.

## Pages Included

1. `index.html` — **Main**: Student identifying information and links to all course pages.
2. `numerical.html` — **Numerical Problem**: Weeks 6–7 EEE equation, numerical method, results, and independent check.
3. `data-model.html` — **Data and Model**: Week 10 method on a documented dataset (source, licence, checks, split, baseline, error).
4. `presentation.html` — **Presentation**: Week 10 slides and final presentation (inline PDF embed + download links).
5. `code-statement.html` — **Code and Statement**: Repository link, how to run it, sources, and AI-use statement.

## Folder Structure

```text
.
├── .nojekyll
├── index.html
├── numerical.html
├── data-model.html
├── presentation.html
├── code-statement.html
├── README.md
└── assets/
    ├── css/
    │   └── style.css
    ├── figures/       # Put your PNG/SVG plots here
    └── slides/        # Put week10-slides.pdf and final-presentation.pdf here
```

## How to Customize

1. Search for `<!-- EDIT:` or `[` across the 5 `.html` files and fill in your student info, equation, dataset documentation, code instructions, references, and AI-use statement.
2. Save your plots inside `assets/figures/` and update the `<figure>` blocks in `numerical.html` and `data-model.html`.
3. Save your slide decks as `assets/slides/week10-slides.pdf` and `assets/slides/final-presentation.pdf` so the links and embedded viewers on `presentation.html` work automatically.
4. *(Optional)* If you want LaTeX math rendering (`\( ... \)` or `$$ ... $$`), uncomment the MathJax `<script>` tag in the `<head>` of `numerical.html` and `data-model.html`.

## How to Upload to GitHub and Deploy with GitHub Pages

### Option A: Upload directly in the GitHub web interface
1. Unzip `eee-course-site.zip`.
2. Create a new public repository on GitHub (e.g., `eee-course-site` or `<your-username>.github.io`).
3. Click **Add file → Upload files**, drag the contents **inside** the `eee-course-site/` folder (so `index.html` is at the repository root), and commit to `main`.
4. Go to **Settings → Pages**.
5. Under **Build and deployment → Source**, choose **Deploy from a branch**, select **`main`** and **`/ (root)`**, then click **Save**.
6. Wait 1–2 minutes; GitHub will display your live URL at the top of the Pages settings page.

### Option B: Push with Git from your terminal
```bash
cd eee-course-site
git init -b main
git add .
git commit -m "Initial course portfolio site"
git remote add origin https://github.com/<username>/<repository>.git
git push -u origin main
```
Then enable GitHub Pages in **Settings → Pages** (`main` branch, `/ (root)`).
