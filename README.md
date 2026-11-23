# Scientific Programming

A site for containing Scientific Programming files.

## Adding content

Each page has a `<ul class="items">` list. To add something, put the file in the
right folder, then paste a block like the ones below inside that list.
Use lowercase file names without spaces (for example `problem3.pdf`), and make
sure the name in the link matches the file exactly.

### Numerical Problems (`numerical-problems.html`)

1. Put the statement and solution PDF in `problems/`.
2. Make sure the lab's code entry exists in `code.html` (see Code below).
3. Paste this inside the list:

```html
<li>
<h3>Problem 3: Title</h3>
<p>One sentence on what the problem asks and which method solves it.</p>
<div class="links">
<a href="problems/problem3.pdf">Statement and solution (PDF)</a>
<a href="code.html#lab3">Code (lab3)</a>
</div>
</li>
```

The text after `#` in the code link must match the `id` of the lab's entry in `code.html`.

### Data and Models (`data-and-models.html`)

1. Zip the datasets and put the ZIP in `data/`. Zip the trained models and put the ZIP in `models/`.
2. Paste this inside the list (change the title, text and file name):

```html
<li>
<h3>Datasets</h3>
<p>What the datasets contain, where they came from, and their units.</p>
<div class="links"><a href="data/datasets.zip" download>Download datasets</a></div>
</li>
```

### Presentation (`presentation.html`)

1. Put the slides in `presentations/`.
2. Paste this inside the list:

```html
<li>
<h3>Slides</h3>
<p>Final presentation shown in class.</p>
<div class="links">
<a href="presentations/presentation.pdf" download>Download PDF</a>
<a href="presentations/presentation.pptx" download>Download PowerPoint</a>
</div>
</li>
```

### Code (`code.html`)

1. Zip the lab's Python project folder (for example `lab3.zip`) and put it in `code/`.
2. Paste this inside the list, using the lab name as the `id`:

```html
<li id="lab3">
<h3>Lab 3</h3>
<p>What this lab covers and what its main.py does.</p>
<div class="links"><a href="code/lab3.zip" download>Download project folder (ZIP)</a></div>
</li>
```

## Publishing changes

```bash
git add .
git commit -m "Add lab 3"
git push
```

The site updates a minute or two after pushing.

