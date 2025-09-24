# E1. Refator de Semântica & Acessibilidade (25 min)

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
