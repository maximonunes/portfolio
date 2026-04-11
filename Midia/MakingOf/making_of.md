# 📄 Making Of – Portfólio em Django

## 1. Introdução

Este projeto teve como objetivo o desenvolvimento de uma aplicação web de portfólio utilizando o framework Django.

A aplicação permite organizar e apresentar informação académica relevante, nomeadamente Trabalhos Finais de Curso (TFCs), cursos e unidades curriculares, com recurso a dados externos em formato JSON e APIs públicas.

O sistema foi desenvolvido com foco na automatização da importação de dados, modelação relacional e integração de fontes externas de informação académica.

---

## 2. Modelação de Dados

A modelação de dados foi um dos elementos centrais do projeto, tendo sido implementada com o framework :contentReference[oaicite:0]{index=0} através do seu ORM (Object-Relational Mapping).

Foram definidos os seguintes modelos principais:

- **Curso**
- **Autor**
- **TFC (Trabalho Final de Curso)**
- **Unidade Curricular**

---

## 📌 Estrutura das entidades

### 🎓 Curso
Representa um curso académico da instituição.

**Objetivo:**
Centralizar a informação base dos cursos e servir de referência para outras entidades.

---

### 👤 Autor
Representa o autor de um Trabalho Final de Curso.

**Objetivo:**
Permitir a identificação e reutilização de autores em diferentes TFCs, evitando duplicação de dados.

---

### 📘 TFC (Trabalho Final de Curso)
Representa um projeto académico final.

**Objetivo:**
Armazenar informação detalhada sobre projetos desenvolvidos no contexto académico.

---

### 📚 Unidade Curricular
Representa uma disciplina pertencente a um curso.

**Objetivo:**
Descrever o plano curricular de forma detalhada e estruturada.

---

## 📌 Relações implementadas

O modelo relacional foi definido com base em relações do tipo 1:N:

- Um **Curso** pode estar associado a vários **TFCs**
- Um **Autor** pode estar associado a vários **TFCs**
- Um **Curso** pode ter várias **Unidades Curriculares**

---

## 🔗 Representação das relações

- Curso → TFC (1:N)  
- Autor → TFC (1:N)  
- Curso → Unidade Curricular (1:N)  

---

## 3. Evolução da Modelação

A modelação inicial foi sendo progressivamente refinada ao longo do desenvolvimento do projeto, com base na análise dos dados reais obtidos através de ficheiros JSON e APIs externas.

### 🔄 Principais alterações realizadas:

- Criação da entidade **Autor**, separando-a do modelo TFC
- Expansão do modelo **TFC** com campo `resumo`
- Evolução do modelo **Unidade Curricular** com novos atributos:
  - `descricao`
  - `objetivos`
  - `programa`
  - `avaliacao`
  - `ano_curricular`
- Introdução da relação entre **Unidade Curricular e Curso**

### 📌 Justificação das alterações:

Estas alterações foram realizadas com os seguintes objetivos:

- Melhor representação da realidade académica  
- Redução de redundância de dados  
- Normalização da base de dados  
- Suporte a informação mais detalhada proveniente das APIs  
- Preparação do modelo para futuras extensões  

---

## 4. Importação de Dados (TFCs)

Foi desenvolvido o script `importar_tfcs.py` para automatizar a importação de dados a partir de ficheiros JSON.

### ⚙️ Funcionamento do script:

- Percorre todos os ficheiros JSON na pasta `data/`
- Lê e interpreta os dados
- Trata diferentes estruturas (lista ou objeto único)
- Extrai informação relevante:
  - título
  - ano
  - resumo
  - curso
  - autor
- Cria automaticamente os registos na base de dados

### 📌 Decisões técnicas:

- Utilização de `.get()` para evitar erros em campos inexistentes  
- Utilização de `get_or_create()` para evitar duplicação de cursos e autores  
- Normalização dos dados antes da inserção  

---

## 5. Importação de Dados (Cursos e UCs)

Foi desenvolvido o script `importar_ucs.py`, responsável pela integração de dados provenientes de APIs externas.

### ⚙️ Funcionamento:

- Leitura de ficheiros JSON obtidos da API
- Identificação de cursos e unidades curriculares
- Criação ou atualização de registos na base de dados

### 📌 Decisões técnicas:

- `get_or_create()` utilizado para garantir unicidade de cursos  
- `update_or_create()` utilizado para permitir atualização de UCs  
- Estrutura preparada para lidar com dados externos variáveis  

---

## 6. Consumo de API

Foi desenvolvido o script `download_api.py` para recolha automática de dados académicos através de APIs externas.

### 📌 Dados obtidos:

- Informação de cursos
- Planos curriculares
- Unidades curriculares detalhadas

Os dados são armazenados na pasta `files/` em formato JSON.

### 📌 Justificação:

- Separação entre recolha e processamento de dados  
- Reutilização dos dados offline  
- Maior controlo sobre a informação importada  

---

## 7. Organização do Projeto

A estrutura do projeto foi organizada de forma modular:

- `data/` → ficheiros JSON de TFCs  
- `files/` → dados obtidos da API  
- `scripts/` → scripts de importação e automação  
- `portfolio/` → aplicação principal  
- `config/` → configurações do projeto  

### 📌 Justificação:

Esta organização permite:

- Separação clara de responsabilidades  
- Facilidade de manutenção do código  
- Escalabilidade do projeto  
- Melhor leitura e organização da aplicação  

---

## 8. Administração (Django Admin)

Os modelos foram registados no painel de administração do Django.

### 📌 Funcionalidades utilizadas:

- Inserção manual de dados  
- Visualização de registos  
- Validação de dados importados  

### 📌 Vantagens:

- Interface automática fornecida pelo Django  
- Facilidade de testes  
- Gestão rápida de dados  

---

## 9. Dificuldades Encontradas

Durante o desenvolvimento surgiram várias dificuldades técnicas:

- Diferenças na estrutura dos ficheiros JSON (listas vs objetos únicos)  
- Mapeamento entre dados da API e modelos internos  
- Integração de dados externos com estrutura relacional existente  
- Problemas ao adicionar novas relações no modelo (migrations)

### ⚠️ Problema específico:

Ao adicionar a relação `ForeignKey` entre Unidade Curricular e Curso, o Django exigiu um valor por defeito para registos já existentes na base de dados.

### ✅ Solução adotada:

- Definição de um valor por defeito durante a migração  
- Posterior correção dos dados através dos scripts de importação  
- Ajustes incrementais na modelação  

---

## 10. Conclusão

Este projeto permitiu consolidar conhecimentos fundamentais em:

- Modelação de dados relacionais  
- Desenvolvimento com Django e ORM  
- Integração de APIs externas  
- Processamento e importação de dados JSON  
- Automatização de processos de dados  

A aplicação desenvolvida representa uma base sólida para um portfólio académico dinâmico, com estrutura preparada para evolução futura e expansão de funcionalidades.

---

## 💡 Reflexão final

Este projeto demonstrou a importância de uma modelação de dados bem estruturada e da adaptação contínua do sistema à realidade dos dados disponíveis, reforçando a necessidade de uma abordagem iterativa no desenvolvimento de aplicações web.