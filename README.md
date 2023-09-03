
# 📘 Alice Life Log

O projeto `alice-life-log` é uma aplicação Django que permite aos usuários registrar e visualizar informações pessoais e profissionais.

## 🏗️ Estrutura do Projeto

```
alice-life-log/ # Diretório raiz do projeto.
├── life_log/ # Contém o arquivo manage.py e as configurações principais.
│ ├── manage.py # Script que ajuda na administração do projeto Django.
│ ├── config/ # Configurações principais do Django.
│ │ ├── settings.py # Configurações do projeto Django.
│ │ ├── urls.py # Mapeamentos de URL principais do projeto.
│ │ ├── asgi.py # Entrada ASGI para servidores compatíveis.
│ │ └── wsgi.py # Entrada WSGI para servidores web.
├── personal_info/ # Aplicativo Django para gerenciar informações pessoais.
│ ├── admin.py # Configuração do admin para modelos personal_info.
│ ├── apps.py # Configuração do aplicativo personal_info.
│ ├── models.py # Modelos de banco de dados para personal_info.
│ ├── serializers.py # Serializadores para modelos personal_info.
│ ├── tests.py # Testes para o aplicativo personal_info.
│ ├── urls.py # Mapeamentos de URL para o aplicativo personal_info.
│ └── views.py # Lógicas de visualização para o aplicativo personal_info.
├── professional_info/ # Aplicativo Django para gerenciar informações profissionais.
│ ├── admin.py # Configuração do admin para modelos professional_info.
│ ├── apps.py # Configuração do aplicativo professional_info.
│ ├── models.py # Modelos de banco de dados para professional_info.
│ ├── serializers.py # Serializadores para modelos professional_info.
│ ├── tests.py # Testes para o aplicativo professional_info.
│ ├── urls.py # Mapeamentos de URL para o aplicativo professional_info.
│ └── views.py # Lógicas de visualização para o aplicativo professional_info.
```

## 📝 Descrições:

- `life_log/`: Diretório que contém o arquivo `manage.py` e as configurações principais do projeto.
  - `manage.py`: Um utilitário de linha de comando que permite interagir com o projeto Django de várias maneiras.
  - `config/`: Diretório com configurações principais do Django.
    - `settings.py`: Onde as configurações do projeto Django estão definidas.
    - `urls.py`: Mapeamento das URLs do projeto.
    - `asgi.py`: Entrada ASGI para servidores compatíveis.
    - `wsgi.py`: Entrada WSGI usada para servir o projeto em servidores web.

- `personal_info/` e `professional_info/`: Aplicativos Django. Ambos têm estruturas similares, por isso a descrição será feita conjuntamente:
  - `admin.py`: Define a representação dos modelos do aplicativo no painel administrativo do Django.
  - `apps.py`: Configurações básicas do aplicativo.
  - `models.py`: Onde os modelos de banco de dados são definidos.
  - `serializers.py`: Usado para transformar modelos em formatos que podem ser facilmente renderizados em uma resposta (como JSON).
  - `tests.py`: Contém testes unitários para o aplicativo.
  - `urls.py`: Define as rotas URL específicas para o aplicativo.
  - `views.py`: Onde a lógica de visualização e resposta é definida.

- Outros arquivos ou diretórios podem estar presentes na raiz do projeto ou dentro dos aplicativos, que servem para configurações.

## 📋 Pré-requisitos

- Python (versão 3.11 ou superior) 🐍
- Django (versão 4.2 ou superior) 🌐
- Django REST framework 🔗

## 🔧 Configuração e Instalação

1. **Ambiente Virtual**:
   Para isolar as dependências do projeto, crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```
   Ative o ambiente virtual:

   ```bash
   venv\Scripts\activate
   ```
   Instalar Dependências:
   No ambiente virtual ativado, instale as dependências necessárias:

   ```bash
   pip install django djangorestframework
   ```
   Configuração do Django:
   Navegue até o diretório `life_log` e execute os seguintes comandos:

   Para criar as tabelas no banco de dados:

   ```bash
   python manage.py migrate
   ```
   Para iniciar o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```
   
## 🖥️ Uso

Após iniciar o servidor de desenvolvimento, a aplicação estará disponível em `http://127.0.0.1:8000/`.

Os endpoints incluem:

- Informações pessoais: `/personal/`
- Informações profissionais: `/professional/`