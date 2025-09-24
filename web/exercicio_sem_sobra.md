Bora. Aqui vai um **Paper UI Lab (2h)** para devs (sem PC) focado em **desenhar telas no papel** e **mapear 1:1 para HTML5/CSS** depois.

---

# Paper UI Lab — 2 horas, técnico

## Visão geral

* Saída: 3 wireframes (mobile/tablet/desktop), inventário de componentes, **naming BEM**, **tokens**, **breakpoints**, foco/ordem de tab, e **esqueleto de HTML/CSS** pronto pra portar.
* Times: 14–18 grupos de 4–6. Cada grupo escolhe **um tipo de tela**:
  `Landing`, `Lista+Detalhe`, `Dashboard`, `Formulário pesado`, `Produto/Checkout`.

## Agenda

* **00:00–00:10** — Brief rápido + constraints
* **00:10–00:35** — E1. **Tokens & Grid** (definições objetivas)
* **00:35–01:10** — E2. **Wireframes 3 breakpoints** (layout responsivo)
* **01:10–01:35** — E3. **Componentes & Estados** (BEM, a11y, fluxos)
* **01:35–01:55** — E4. **Mapa Semântico & CSS Layers** (esqueleto)
* **01:55–02:00** — Fechamento relâmpago

---

## Constraints (impedir bikeshedding)

* **Escala 4pt**: múltiplos de 4 para spacing e sizing.
* **Grid**: desktop `12 col`, tablet `8`, mobile `4`. `gap` padrão = `space-3`.
* **Breakpoints**: `sm 480`, `md 768`, `lg 1024`, `xl 1200`.
* **Cores** (papel): use nomes de tokens, não hex (ex.: `--brand-500`, `--fg-900`).
* **Tipografia**: 2 níveis base (body, heading) com variação via `clamp()` na posterior implementação.

---

## E1) Tokens & Grid (25 min)

**Tarefas**

1. Defina **tokens mínimos** (nomes e valores) em uma folha:

   * Spacing: `--space-1:4`, `--space-2:8`, `--space-3:12`, `--space-4:16`, `--space-6:24`, `--space-8:32`.
   * Radius: `--radius-1:4`, `--radius-2:8`.
   * Border: `--border-1:1`, `--border-2:2`.
   * Container: `--container-max:1200`.
   * Z-index: `--z-modal: 999; --z-dropdown: 100;`.
2. Desenhe **grid** (linhas verticais leves) nas 3 folhas (mobile/tablet/desktop) com margens laterais (= `space-6`).
3. Defina **escala tipográfica** (nomes, não números):
   `--font-body`, `--font-sm`, `--font-md`, `--font-lg`, `--font-xl`, `--font-2xl`.
   Observação para implementação: usar `clamp()` depois.

**Checklist de saída**
✅ Tabela de tokens preenchida • ✅ Grid marcado nos 3 formatos • ✅ Escala tipográfica nomeada

---

## E2) Wireframes Responsivos (35 min)

**Tarefas**

1. Desenhe **3 variações** (mobile, tablet, desktop) da mesma tela **usando o grid**.
2. Anote **semântica** por bloco (ex.: `header`, `nav`, `main`, `section[aria-labelledby=h2-#]`, `aside`, `footer`).
3. Marque **alinhamentos** (stack/inline) e **larguras** em frações do grid (`span 4/12`, etc.).
4. Defina **ordem de leitura** e **ordem de tab** numerando elementos focáveis.

**Regras de aceitação**

* Desktop: suportar **≥ 3 col** de cards quando aplicável; manter **altura consistente** dos cartões na linha.
* Mobile: navegação compacta em **linha ou off-canvas**; conteúdo principal primeiro.
* Tablet: **2 col** onde fizer sentido; evitar layouts “desktop em miniatura”.

---

## E3) Componentes & Estados (25 min)

**Tarefas**

1. Liste os **componentes** usados na tela (máx. 8): `card`, `btn`, `navbar`, `sidebar`, `table`, `form-field`, `tag`, `breadcrumb`, etc.
2. Para 3 componentes críticos, defina **BEM** e estados:

   * `card`, `card__media`, `card__title`, `card__meta`, `card__actions`, modificadores: `card--featured`, `card--loading`.
   * `btn`, `btn--primary`, `btn--ghost`, `btn--danger`, estados `:hover`, `:focus-visible`, `:disabled`.
   * `form-field`, `form-field__label`, `form-field__input`, `form-field--error`.
3. **A11y & interação**:

   * Especifique **papéis/atributos** necessários (`role="navigation"`, `aria-current="page"`, `aria-invalid="true"`).
   * Desenhe **foco visível** (ex.: anotar `outline: 2px auto`).
   * Modele **fluxo** (setas entre telas ou dentro da tela) e **mensagens de erro**.

**Saída**

* Inventário + diagrama de estados (papel) + tabela de props/atributos por componente.

---

## E4) Mapa Semântico & CSS Layers (20 min)

**Tarefas**

1. Escreva (no papel) o **esqueleto HTML** da sua tela (sem conteúdo/lorem), **só tags e classes**:

   * Regra: **uma** região `main`, headings com hierarquia, `nav ul>li>a`, `img` com `alt` (ou `alt=""` se decorativa).
2. Defina a **arquitetura CSS** que vai implementar depois (apenas a estrutura e layering):

   ```
   /src/css/
     00-settings/ (tokens.css)
     01-tools/    (mixins.css)
     02-generic/  (reset.css, base.css)
     03-elements/ (typography.css, links.css)
     04-objects/  (layout-grid.css, container.css, stack.css)
     05-components/(card.css, btn.css, nav.css, form-field.css, table.css)
     06-utilities/ (.u-sr-only.css, .u-hide.css, .u-visually-hidden.css)
   ```

   E as **camadas**:

   ```css
   @layer reset, tokens, base, elements, objects, components, utilities;
   ```

3. Mapeie **breakpoints** por componente (matriz curta):

   * Linhas = componentes; colunas = `sm/md/ld/xl`; células = mudanças (ex.: “`card` → de 1fr para 3fr; `btn` cresce via `inline-size: clamp(...)`”).

---

## Critérios de correção (objetivos)

* **Tokens/Grid (20%)**: consistência 4pt, grid aplicado nos 3 formatos.
* **Wireframes (35%)**: proporção correta, hierarquia clara, responsividade **sem colapso** visual.
* **Componentes/Estados/A11y (25%)**: BEM correto, estados cobertos, foco/ordem de tab coerentes.
* **Mapa Semântico & CSS Layers (20%)**: HTML5 válido (conceitualmente), camadas bem separadas, matriz de breakpoints útil.

---

## Gabaritos de referência (resumo)

**HTML base (conceitual)**

```html
<header class="header" role="banner">
  <nav class="nav" aria-label="Principal">
    <ul class="nav__list">
      <li class="nav__item"><a class="nav__link" href="/" aria-current="page">Início</a></li>
      ...
    </ul>
  </nav>
</header>

<main id="main" class="layout">
  <section class="hero" aria-labelledby="hero-title">
    <h1 id="hero-title">Título</h1>
  </section>

  <section class="cards" aria-label="Destaques">
    <article class="card card--featured">
      <img class="card__media" src="#" alt="">
      <h2 class="card__title">...</h2>
      <p class="card__meta">...</p>
      <div class="card__actions">
        <a class="btn btn--primary" href="#">Comprar</a>
      </div>
    </article>
    ...
  </section>

  <aside class="sidebar" aria-label="Filtros">...</aside>
</main>

<footer class="footer" role="contentinfo">...</footer>
```

**Layout responsivo (trechos a implementar depois)**

```css
/* Objects */
.container { max-width: var(--container-max); margin-inline:auto; padding-inline: var(--space-6); }

.cards { display:grid; gap: var(--space-6); }
@media (min-width: 1024px){ .cards { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 768px) and (max-width: 1023px){ .cards { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 767px){ .cards { grid-template-columns: 1fr; } }

.card { display:flex; flex-direction:column; gap: var(--space-3); }
.card__actions { margin-top:auto; }
```

**BEM exemplos**

* `btn btn--primary | btn--ghost | btn--danger`
* `nav nav__list nav__item nav__link nav--inline`
* `table table__row table__cell table--striped`

**A11y essenciais**

* `lang="pt-BR"`, `meta viewport`, `a[href="#main"]` (skip link).
* `:focus-visible` estilo visível.
* `aria-live="assertive"` para feedback de erro em formulários, se aplicável.

---

## Folhas para imprimir (modelos rápidos)

**1) Tokens**

```
Spacing: 1=__ 2=__ 3=__ 4=__ 6=__ 8=__
Radius:  1=__ 2=__
Border:  1=__ 2=__
Container max: __
Z-index: modal __  dropdown __
Breakpoints: sm __  md __  lg __  xl __
Type scale: body __  sm __  md __  lg __  xl __  2xl __
```

**2) Matriz de Breakpoints por Componente**

```
Componente | sm            | md                 | lg                     | xl
-----------|---------------|--------------------|------------------------|-----------------
card       | 1 col         | 2 col              | 3 col                  | 3 col + sidebar
btn        | inline-size _ | clamp(...)         | clamp(...)             | idem
nav        | colapsada     | inline             | inline + dropdown      | inline + mega
...
```

**3) Ordem de Tab / Foco**

```
# Elemento (selector)     | Role/aria              | TabIndex | Observações foco (:focus-visible)
1 header .nav__link[1]    | link / aria-current    | auto     | underline + outline 2px auto
2 header .nav__link[2]    | link                   | auto     | ...
...
```

**4) Inventário de Componentes (BEM)**

```
Bloco       | Elementos                          | Modificadores
------------|------------------------------------|---------------------------
card        | __media __title __meta __actions   | --featured --loading
btn         | (n/a)                              | --primary --ghost --danger
form-field  | __label __input __hint __error     | --invalid --success
```

---

Se quiser, eu já organizo tudo isso num **packet A4** (enunciados + folhas de resposta + gabaritos separados) pra você imprimir em sala. Quer que eu gere?
