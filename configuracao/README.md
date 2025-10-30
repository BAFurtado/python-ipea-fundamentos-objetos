## 🔧 Configuração do Ambiente de Desenvolvimento

### Recomendações para o Curso 

### ⚡ **VS Code** + Python + Windows

- **Mais leve e direto para análise de dados**

- *Usuários avançados podem utilizar Linux + PyCharm + Miniconda*

## A. Necessários passos 1 e 2 antes do início das aulas

1. **Instalar Python**
   - [Python.org](https://www.python.org/downloads/) - baixe a versão **3.12.10**
   - **NÃO** baixar **Python** da Microsoft Store
   ## ⚠️ **Marque a opção "Add Python to PATH" durante a instalação** (crucial)


2. **Instalar **VS Code****
   - [**VS Code** Download](https://code.visualstudio.com/download)
   - Depois de instalado **VS Code** e **Python**, instale algumas extensões
   - Extensões essenciais (no **VS Code** busque botão extensions `CTRL+Shift+X` na barra lateral à esquerda):
   - Verifique o autor (Microsoft para Python) e clique `install`

     - **Python** (Microsoft)
     - **Pylance** (melhor autocompletar)
     - **GitLens** (para versionamento)

## B. Vamos desenvolver os passos seguintes ao longo das aulas

3. **Instalar Git**
- [Git Download](https://git-scm.com/downloads)
- Configuração básica (após instalação, abra o terminal):
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@ipea.gov.br"
```

4. **Instalar environment--ambiente: locais onde arquivos de execução do python e bibliotecas encontram-se disponíveis**
- Abra o *Terminal*
- Verifique se a versão de **python** está correta. 
   - Windows
      - `where python`
   - Linux/Mac
      - `which python`
- Instale o environment com o seguinte comando:
   - `python -m venv venv-curso-ipea ` 
   Você está chamando o interpreter `python` e pedindo a ele para rodar um módulo `-m` que se chama `venv` de virtual environment. Em seguida, dá o nome ao seu novo ambiente: **`venv-curso-ipea`**
      - Melhor usar esse mesmo nome no ambiente para a primeira vez.
      - **Nota** : Se `python` não funcionar, tente `python3` ou `python3.12`
- Em seguida é necessário ativar o ambiente e avisar ao **VS Code** para utilizá-lo, onde ele se encontra. Faça isso no *Terminal* com
   - Windows
      - `venv-curso-ipea\Scripts\activate`
   - Mac/Linux
      - `source venv-curso-ipea/bin/activate`
   - **Troubleshooting**. Use o comando `CTRL + Shift + P` para acessar os atalhos do **VS Code**. Busque pela opção `Python: Select Interpreter` e escolha o **python** disponível que foi instalado.
   - **Alternativa**: crie uma pasta na raiz do seu projeto `.vscode`e inclua um novo arquivo `settings.json`. Copie o seguinte código: 
   
   ```json
   {
    "python.defaultInterpreterPath": "${workspaceFolder}\\venv-curso-ipea\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "python.venvPath": "${workspaceFolder}",
    "python.analysis.autoImportCompletions": true,
    "python.analysis.typeCheckingMode": "basic",

    // Windows terminal padrão
    "terminal.integrated.defaultProfile.windows": "PowerShell",

    // Ocultar pastas/arquivos desnecessários no Explorer
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
       }
   }

    ```


5. **Verificar Instalação**
```python
# executar no terminal (na barra de cima Terminal/New terminal):
python --version
pip --version
```
- Se a versão que aparecer for diferente, pode ser que você tenha que indicar ao **VS Code** qual o caminho correto (usando CTRL+Shift+P)


6. **Instalar bibliotecas dentro do environment do curso**
**Bibliotecas principais**

- **Opção 1**
   - Abra o terminal. Você **DEVE** ver `(venv-curso-ipea)` antes do prompt. 
      - Caso você veja `(base)`, significa que você não está dentro do ambiente criado. **Pode prosseguir**, mas as bibliotecas serão instaladas no ambiente geral e não no criado por você. 
      - Para entrar no ambiente correto, caso ele tenha sido criado, digite no Terminal: `venv-curso-ipea\Scripts\activate`, 
   Digite: 
   - `pip install pandas numpy scikit-learn jupyter matplotlib seaborn plotly openpyxl`
      - *Caso veja `(base)`, isso indica que você não está no ambiente correto. Digite no Terminal `venv-curso-ipea\Scripts\activate`*
- **Opção 2**
   - Crie um arquivo `requirements.txt` na raiz do projeto. **Exemplo**: `https://github.com/BAFurtado/python-ipea-fundamentos-objetos/blob/main/configuracao/requirements.txt`
   - No Terminal, digite: `pip install -r requirements.txt`


7. **Tenha um arquivo .gitignore**
Evite que arquivos desnecessários sejam enviados para o repositório na nuvem. 

Copie as seguintes configurações em um arquivo na raiz do seu projeto nomeado `.gitignore` (File/New File)

```bash
# Environments
venv-curso-ipea/
env/
.venv/

# **VS Code**
.vscode/
*.code-workspace

# Python
__pycache__/
*.pyc
*.pyo
.python-version

# Dados grandes
dados/raw/
*.csv
*.xlsx
!dados/exemplos/sample_data.csv
```

8. **Desafio: teste avançado de instalação**
- No seu workspace, dentro do explorer do **VS Code**, crie uma pasta configuracao (note, sem acentos ou cedilha), dê download do arquivo em: https://github.com/BAFurtado/python-ipea-fundamentos-objetos/blob/main/configuracao/verificacao-instalacao.py
- No Terminal, dentro do ambiente criado `(venv-curso-ipea)`, na raiz do projeto, digite: 

   `python configuracao/verificacao-instalacao.py`. 

- Esse comando vai rodar o `script` correspondente na pasta configuracao (confira o caminho do arquivo) e imprimir o diagnóstico da sua instalação!

### Caveats--detalhes--troubleshooting

1. Caso tenha mais de um **python** instalado no seu computador, pode ser necessário `CTRL+Shift+P` (abre a paletta de comando do **VS Code**) e digite `Python: Select interpreter` (para avisar ao **VS Code** qual versão de Python seu projeto irá utilizar). Se os **pythons** forem de tentativas de instalações frustadas anteriores, vale a pena deletá-los e começar novamente com a versão 3.12.10.
2. Logo que abrir o **VS Code**, use a opção `File/Open Folder` para indicar o caminho da pasta que vai utilizar para o curso. 
3. Em um momento seguinte do curso, vamos `clonar` o repositório diretamente do GitHub.
4. Se houver um arquivo de bibliotecas necessárias, utilize `pip install -r configuracao/requirements.txt` para instalar direto do arquivo. Tenha certeza de que está no ambiente certo--aparecerá *(venv-curso-ipea)* no prompt do Terminal
5. Se tiver problemas de permissão no Windows, use: `pip install --user pandas numpy scikit-learn jupyter matplotlib seaborn`
6. Sempre confira em qual diretório o seu prompt está, em qual pasta está o script a ser rodado. Confira ainda se o ambiente está ativo (aparece o nome entre parenteses, antes do prompt)
7. Se o python não estiver sendo reconhecido pelo sistema, tente adicionar o caminho (descubra o caminho com `where python`) ao **PATH** do sistema: 
   - System Properties → Environment Variables → PATH
      - Ou: Propriedades do sistema → Variáveis de ambiente → PATH
   - Adicione: C:\caminho\para\python312\
8. - Atenção: [Boas práticas Windows](boaspraticas.md)