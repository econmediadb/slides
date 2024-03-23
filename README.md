# Using reveal.js on GitHub in the classroom

## 1. Project overview

![structured writing](docs/media/svg/Structured_Writing_0.svg)

### 1.1. Structure of Slides

```mermaid
graph LR;
    A[subject-level.html] -->A1[textbook summary]
    A --> A2[mcq for revision]
    A --> A3[data response question]
    A --> A4[four-part question]

    A3 --> A31[identify ...]
    A3 --> A32[calculate ...]
    A3 --> A33[explain ...]
    A3 --> A34[analyse ...]
    A3 --> A35[discuss ...]

    A4 --> A41[define ...]
    A4 --> A42[identify ...]
    A4 --> A43[explain ...]
    A4 --> A44[analyse ...]
    A4 --> A45[discuss ...]

    style A31 fill:#009933
    style A32 fill:#009933
    style A33 fill:#009933

    style A34 fill:#0000FF

    style A35 fill:#CC8400

    style A41 fill:#009933
    style A42 fill:#009933
    style A43 fill:#009933    

    style A44 fill:#0000FF

    style A45 fill:#CC8400    
```

**Note**: The knowledge and understanding questions (green boxes) will guide the learner which *theoretical* concepts he/she should use in the analysis (blue box) and evaluation (orange box). 


### 1.2. Groupe de travail EcoPo ESC 3DG-1DG

```mermaid
graph LR;
    A[sciences-economiques.html] -->A1[markdown/economie-politique.md]
    A1 --> A11[Introduction]
    A1 --> A12[Chapitre 1: Création de richesse]
    A1 --> A13[Chapitre 2: Répartition de richesse]
    A1 --> A14[Chapitre 3: Formation des prix]
    A --> A2[markdown/mathematiques-fiancieres.md]
    A2 --> A21[pourcentages]
    A2 --> A22[intérêts simples]
    A2 --> A23[intérêts composés]
    A2 --> A24[indices simples]
    A --> A3[markdown/comptabilite.md]
    A3 --> A31[Bilan]
    A3 --> A32[Grand-Livre]
    A3 --> A33[Comptes de charges et de produits]
    A3 --> A34[Journal]
    A3 --> A35[Balance de vérification]
    A3 --> A36[La facture et la TVA]
    A3 --> A37[Les réductions de prix]
```

## 2. Tools used in project

### 2.1. reveal.js

[reveal.js](https://revealjs.com/) allows to make nice presentations that are interactive and easy to visualize on mobile devices. The html presentations are hosted on `pages.github.io`.

### 2.2. Mermaid live editor

[Mermaid live editor](https://mermaid.live/edit): is used convert mermaid diagrams into svg. This tool allows to copy the URL of the svg directly into reveal.js without having to download the entire file.

### 2.3. MathJax

[MathJax](https://www.mathjax.org/) is supported by reveal.js and allows to include maths into the presentation.

### 2.4. D3.js

[D3.js](https://d3js.org/) is a JavaScript library made for data visualization.

### 2.5. blender

[blender](https://www.blender.org/) is used for video editing and for the creation of animations.

## 3. Frequently used code

### 3.1. Controlling the the size

```html
<div style="font-size: 133%;">
<p>\begin{equation} \frac{\partial e_b}{\partial x^b} = &nbsp;&nbsp;\Gamma_{ab}^k &nbsp;e_k &nbsp; \end{equation}</p>
</div>
```

### 3.2. Including a figure with caption

```html
<figure>
  <img src="https://imagesource.org/figure.png" alt="label here" style="width:60%">
  <figcaption> <font size="5"> Caption Text Here. </font> </figcaption>
</figure>
```

### 3.3. Controlling the slide background

```html
<section data-background="#dddddd">
  <h3> title of unit </h3>
  <ol type="1">
    <li> item 1 </li>
    <li> item 2 </li>
    <li> item 3 </li>	
    </ol>
</section>
```

### 3.4. Using TikZJax

[TikZJax](https://tikzjax.com/)

In the `<head>` of your HTML, include

```html
<link rel="stylesheet" type="text/css" href="https://tikzjax.com/v1/fonts.css">
<script src="https://tikzjax.com/v1/tikzjax.js"></script>
```

Then in the `<body>`, include TikZ code such as

```html
<script type="text/tikz">
  \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
</script>
````



