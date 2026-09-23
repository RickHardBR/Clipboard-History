# 📋 Clipboard History Manager

<p align="center">
  <b>Português</b> | <a href="README.en.md">English</a> | <a href="README.es.md">Español</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20%7C%20ttkbootstrap-darkgreen" alt="GUI Framework" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white" alt="Platform" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
</p>

Um gerenciador de histórico da área de transferência moderno, rápido e leve para **Windows**, desenvolvido em **Python** com **Tkinter** e **ttkbootstrap**. 

Monitore automaticamente tudo o que copia (textos, URLs e imagens), organize por abas com design refinado, edite itens com facilidade e personalize o tema e o idioma da aplicação com atualização em tempo real.

---

## ✨ Principais Funcionalidades

- 🔄 **Monitoramento Contínuo do Clipboard**: Captura automática de textos, links web e capturas de tela/imagens sem interferir no fluxo de trabalho.
- 🗂️ **Categorização Inteligente em Abas**:
  - **Textos**: Histórico de textos convencionais copiados.
  - **Links**: Identificação e separação automática de links (`http://` e `https://`).
  - **Imagens**: Histórico com miniaturas e data/hora das capturas.
- 🎨 **Interface Moderna e Personalizada**:
  - Componentes desenhados em Canvas (`RoundedButton`, `CustomTabBar`, `CustomList`) com cantos arredondados, feedback de hover suave e destaque da seleção ativa em estilo *pill*.
  - Scrollbars discretas integradas à paleta visual.
  - Suporte completo a **Tema Escuro (Dark)** e **Tema Claro (Light)**.
  - 4 Cores de Destaque (*Accent Colors*): **Roxo**, **Verde-água**, **Azul** e **Vermelho**.
- 🌐 **Suporte Multi-idioma (i18n)**:
  - 🇧🇷 Português (Brasil)
  - 🇺🇸 English
  - 🇪🇸 Español
- ⚡ **Hot-Reload de Preferências**: Mude o tema, a cor de destaque ou o idioma e veja o programa se reconfigurar instantaneamente, **sem necessidade de reiniciar**.
- 🖼️ **4 Modos de Visualização para Imagens**:
  - Detalhes (Lista com data, hora e hash do arquivo)
  - Ícones Pequenos (64x64)
  - Ícones Médios (128x128)
  - Ícones Grandes (256x256)
- ✏️ **Editor Integrado**: Janela flutuante para visualizar e corrigir textos rapidamente.
- 💾 **Exportação Rápida**: Salve qualquer texto ou link selecionado diretamente em arquivo `.txt`.
- 🗑️ **Lixeira Completa (Apagados)**: Exclua itens com segurança, com opção de restaurar ou eliminar definitivamente.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.12](https://www.python.org/)** — Linguagem principal.
- **Tkinter** — Framework nativo de interface gráfica.
- **[ttkbootstrap](https://ttkbootstrap.readthedocs.io/)** — Temas visuais e estilização de widgets do sistema.
- **[Pillow (PIL)](https://python-pillow.org/)** — Manipulação, captura e renderização de imagens do clipboard.
- **[PyInstaller](https://pyinstaller.org/)** — Empacotamento do programa em executável `.exe` independente.

---

## 📂 Estrutura do Projeto

```plaintext
Clipboard History/
│
├── .gitignore             # Arquivos e pastas ignorados pelo Git
├── clipboard_history.py   # Código-fonte principal da aplicação
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação em português (padrão)
├── README.en.md           # Documentação em inglês
└── README.es.md           # Documentação em espanhol
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3.10 ou superior** instalado no seu computador.

### 1. Clonar o repositório

```bash
git clone https://github.com/RickHardBR/Clipboard-History.git
cd Clipboard-History
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a aplicação

```bash
python clipboard_history.py
```

---

## 📦 Como Gerar o Executável (.exe)

O programa pode ser compilado em um único executável independente para Windows, sem exigir o Python instalado na máquina de destino.

Execute o comando abaixo no terminal da pasta do projeto:

```powershell
pyinstaller --onefile --windowed --name "ClipboardHistory" clipboard_history.py
```

O arquivo final estará disponível na pasta:
```
dist/ClipboardHistory.exe
```

> **Nota:** A flag `--windowed` garante que o executável rode em modo janela limpo, sem abrir o terminal de comandos do Windows.

---

## ⚙️ Configurações e Preferências

As configurações ficam salvas no arquivo `config.json` gerado automaticamente na raiz do projeto:

```json
{
    "theme": "dark",
    "accent_color": "#7c5cff",
    "language": "pt_BR"
}
```

Para alterar:
1. Abra o menu **Configurações > Preferências** (ou clique nas opções correspondentes no seu idioma).
2. Escolha o **Tema Visual**, a **Cor de Destaque** e o **Idioma**.
3. Clique em **Aplicar e Salvar**. As alterações são refletidas na hora!

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE). Sinta-se livre para usar, modificar e distribuir.

---

<p align="center">
  Desenvolvido por <b>RickHardBR</b> 🚀
</p>
