<h1 align="center">
  <img src="static\imagens\banner-projeto.png" alt="Banner do Projeto" style="object-fit:cover;height:180px;">
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/versão-1.0-blue?style=for-the-badge" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/license-BSD-blue?style=for-the-badge" alt="Licença BSD">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge" alt="Status de desenvolvimento">
</p>

## Descrição do Projeto
Projeto de extensão universitária desenvolvido pelos alunos do 5º semestre do IFMT Campus Cuiabá, na disciplina Oficina de Prática Extensionista. O sistema visa informatizar e otimizar processos de gestão de almoxarifado da FUNAC, instituição pública do Governo do Estado de Mato Grosso, trazendo benefícios tanto para o fluxo administrativo quanto para o desenvolvimento acadêmico dos alunos envolvidos.

## Contexto Institucional
- **Instituição:** IFMT Campus Cel. Octayde Jorge da Silva
- **Disciplina:** Oficina de Prática Extensionista II
- **Parceria:** FUNAC/SEJUS/MT (Fundação Nova Chance, instituição do Governo do Estado de Mato Grosso)

## 📌 Índice

<p align="center">  
<ol>  
  <a href="#Objetivos"><li> Objetivos </li></a>           
  <a href="#Equipe"><li> Equipe </li></a>             
  <a href="#Tecnologias-Utilizadas"><li> Tecnologias Utilizadas </li></a>       
  <a href="#Funcionalidades"><li> Funcionalidades</li></a>            
  <a href="#Instalação-e-Configuração"><li> Instalação e Configuração </li></a>           
  <a href="#estrutura-do-projeto"><li> Estrutura do Projeto</li></a>           
  <a href="#cronograma"><li> Cronograma </li></a>           
  <a href="#Documentação"><li> Documentação </li></a>           
  <a href="#como-contribuir"><li> Como Contribuir </li></a>                    
  <a href="#licença"><li> Licença </li></a>      
  <a href="#status-do-projeto"><li> Status do Projeto </li></a>           
  <a href="#agradecimentos"><li> Autores e Agradecimentos </li></a>         
  </ol>
</p>

## 🎯Objetivos
- **Geral:** Desenvolver um sistema que modernize a gestão de almoxarifado da FUNAC.
- **Específicos:**
  - Otimizar a gestão de almoxarifado da instituição.
  - Aplicar os conhecimentos de desenvolvimento web e banco de dados aprendidos no curso.
  - Integrar práticas reais de extensão universitária.
  - Promover benefícios institucionais para a FUNAC através da inovação tecnológica.
  - Fomentar o trabalho colaborativo entre alunos e profissionais da FUNAC.

## 👥Equipe
- **Discentes:** Turma do 5º semestre - 2025/02 TSI IFMT Cel. Octayde Jorge da Silva
- **Docente:** Profª Esp. Heloise de Souza Bastos
- **Colaboradores:** Técnicos e gestores da FUNAC

## 💻Tecnologias Utilizadas
- **Linguagens:** Python
- **Framework:** Django
- **Ferramentas de Versionamento:** Git, GitHub
- **Outras:** Markdown para documentação

## 🛠️Funcionalidades

**Itens**
- O sistema deve permitir o cadastro de novos itens, incluindo os seguintes dados: descrição, código, unidade de medida, valor unitário e fornecedor.
- Deve ser possível atualizar os dados de itens cadastrados.
- O sistema deve permitir a busca de itens por diversos critérios, como código, descrição, fornecedor, entre outros.

**Estoque**
- O sistema deve permitir o registro de entradas e saídas de itens do estoque.
- O sistema deve controlar os níveis de estoque mínimo e máximo para cada item.
- O sistema deve possibilitar a realização de inventários periódicos.

## ⚙Instalação e Configuração

### Pré-requisitos
- Python 3.10+
- Django 4.0+
- Git

### Passo a Passo
```
# Clone o repositório

git clone https://github.com/ifmt-cba-laboratorio-de-software/oficinaii-api-almoxarifado.git

1 - Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\Activate

2 - Instalar dependências
python -m pip install --upgrade pip
pip install -r requirements.txt

3 - Configure o banco de dados no arquivo settings.py

4 -  Aplicar migrações
python manage.py makemigrations
python manage.py migrate

5 - Criar superuser
 python manage.py createsuperuser

6 -Execute as migrações
python manage.py migrate

7 - Rodar o servidor de desenvolvimento
python manage.py runserver

```

## 📂Estrutura do Projeto
```
funac-projeto/
├── app/
├── templates/
├── static/
├── requirements.txt
├── README.md

docs/
├── Requisitos - Almoxarifado.pdf
├── Diagramas Banco de Dados.pdf
├── 
```

## 📅Cronograma

| Etapa | Data |
|:----------|------|
| Levantamento| 31/01/2025 | 
| Preparação   | 12/09/2025 |
| Desenvolvimento  | 21/11/2025 |
| Testes |  28/11/2025 |
| Entrega Final |  05/12/2025 |


## 📚Documentação
- [Requisitos do Sistema](./docs/requisitos.md)
- [Diagrama Banco de Dados](./docs/Diagramas-Banco-de-Dados.pdf)
- [Especificação técnica](.requirements.txt)

## ✍️Como Contribuir

> [!CAUTION]
> AVISO NÃO CRIE BRANCH NA MAIN.

> [!TIP]
> Crie a sua branch baseado na branch  `dev.`

1. Faça um fork do projeto
2. Clone seu fork para sua máquina (`git clone ...`)
3. Crie uma branch para sua modificação (`git checkout -b minha-feature`)
4. Commit suas alterações
5. Envie um pull request para análise

> Siga o padrão de código, respeite as convenções e documente suas contribuições!

## 📜Licença 
Projeto licenciado sob BSD. Consulte o arquivo [LICENSE](./LICENSE).

## 🔄Status do Projeto
<img src="https://img.shields.io/badge/em%20desenvolvimento-yellow?style=for-the-badge" alt="Status de desenvolvimento">

## 🤝Agradecimentos
Agradecimento especial à FUNAC pela parceria institucional, à Prof.ª Esp. Heloise de Souza Bastos pelo acompanhamento didático e ao IFMT - Campus Cuiabá pela estrutura.

---
Feito com ❤️ por discentes do IFMT.



- [Voltar ao Início](#Descrição-do-Projeto)