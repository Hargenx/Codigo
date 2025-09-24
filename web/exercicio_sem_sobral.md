Perfeito, então vamos direto ao ponto: um **lab de 2 horas**, só papel/canetão, **focado em HTML5/CSS de verdade** (sem “dinâmicas fofinhas”). Saem com **arquitetura de HTML semântico, plano de CSS escalável, layouts Flex/Grid prontos, e decisões de responsividade**. Você só precisa imprimir os enunciados abaixo.

---

# HTML/CSS Paper Lab (2h) — para devs, sem PCs

## Setup (rápido)

* 14–18 grupos de 4–6 devs (com 89, dá tranquilo).
* Cada grupo recebe 1 “packet” impresso (exercícios + folhas-resposta).
* Materiais: caneta/marcador, régua, fita crepe.
* Avaliação: cada exercício vale pontos objetivos; gabaritos incluídos.

## Agenda

* 00:00–00:10 — Briefing + distribuir packets
* 00:10–00:35 — E1. **Refator de Semântica & A11y** (HTML5)
* 00:35–01:00 — E2. **Cascata & Especificidade** (sem chute)
* 01:00–01:25 — E3. **Layout Constraints** (Flex/Grid no papel)
* 01:25–01:45 — E4. **Plano de Responsividade** (breakpoints e tokens)
* 01:45–02:00 — E5. **Arquitetura CSS** (BEM/ITCSS) + fechamento

---

## E1. Refator de Semântica & Acessibilidade (25 min)

**Input (imprimir):**

```html
<div id="topo">
  <div class="logo"><img src="logo.png"></div>
  <div class="menu"><a href="/">Home</a> | <a href="/blog">Blog</a></div>
</div>
<div class="wrap">
  <div class="title">Sobre nós</div>
  <div class="txt">Somos uma empresa...</div>
  <div class="cards">
    <div class="card">
      <div class="cardtitle">Missão</div>
      <div class="cardtxt">Texto</div>
    </div>
    <div class="card">
      <div class="cardtitle">Visão</div>
      <div class="cardtxt">Texto</div>
    </div>
  </div>
</div>
<div class="footer">© 2025</div>
```

**Tarefas:**

1. Reescreva **somente as tags/atributos** (sem mudar texto/ordem visual) usando HTML5 semântico + A11y mínimo (e.g., `alt`, estrutura de navegação, heading hierarchy).
2. Delimite **uma** região `main`.
3. Marque **tab order** esperado (1–8) considerando links/inputs (se houver).
4. Liste **2 melhorias** de A11y extras que você aplicaria (sem código).

**Gabarito (essencial):**

* `header`, `nav`, `main`, `section`, `article`/`section` para cards, `footer`.
* `img` com `alt="Nome da empresa"` (ou `alt=""` se decorativa).
* Menus como lista: `nav > ul > li > a`.
* Hierarquia: `h1` (“Sobre nós”), `h2` nos cards.
* A11y extra típico: `lang="pt-BR"` no `html`, `meta charset`, `skip link` (`a[href="#main"]`), contraste, foco visível.

---

## E2. Cascata & Especificidade (25 min)

**Input (imprimir regras + alvo):**

```css
/* 1 */
.card .title { color: #333; }
#about .card .title { color: #444; }
.card-title { color: #555; }
.card > .title { color: #666; }
.card .title.highlight { color: #000; }

/* 2 */
a.btn { background: #09f; }
nav a { background: transparent; }
#hero nav a.btn.primary:hover { background: #06c !important; }
```

**HTML alvo:**

```html
<section id="about" class="wrap">
  <div class="card">
    <h2 class="title highlight">Sobre nós</h2>
    <p>...</p>
  </div>
</section>

<nav id="hero"><a class="btn primary" href="#">Call</a></nav>
```

**Tarefas:**

1. Calcule a **especificidade** de cada seletor que atinge `h2.title.highlight`.
2. Diga **qual cor** final aplica ao `h2` e **por quê** (cascata/ordem).
3. Para o link em `#hero nav a.btn.primary:hover`, explique a origem final do `background` e o motivo (incluindo `!important`).

**Gabarito (resumo):**

* `.card .title` → (0,0,2,1)
* `#about .card .title` → (0,1,2,1)
* `.card-title` (não atinge)
* `.card > .title` → (0,0,2,1)
* `.card .title.highlight` → (0,0,3,1)
  **Vence** `#about .card .title` por ter **ID** (mesmo `.highlight` tendo +1 classe), então **color: #444**.
  No `a.btn.primary:hover`, o `#hero nav a.btn.primary:hover { ... !important }` domina (origem igual, `!important` > normal), então **#06c**.

---

## E3. Layout Constraints (Flex/Grid no papel) (25 min)

**Requisito visual (imprimir wireframe simples):**

* **Header** full-width, altura fixa.
* **Main** com **cards** 3-col em ≥ 1024px, 2-col em 768–1023px, 1-col < 768px.
* Cards: mesma altura na linha; botão alinhado **no rodapé** do card.
* Sidebar opcional **só** ≥ 1200px, à direita (25%/min 280px).

**Tarefas (no papel):**

1. Especifique **classes** e **HTML mínimo** para suportar isso (sem conteúdo).
2. Escreva **apenas as declarações CSS** (sem valores mágicos gigantes) para:

   * Grid responsivo de cards (pode Flex ou Grid).
   * “Botão no rodapé do card” (pista: `display:flex; flex-direction:column; margin-top:auto;`).
   * Sidebar condicional (pista: `@media (min-width:1200px)` + grid de áreas).

**Gabarito (padrões aceitos):**

* **Grid de cards (Grid):**

  ```css
  .cards { display:grid; gap:1rem; }
  @media (min-width:1024px){ .cards { grid-template-columns: repeat(3,1fr); } }
  @media (min-width:768px) and (max-width:1023px){ .cards { grid-template-columns: repeat(2,1fr); } }
  @media (max-width:767px){ .cards { grid-template-columns: 1fr; } }
  .card { display:flex; flex-direction:column; }
  .card .actions { margin-top:auto; }
  ```

* **Sidebar condicional (Grid de áreas):**

  ```css
  .layout { display:grid; grid-template-columns: 1fr; grid-template-areas: "header" "main"; }
  @media (min-width:1200px){
    .layout { grid-template-columns: 1fr minmax(280px,25%); grid-template-areas: "header header" "main aside"; }
  }
  header{ grid-area:header; } main{ grid-area:main; } aside{ grid-area:aside; }
  ```

---

## E4. Plano de Responsividade (20 min)

**Tarefas:**

1. Defina **tokens** de spacing/typography e **breakpoints** (3–4 no máximo).
2. Liste **políticas**: container widths, `box-sizing`, `img { max-width:100% }`, `font-size` responsivo (ex.: clamp).
3. Escreva **1 linha** de justificativa por decisão (ex.: “`clamp(1rem, 1vw + .8rem, 1.25rem)` para tipografia fluida sem saltos”).

**Gabarito (exemplo enxuto):**

* Breakpoints: `sm:480`, `md:768`, `lg:1024`, `xl:1200`.
* Tokens: `--space-1: .5rem; --space-2: 1rem; --radius: .5rem;` etc.
* Política: `:root { box-sizing:border-box } *,*:before,*:after{ box-sizing:inherit }`
* Tipografia: `html { font-size: clamp(16px, 1.2vw, 18px); }`

---

## E5. Arquitetura CSS (BEM/ITCSS) (15 min)

**Tarefas:**

1. Proponha **estrutura de pastas** e **camadas** (ITCSS ou semelhante).
2. Nomeie 3 componentes em **BEM** (ex.: `card`, `btn`, `nav`) com **elementos** e **modificadores**.
3. Defina convenções: ordem de propriedades, onde entram utilitários (`.u-hidden`, `.u-sr-only`), e como lidar com `!important`.

**Gabarito (curto):**

```code
/src/css/
  00-settings/ (tokens: colors, spacing, z-index)
  01-tools/     (mixins, helpers)
  02-generic/   (normalize/reset, base)
  03-elements/  (HTML tags: a, p, h1..)
  04-objects/   (layouts: container, grid, stack)
  05-components/(card, btn, nav, form)
  06-utilities/ (.u-*)
```

* BEM:

  * `.card`, `.card__title`, `.card__actions`, `.card--featured`
  * `.btn`, `.btn--primary`, `.btn--ghost`
  * `.nav`, `.nav__item`, `.nav__link`, `.nav--inline`
* `!important` apenas em utilitários documentados.

---

# O que você leva “pronto”

* **HTML semântico** sólido (com a11y mínima correta).
* **Domínio da cascata/especificidade** com justificativa técnica.
* **Layouts Flex/Grid** desenhados e parametrizados (fáceis de portar pro código).
* **Plano de responsividade** baseado em tokens e clamp.
* **Arquitetura CSS** escalável (ITCSS + BEM) com convenções claras.

Se quiser, eu já formatarei isso como **packet A4 imprimível** (enunciados + folhas-resposta + gabaritos separados). É só dizer e eu te entrego os PDFs.
