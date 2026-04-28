# Making Of — Projeto Portfólio Django

---

## 1. Processo de Modelação Geral

O desenvolvimento deste projeto começou com uma fase de planeamento em papel, onde identifiquei todas as entidades necessárias para representar um portfólio académico completo.

Nesta fase inicial:

- Defini as entidades principais  
- Estabeleci relações entre elas  
- Elaborei um primeiro Diagrama Entidade–Relação (DER)  
- Listei atributos de cada entidade em folhas separadas  

Esta abordagem permitiu-me organizar melhor a informação antes da implementação em Django, evitando decisões apressadas durante a programação.

---

## 2. Evolução do Modelo e do DER

- Durante o processo de desenvolvimento, o modelo sofreu algumas alterações importantes.

- O primeiro DER incluía todos os atributos previstos inicialmente, incluindo um campo de nível de interesse associado à entidade Tecnologia.

- Este atributo foi posteriormente reavaliado, concluindo-se que não era adequado enquanto simples campo da entidade, por representar um conceito mais amplo do que a própria tecnologia.

- Assim, em vez de ser eliminado, este conceito foi reformulado e passou a ser representado através da criação de uma entidade independente denominada Interesse, permitindo uma modelação mais estruturada e flexível da informação.

### Justificação da alteração:

- O nível de interesse, inicialmente associado à entidade Tecnologia, foi considerado pouco adequado enquanto atributo isolado, por ser redundante face a outras entidades mais representativas da experiência, como Competências e Projetos.
- No entanto, em vez de ser removido do sistema, este conceito foi posteriormente reaproveitado sob a forma de uma entidade própria denominada Interesse, permitindo uma representação mais estruturada e independente desta informação.
- Esta decisão contribuiu para um modelo mais organizado, coerente e com maior flexibilidade na gestão das relações entre entidades.
- Melhorou a coerência do sistema de relações entre entidades  

- Outra decisão importante foi separar a definição dos atributos do DER.

- Inicialmente, os atributos estavam incluídos no próprio diagrama, o que tornava o esquema visual mais pesado e difícil de interpretar.  
Ao separar esta informação:

- o DER ficou mais claro e focado nas relações  
- a descrição dos atributos ficou mais organizada e legível  

---

### Evidência da evolução

 Diagrama inicial  

![DER](/media/MakingOf/imagem2.jpg)

 Diagrama final

![DER](/media/MakingOf/1000019823.jpg)

 Página separada com atributos das entidades  

![DER](/media/MakingOf/1000019820.jpg)

---

##  3. Processo de Modelação: Perfil

A entidade Perfil representa a informação pessoal do portfólio.

### Decisões de modelação:

- Incluí fotografia para reforçar a componente visual  
- Adicionei biografia para contextualização pessoal  
- Incluí links externos (LinkedIn e GitHub) por serem essenciais em contexto profissional  
- Adicionei currículo em PDF para download direto  

Esta entidade serve como base de apresentação do portfólio.

---


## 4. Processo de Modelação: Curso

O Curso representa a estrutura base do percurso académico.

### Decisões de modelação:

- Usei `codigo` como identificador principal por coerência com dados externos  
- Incluí nome e descrição para contextualização  
- Adicionei logotipo para melhorar a apresentação visual  

---


## 5. Processo de Modelação: Unidade Curricular

A Unidade Curricular foi uma das entidades mais importantes do modelo, pois organiza todo o percurso académico.

### Decisões de modelação:

- Separei `ano` e `semestre` para permitir filtragem eficiente  
- Usei `CharField` para o código legível, devido à sua natureza alfanumérica  
- Incluí ECTS para caracterização académica  
- Adicionei imagem e link externo para enriquecer a apresentação  

### Relações:

- Curso (ForeignKey) → estrutura hierárquica  
- Docente (ForeignKey) → docente responsável  

---


## 6. Processo de Modelação: Docente

Inicialmente, os docentes estavam representados apenas como texto dentro das UCs.

Após análise do modelo, percebi que isso criava redundância e pouca flexibilidade, pelo que optei por criar uma entidade própria.

### Decisões de modelação:

- Evitar repetição de nomes  
- Permitir reutilização de docentes  
- Adicionar biografia e link profissional  

---


## 7. Processo de Modelação: Projeto

Os projetos representam a parte prática do portfólio e são uma das entidades mais importantes.

### Decisões de modelação:

- Incluí ano para organização cronológica  
- Adicionei link para GitHub (essencial para avaliação profissional)  
- Incluí imagem para apresentação visual  
- Adicionei descrição detalhada do projeto  

### Relações:

- UC (ForeignKey) → contexto académico  
- Tecnologia (ManyToMany) → flexibilidade tecnológica  

---


## 8. Processo de Modelação: Tecnologia

A entidade Tecnologia representa ferramentas, linguagens e frameworks utilizados nos projetos.

### Decisões de modelação:

- Incluí categoria para organização (frontend, backend, etc.)  
- Adicionei logotipo e link oficial  
- Removi o campo nível de interesse para simplificar o modelo final  

Esta remoção foi importante para evitar redundância com outras entidades do sistema.

---

## 9. Processo de Modelação: Competência

A entidade Competência representa as capacidades adquiridas ao longo do percurso académico.

### Decisões de modelação:

- Defini um nível de 1 a 5 para representar domínio  
- Relacionei competências com projetos para validação prática  

---


## 10. Processo de Modelação: Formação

A entidade Formação representa cursos adicionais e certificações.

### Decisões de modelação:

- Estrutura cronológica com data de início e fim  
- Flexibilidade para formações em curso  

---


## 11. Processo de Modelação: TFC

Os Trabalhos Finais de Curso foram modelados com base em dados externos (JSON).

### Decisões de modelação:

- Selecionei apenas atributos relevantes  
- Incluí resumo, autores e orientadores  
- Adicionei rating para destacar trabalhos mais relevantes  

### Relações:

- Curso (ForeignKey) → associação académica  

---


## 12. Processo de Modelação: Interesse (Entidade adicional)

Esta entidade foi criada como extensão do projeto para enriquecer o perfil pessoal.

### Decisões de modelação:

- Adicionada para tornar o portfólio mais completo  
- Inclui ícone para representação visual  
- Não fazia parte do enunciado original  

---

## 13. Processo de Modelação: MakingOf

A entidade MakingOf foi criada para documentar todo o processo de desenvolvimento do projeto.

### Decisões de modelação:

- Registar decisões importantes  
- Documentar erros e respetivas soluções  
- Incluir imagens do processo em papel  
- Registar uso de inteligência artificial  

---


## 14. Utilização de Inteligência Artificial e Metodologia

Durante o desenvolvimento utilizei ferramentas de inteligência artificial como apoio.

Estas foram usadas principalmente para:

- Esclarecimento de dúvidas técnicas  
- Apoio na estruturação de modelos  
- Resolução de erros de implementação  

No entanto, todas as decisões foram analisadas e compreendidas, tendo o planeamento inicial sido realizado manualmente em papel.

### Metodologia seguida:

- Planeamento em papel (DER e atributos)  
- Implementação incremental em Django  
- Testes constantes no admin  
- Ajustes progressivos no modelo  

---

## 15. Conclusão

Este projeto permitiu consolidar conhecimentos de modelação de dados e desenvolvimento web com Django.

A abordagem baseada em planeamento inicial, evolução do modelo e documentação contínua foi essencial para garantir coerência e qualidade final da aplicação.
