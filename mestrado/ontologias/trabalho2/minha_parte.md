# 2) Ontologia Levemente Fundamentada: **Schema.org** (institucional, uso massivo na Web)

2.1. **O que é / onde está**

Vocabulário colaborativo para dados estruturados (SEO, *rich results*), mantido por um consórcio fundado por **Google, Microsoft, Yahoo e Yandex**; desenvolvido em processo aberto e comunitário no site oficial. ([Schema.org][1])

2.2. **Nível de detalhe / expressividade**

* **Leve e pragmático:** classes amplas e hierárquicas como `Thing`, `Person`, `Organization`, `Place`, `Event`, `Product`, `CreativeWork`; cada tipo tem propriedades simples (exemplos nas páginas oficiais de cada tipo). ([Schema.org][2])
* **Formatos de marcação suportados:** o vocabulário Schema.org pode ser usado em **JSON-LD, RDFa ou Microdata** (guias oficiais). ([Schema.org][3])
* **Sem compromissos ontológicos fortes** (p.ex., não explicita *relators*, *papéis anti-rígidos* ou taxonomias sortais/não-sortais como na UFO; é um vocabulário pragmático para anotação). (Base: docs oficiais do Schema.org). ([Schema.org][2])

2.3. **Uso (evidência)**

* A **documentação do Google Search** declara que “a maior parte do *structured data* do Google usa o vocabulário **schema.org**”, evidenciando a adoção massiva no ecossistema de busca. ([Google for Developers][4])
* As páginas de tipos específicos de *rich results* (por exemplo, **Organization**, **Product**, **Event**) instruem o uso de **schema.org** nos sites. ([Google for Developers][5])

## Identificando os “tipos básicos” na ontologia **não** bem-fundamentada (Schema.org)

Mesmo sem UFO/OntoUML, é possível mapear rapidamente os “básicos” diretamente nas páginas dos tipos/propriedades:

* **Entidades (endurantes, no senso comum):** `Person`, `Organization`, `Product`, `Place`. ([Schema.org][6])
* **Eventos (perdurantes, no senso comum):** `Event`. ([Schema.org][7])
* **Artefatos informacionais:** `CreativeWork` (e subtipos como `Article`, `HowTo`, `Dataset` listados nessa página). ([Schema.org][8])
* **“Qualidades/atributos” como dados:** `QuantitativeValue` (usado para características quantitativas). ([Schema.org][9])
* **Relações simples (propriedades):** `author`, `location`, `offers`, `memberOf`, `knowsAbout`. ([Schema.org][10])
  *(Obs.: `memberOf` e `knowsAbout` aparecem em múltiplas páginas de tipos e propriedades do Schema.org; quando precisar citar num slide, pode apontar para o buscador/termo no site ou para páginas de tipos onde essas propriedades constam como “used on these types”.)*
* **Observação conceitual:** faltam **relators** (fundamentos de relações materiais), **papéis anti-rígidos** e **restrições ontológicas** típicas de modelos bem-fundamentados (UFO/OntoUML) — o que é coerente com a natureza de vocabulário leve do Schema.org. (Leitura: organização dos esquemas e documentação oficial). ([Schema.org][2])

### Comparativo (1 slide pronto)

| Aspecto                  | **Schema.org (leve)**                                              | **CTO/AGROPTO (bem-fundamentada)**                                                      |
| ------------------------ | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Finalidade               | Interoperabilidade Web/SEO. ([Schema.org][1])                      | Entendimento preciso de tarefas/eventos/condições (E-OntoUML/CTO). ([SciTePress][11])   |
| Expressividade           | Moderada (classes/propriedades genéricas). ([Schema.org][2])       | Alta (sortais, papéis, **relators**, eventos/condições). ([ontouml.readthedocs.io][12]) |
| Compromissos ontológicos | Poucos (vocabulário). ([Schema.org][2])                            | Fortes (UFO; E-OntoUML/CTO). ([nemo.inf.ufes.br][13], [ontouml.readthedocs.io][12])     |
| Uso                      | Massivo na Web (empresas/buscadores). ([Google for Developers][4]) | Pesquisa e casos de domínio (agro). ([SciTePress][11])                                  |
| Benefício típico         | Descoberta e integração leve. ([Schema.org][3])                    | Desambiguação, análise causal e reuso por princípios. ([ontouml.readthedocs.io][12])    |

---

## 3) Bibliografia (links abertos)

* **OntoUML Specification** (documentação oficial, *community portal*/ReadTheDocs). ([ontouml.readthedocs.io][14])
* **UFO – visão geral/introdução** (*UFO: Unified Foundational Ontology*, NEMO/UFES, 2021 – PDF). ([nemo.inf.ufes.br][13])
* **CTO/AGROPTO** (*Complex Task Ontology Conceptual Modelling*, KEOD 2018). ([SciTePress][11])
* **Catálogo FAIR OntoUML/UFO** (repositório GitHub; artigo na *Data & Knowledge Engineering* 2023). ([GitHub][15], [ScienceDirect][16])
* **Schema.org** (home e “About”). ([Schema.org][1])
* **Gene Ontology** (exemplo de ontologia de domínio; portal oficial “Gene Ontology Resource”).

[1]: https://schema.org/?utm_source=chatgpt.com "Schema.org - Schema.org"
[2]: https://schema.org/docs/schemas.html?utm_source=chatgpt.com "Organization of Schemas"
[3]: https://schema.org/docs/gs.html?utm_source=chatgpt.com "Getting started with schema.org using Microdata"
[4]: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?utm_source=chatgpt.com "Intro to How Structured Data Markup Works"
[5]: https://developers.google.com/search/docs/appearance/structured-data/organization?utm_source=chatgpt.com "Organization Schema Markup | Google Search Central"
[6]: https://schema.org/Person?utm_source=chatgpt.com "Person - Schema.org Type"
[7]: https://schema.org/Event?utm_source=chatgpt.com "Event - Schema.org Type"
[8]: https://schema.org/CreativeWork?utm_source=chatgpt.com "CreativeWork - Schema.org Type"
[9]: https://schema.org/QuantitativeValue?utm_source=chatgpt.com "QuantitativeValue - Schema.org Type"
[10]: https://schema.org/author?utm_source=chatgpt.com "author - Schema.org Property"
[11]: https://www.scitepress.org/PublishedPapers/2018/69562/?utm_source=chatgpt.com "Complex Task Ontology Conceptual Modelling"
[12]: https://ontouml.readthedocs.io/en/latest/intro/ontouml.html?utm_source=chatgpt.com "OntoUML specification documentation"
[13]: https://nemo.inf.ufes.br/wp-content/uploads/ufo_unified_foundational_ontology_2021.pdf?utm_source=chatgpt.com "UFO: Unified Foundational Ontology | Nemo"
[14]: https://ontouml.readthedocs.io/?utm_source=chatgpt.com "OntoUML specification — OntoUML specification documentation"
[15]: https://github.com/OntoUML/ontouml-models?utm_source=chatgpt.com "OntoUML/UFO Catalog"
[16]: https://www.sciencedirect.com/science/article/pii/S0169023X23000708?utm_source=chatgpt.com "A FAIR catalog of ontology-driven conceptual models"
