# Trabalho – Desenvolvimento Web (HTML5, CSS, JS e PHP opcional)

## 1) Objetivo do projeto

Construir um **site responsivo** com **5 páginas** integradas sob um **tema central** (ex.: “Café & Pâtisserie”, “Estúdio de Yoga”, “ONG de Adoção”, “Portfólio Criativo”), utilizando **HTML5**, **CSS (puro ou framework: Bootstrap/Tailwind/etc)** e **JavaScript**. **PHP** para funcionalidades extras (ex.: processamento de formulário). Trabalho em **grupos de até 5 alunos**.

> Resultado esperado: um site navegável, consistente, acessível e documentado, publicado (opcional) e versionado no GitHub.&#x20;

---

## 2) Escopo mínimo obrigatório (MVP)

### 2.1 Estrutura de páginas (5 no total)

* **Home** (apresentação do tema e navegação clara).
* **Conteúdo 1** (ex.: Produtos/Serviços).
* **Conteúdo 2** (ex.: Blog/Notícias ou Portfólio).
* **Sobre** (história/propósito/equipe).
* **Contato** (formulário funcional com validação no cliente).

> **Regra:** não repetir tema/propósito entre páginas; cada página deve ter **foco distinto** dentro do conceito geral.

### 2.2 Layout, estilo e navegação

* **Header** com logotipo/título e **menu** (desktop + mobile com “menu sanduíche”).
* **Footer** com direitos autorais, contato e links úteis.
* **Tema visual** consistente (tipografia, paleta, espaçamentos).
* **Responsividade mobile-first** com ao menos **3 pontos de quebra** (ex.: ≤480px, 768px, ≥1024px).

### 2.3 Acessibilidade e usabilidade

* **HTML semântico** (header, nav, main, section, article, footer).
* **Texto alternativo** em imagens (`alt`), **ordem lógica** de heading (`h1…h3`).
* **Contraste** atendendo **WCAG AA** e **navegação por teclado**.
* **Foco visível** em elementos interativos.

### 2.4 Interatividade com JavaScript (mínimo 2 itens)

* Exemplos: **menu mobile**, **modal** de detalhes, **carrossel**, **tabs/accordion**, **validação de formulário** (HTML5 + JS), **tema claro/escuro** (toggle com `localStorage`).

### 2.5 Formulário de contato

* Campos: **nome, e-mail, mensagem** (mínimo).
* **Validações**: obrigatoriedade, formato de e-mail, tamanho da mensagem.
* **Feedback ao usuário** (mensagem de sucesso/erro).
* **PHP**: receber `POST` e exibir os dados enviados (ou salvar em arquivo `.txt`) ou em um banco relacional. *Não* é necessário enviar e-mail real.

### 2.6 Boas práticas e desempenho

* **Arquivos separados**: `index.html`, `style.css`/framework, `app.js`.
* **Assets otimizados** (imagens comprimidas, favicons).
* **Sem erros críticos** no **W3C Validator** (HTML/CSS).
* Evitar **bloqueio de renderização** (JS no final ou `defer`).

---

## 3) Tecnologias e restrições

* **Obrigatório:** HTML5, CSS (puro ou **um** framework), JavaScript.
* **Opcional:** PHP básico para processar formulário.
* **Permitido:** bibliotecas JS vanilla ou componentes do framework CSS escolhido.
* **Não permitido:** construtores “no-code” (Wix, Webflow, etc.), CMS prontos (WordPress), **copiar templates prontos** sem customização substancial, uso de **conteúdo sem licença**.

---

## 4) Organização do time e versionamento

* **Grupos de até 5**. Sugestão de papéis (podem acumular):

  * Líder/PM, Dev Front, Dev UI/Design System, Acessibilidade/QA, Documentação/Release.
* **GitHub obrigatório**:

  * Mínimo **15 commits** distribuídos entre membros.
  * Mensagens de commit descritivas.
  * **README.md** completo (modelo abaixo).
* **Estrutura sugerida do projeto:**

  ```code
  /projeto
    /assets
      /img
      /css   -> style.css (ou /tailwind.css/ou outro)
      /js    -> app.js
    index.html
    sobre.html
    conteudo1.html
    conteudo2.html
    contato.html
    cadastro.php
    README.md
    LICENSE
  ```

---

## 5) Entregáveis

1. **Repositório GitHub** público com todo o código.
2. **README.md** contendo:

   * Nome e descrição do projeto.
   * Tecnologias utilizadas.
   * Como executar localmente.
   * Como publicar (se publicado).
   * Funcionalidades implementadas.
   * Membros da equipe e responsabilidades.
3. **(Opcional)** Link publicado (**GitHub Pages** ou **Netlify**).
4. **Apresentação**: demonstração do site + explicação das decisões técnicas e do processo.

> **Prazo final:** **24/11/2025** (23:59 BRT). Entrega do link do repositório no SAVA.&#x20;

---

## 6) Critérios de avaliação (100 pts)

| Critério                                            |   Peso | Indicadores objetivos                                                                                                                    |
| --------------------------------------------------- | -----: | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Aplicação correta das tecnologias (HTML/CSS/JS)** | **30** | HTML semântico; CSS organizado (ou uso correto do framework); JS funcional e sem erros; estrutura de pastas; *build* simples (se houver) |
| **Consistência de design e responsividade**         | **20** | Estilo coerente; 3 breakpoints funcionando; tipografia/cores; legibilidade                                                               |
| **Funcionalidade e navegabilidade**                 | **20** | Fluxos sem erros; links corretos; interações (≥2) funcionam; formulário válido                                                           |
| **Criatividade e originalidade**                    | **20** | Ideia central; conteúdo autoral; soluções visuais; microinterações                                                                       |
| **Documentação e repositório**                      | **10** | README completo; histórico de commits; contribuição distribuída                                                                          |

> Observações de qualidade (podem impactar vários critérios):
>
> * **Acessibilidade** (alt, contraste, foco, headings)
> * **Validação** (W3C sem erros críticos)
> * **Desempenho** (imagens otimizadas, sem bloqueios desnecessários)

---

## 7) Bônus (até +10 pts)

* **Tema claro/escuro** com persistência.
* **Componentes acessíveis** (aria-expanded, aria-controls etc.).
* **Lighthouse** (Acessibilidade ≥ 90).
* **Publicação** com domínio personalizado ou CI/CD simples.
* **Formulário com PHP** e salvamento seguro em arquivo `.txt`.

---

## 8) Penalidades

* **Atraso:** −100 pts por dia (não há espaço para entregas fora do prazo). Após a data combinada, nota 0.
* **Plágio/template não customizado:** nota 0 e encaminhamento às normas acadêmicas.
* **Contribuição desigual** (comprovada por histórico/peer review): ajuste individual.

---

## 9) Roteiro de apresentação (6–8 min + 2 min Q\&A)

1. Problema/tema e público-alvo (30s).
2. Arquitetura de páginas e navegação (1 min).
3. Decisões de UI/UX e responsividade (1 min).
4. Demonstração das **2 interações JS** (2 min).
5. Acessibilidade e validações (1 min).
6. Lições aprendidas e próximos passos (1 min).

---

## 10) Checklist de conformidade (entregar marcado)

* [ ] 5 páginas com propósitos distintos e coerentes com o tema central.
* [ ] Header, menu, footer consistentes; navegação íntegra.
* [ ] 3 breakpoints testados (mobile, tablet, desktop).
* [ ] Pelo menos **2 interações JS** funcionando.
* [ ] Formulário de contato com validações (HTML5 + JS) e feedback.
* [ ] Acessibilidade: alt em imagens, contraste, foco, headings.
* [ ] Uso do PHP para processamento de formulário.
* [ ] HTML/CSS validados sem erros críticos.
* [ ] Imagens/ícones otimizados e com licença adequada.
* [ ] Repositório no GitHub com **README.md** e commits distribuídos.
* [ ] (Opcional) Site publicado (GitHub Pages ou Netlify).

---

## 11) Modelo de README.md (copiar e editar)

```markdown
# Nome do Projeto

Descrição breve do site e do público-alvo.

## Tecnologias
- HTML5, CSS (Bootstrap/Tailwind ou CSS puro), JavaScript
- (Opcional) PHP para processar o formulário

## Como rodar localmente
1. Clone o repositório
2. Abra `index.html` no navegador
3. (Opcional) Para PHP: use `php -S localhost:8080` na pasta do projeto

## Funcionalidades
- Menu responsivo
- [Descrever interações JS]
- Formulário com validação

## Acessibilidade
- Texto alternativo, contraste, foco visível, headings semânticos

## Publicação
- GitHub Pages: [URL]
- Netlify: [URL]

## Equipe
- Nome – Papel – Principais contribuições
- ...

## Licenças de conteúdo
- Imagens/ícones de [fonte] – licença [tipo]
```

---

## 12) Cronograma sugerido (não avaliativo, mas recomendado)

* **Semana 1–2:** Ideação do tema, referência visual, wireframes (Figma ou papel).
* **Semana 3–4:** Estrutura HTML e navegação; base de estilos; responsividade.
* **Semana 5–6:** Interações JS; formulário; ajustes de acessibilidade.
* **Semana 7:** Otimizações, validação W3C, README, *deploy* (opcional).
* **24/11/2025:** **Entrega final**.

---

### Observações finais

* Prefira conteúdo **autoral**. Se usar imagens/ícones de terceiros, cite a **licença**.
* Mantenha o **escopo simples e bem executado**: poucos componentes, mas corretos, acessíveis e responsivos.
* Em caso de dúvidas técnicas, registre no README as decisões e limitações.
