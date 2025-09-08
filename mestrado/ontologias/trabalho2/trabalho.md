# Explorando Ontologias

**Bem-Fundamentada x Levemente Fundamentada**
Raphael … (DRE)

## Sumário

1. Ontologia Fundamentada em **E-OntoUML** (extensão de OntoUML)
   1.1 O que é E-OntoUML?
   1.2 Motivação por trás da **Complex Task Ontology (CTO)**
   1.3 **AGROPTO** (Agriculture Operations Task Ontology)
   1.4 Modelo original (visão E-OntoUML)
   1.5 Modelo com a nova perspectiva (CTO estendendo E-OntoUML)
   1.6 Pontos de extensão
   1.7 Por que analisar a CTO (e não só E-OntoUML)?
2. **Ontologia Levemente Fundamentada** (Schema.org) – detalhe/expressividade/uso + mapeamento de “tipos básicos”
3. Bibliografia

---

## 1) Ontologia fundamentada em E-OntoUML

### 1.1 Mas o que é E-OntoUML?

OntoUML é uma linguagem **bem-fundamentada** para modelagem conceitual, construída como extensão de UML e **fundada na UFO** (Unified Foundational Ontology). A variante **E-OntoUML** amplia o foco para **eventos/ações** (UFO-B), adicionando construtos e diretrizes para representar **tipos de eventos**, suas relações e impactos no domínio. ([OntoUML][1], [Inf.ufes][2])

Tipos de ontologias (recapitulando): **top-level** (UFO), **de domínio**, **de tarefa** (CTO/AGROPTO), e **de aplicação** (mais específicas). A **Complex Task Ontology (CTO)** é uma **ontologia de tarefa** construída em **E-OntoUML**. ([Nemo][3], [OntoUML][4])

### 1.2 Motivação por trás da **CTO**

A CTO foi proposta para tratar **tarefas complexas** indo além do que o modelo inicial cobria, incorporando: (i) **objetivos da tarefa**, (ii) **interferência de eventos externos no fluxo de controle**, e (iii) **condições** (pré/pós) que afetam execução e resultados. ([SciTePress][5])

### 1.3 **AGROPTO** (Agriculture Operations Task Ontology)

Caso de uso da CTO no domínio agrícola (ex.: pulverização de pesticidas). A modelagem em E-OntoUML/CTO explicita **eventos externos** que interrompem/alteram a execução, **pré-condições/pós-condições** e **estados de execução** (e.g., *interruption*, *cancellation*). ([SciTePress][5])

### 1.4 Modelo original (visão E-OntoUML)

* **Núcleo**: *AgentAction* (ação do agente) altera/gera *Situation* (estado), com relações **pre-state**/**pos-state**; tempo e recursos (*Resource*) como insumos/saídas; participação de recurso explicitada (*ResourceParticipation*).
* **Ênfase**: estruturação de papéis e **comportamento da tarefa** (decomposição/fluxo), mas **sem** tratar ainda objetivos, condições e interferências externas de forma sistemática. ([SciTePress][5])

### 1.5 Modelo com a **nova perspectiva** (CTO estendendo E-OntoUML)

* Introduz **TriggerEvent** (*Ordinary* vs *Exception*; *Planned* vs *Unplanned*) que **causa** uma **Condition** via **ConditionModification** (*relator* que fundamenta a relação material).
* **ExecutionStateAction** (relator) conecta **Condition** ↔ **AgentAction**, especificando **ExecutionState** (*Interruption*, *Cancellation*, *OperationalDelay*).
* Ligações temporais (**triggeredAt**, **causedAt**) e **satisfies** entre **Condition** e **PropositionValueSpecification**.
  → Resultado: fluxo de controle **reativo a eventos e condições**, permitindo análises de interrupção, atrasos, objetivos satisfeitos etc., **como nas Figuras 3–4** do trabalho (interferência externa; ponto temporal da interrupção). ([SciTePress][5])

### 1.6 Pontos de extensão (como “plugamos” CTO no modelo original)

* **Comuns**: *AgentAction*, *Situation*, *TimePoint*, *Resource/Output/Input*.
* **Novos**: *TriggerEvent*, *Condition*, *ConditionModification* (relator), *ExecutionStateAction* (relator) e especializações de **ExecutionState**.
  → Extensão **orgânica**: preserva o núcleo E-OntoUML e acrescenta compromissos UFO-B para eventos/condições/objetivos. ([Inf.ufes][2])

### 1.7 Por que analisar a **CTO** (e não apenas E-OntoUML)?

Porque a CTO exemplifica a **evolução de fundamentos** (UFO → OntoUML → **E**-OntoUML → **CTO**) quando o domínio requer **mais poder explicativo**: condições, objetivos e eventos externos alterando execução. Essa evolução torna explícitos **relators, papéis anti-rígidos, mereologia, qualidades e eventos** — reduzindo ambiguidades comuns em OWL leve. ([Nemo][3], [OntoUML][1])

---

## 2) **Ontologia Levemente Fundamentada**: *Schema.org* (institucional, uso massivo na Web)

**O que é / onde está**
Vocabulário colaborativo para dados estruturados (SEO, *rich results*), mantido por consórcio **Google, Microsoft, Yahoo, Yandex** (site oficial, “About”). ([Schema.org][6])

## **Nível de detalhe / expressividade**

* **Leve e pragmático**: classes amplas (`Thing`, `Person`, `Organization`, `Place`, `Event`, `Product`, `CreativeWork`…) e propriedades simples; facilita anotação **JSON-LD/RDFa/Microdata**.
* **Sem compromissos ontológicos fortes** (não modela, p.ex., **papéis anti-rígidos**, **relators**, taxonomias sortais/não-sortais da UFO). ([Schema.org][6])

**Uso (evidência)**
Adoção massiva na Web (ecossistema de mecanismos de busca; diretrizes e comunidade abertas no site). ([Schema.org][6])

### Identificando os “tipos básicos” na ontologia **não** bem-fundamentada

Mesmo sem UFO/OntoUML, dá para mapear rapidamente os “básicos” em **Schema.org**:

* **Entidades/endurance (no senso comum)**: `Person`, `Organization`, `Product`, `Place`.
* **Eventos/perdurantes**: `Event`.
* **Artefatos informacionais**: `CreativeWork` (e.g., `Article`, `HowTo`, `Dataset`).
* **Qualidades/atributos** (não como *qualities* UFO, mas como dados): `QuantitativeValue`, `ratingValue`, etc.
* **Relações simples**: `author`, `location`, `offers`, `memberOf`, `knowsAbout`.
  → Observação: faltam **relators** (fundamentos de relações materiais), **papéis anti-rígidos** e **restrições ontológicas** típicas de modelos UFO/OntoUML. ([Schema.org][6])

### Comparativo (1 slide pronto)

| Aspecto                  | **Schema.org (leve)**                     | **CTO/AGROPTO (bem-fundamentada)**                             |
| ------------------------ | ----------------------------------------- | -------------------------------------------------------------- |
| Finalidade               | Interoperabilidade Web/SEO                | Entendimento preciso de tarefas/eventos/condições              |
| Expressividade           | Moderada (classes/propriedades genéricas) | Alta (sortais, papéis, **relators**, eventos e condições)      |
| Compromissos ontológicos | Poucos (vocabulário)                      | Fortes (UFO; E-OntoUML/CTO)                                    |
| Uso                      | Massivo na Web (empresas)                 | Pesquisa e casos de domínio (agro), com diagramas e diretrizes |
| Benefício típico         | Descoberta e integração leve              | Desambiguação, análise causal e reuso orientado a princípios   |

---

## 3) Bibliografia (links abertos)

* **OntoUML Specification** (doc oficial). ([OntoUML][4])
* **UFO – visão geral/introdução** (NEMO/UFES; paper 2021). ([Nemo][3])
* **CTO/AGROPTO** (paper KEOD 2018 com Fig. 3–4). ([SciTePress][5])
* **Catálogo FAIR OntoUML/UFO** (para ver mais modelos). ([GitHub][7], [ScienceDirect][8])
* **Schema.org** (site e “About”). ([Schema.org][6])
* **Gene Ontology (ex. de ontologia de domínio)** — se quiser citar no §1.1. ([Gene Ontology Resource][9])

---

### Se quiser, eu transformo isso em 6–8 slides

* 1: título + objetivo do exercício
* 2: E-OntoUML (onde entra no ecossistema UFO/OntoUML)
* 3–4: CTO/AGROPTO (modelo original vs. estendido, com bullets das Fig. 3–4) ([SciTePress][5])
* 5: Schema.org (o que é, expressividade, uso) ([Schema.org][6])
* 6: “tipos básicos” mapeados em Schema.org
* 7: quadro comparativo
* 8: bibliografia (com links)

Quer que eu já gere o **texto dos slides** aqui no chat, prontos para colar?

[1]: https://ontouml.readthedocs.io/en/latest/intro/ontouml.html?utm_source=chatgpt.com "OntoUML specification documentation"
[2]: https://www.inf.ufes.br/~gguizzardi/Events_as_Entities_in_Ontology-Driven_Co.pdf?utm_source=chatgpt.com "Events as Entities in Ontology-Driven Conceptual Modeling"
[3]: https://nemo.inf.ufes.br/wp-content/uploads/ufo_unified_foundational_ontology_2021.pdf?utm_source=chatgpt.com "UFO: Unified Foundational Ontology | Nemo"
[4]: https://ontouml.readthedocs.io/?utm_source=chatgpt.com "OntoUML specification — OntoUML specification documentation"
[5]: https://www.scitepress.org/Papers/2018/69562/69562.pdf?utm_source=chatgpt.com "Complex Task Ontology Conceptual Modelling"
[6]: https://schema.org/?utm_source=chatgpt.com "Schema.org - Schema.org"
[7]: https://github.com/OntoUML/ontouml-models?utm_source=chatgpt.com "OntoUML/ontouml-models: The OntoUML/UFO Catalog is a ..."
[8]: https://www.sciencedirect.com/science/article/pii/S0169023X23000708?utm_source=chatgpt.com "A FAIR catalog of ontology-driven conceptual models"
[9]: https://geneontology.org/?utm_source=chatgpt.com "Gene Ontology Resource"
