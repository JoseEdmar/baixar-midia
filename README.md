# 📥 Baixador de Mídia

Aplicativo desktop simples para download de vídeos e áudios utilizando o [yt-dlp](https://github.com/yt-dlp/yt-dlp) como mecanismo de download.

A aplicação possui uma interface gráfica própria, desenvolvida em Python com Tkinter, com foco em simplicidade e facilidade de uso.

---

## ✨ Funcionalidades

* 📥 Download de vídeos
* 🎵 Download e extração de áudio em MP3
* 🖥️ Interface gráfica simples e intuitiva
* 📂 Salvamento automático dos arquivos na pasta de downloads
* ⚙️ Utilização do `yt-dlp` como mecanismo de download
* 🎬 Utilização do FFmpeg para processamento e conversão de mídia
* 🐍 Desenvolvido em Python
* 📦 Possibilidade de compilação como executável para Windows

---

## 🖼️ Interface

A interface gráfica foi desenvolvida especificamente para este projeto utilizando **Tkinter**.

O objetivo é oferecer uma maneira simples de utilizar o `yt-dlp` sem precisar executar comandos diretamente pelo terminal.

O usuário pode:

1. Inserir a URL da mídia;
2. Escolher entre **Vídeo MP4** ou **Áudio MP3**;
3. Iniciar o download;
4. Abrir diretamente a pasta onde os arquivos são salvos.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Tkinter**
* **yt-dlp**
* **Node.js** — utilizado como runtime JavaScript pelo yt-dlp
* **FFmpeg** — utilizado para processamento, conversão e junção de mídia
* **PyInstaller** — utilizado para gerar executáveis

---

## 📁 Estrutura do projeto

```text
Baixador-Midia/
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── iniciar.bat
```

> A estrutura pode variar conforme a versão do projeto.

---

## 🚀 Instalação

### 1. Pré-requisitos

Antes de executar o projeto, é necessário possuir:

* **Python 3**
* **Node.js**
* **FFmpeg**
* **Firefox**

O Firefox é utilizado pelo `yt-dlp` para obter os cookies do navegador através da opção `--cookies-from-browser firefox`.

### 2. Clonar o repositório

```bash
git clone https://github.com/JoseEdmar/Baixador-Midia.git
```

Entre na pasta do projeto:

```bash
cd Baixador-Midia
```

### 3. Instalar as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Executar o programa

```bash
python main.py
```

---

## 📦 Dependências externas

Além das dependências Python presentes no `requirements.txt`, o programa utiliza alguns softwares externos.

### yt-dlp

É o mecanismo responsável pelo download das mídias.

O projeto utiliza o `yt-dlp` através de uma chamada externa ao programa instalado no sistema.

### Node.js

O Node.js é utilizado como runtime JavaScript pelo `yt-dlp`.

O programa verifica automaticamente se o comando `node` está disponível no sistema.

### FFmpeg

O FFmpeg é utilizado pelo `yt-dlp` para operações de processamento de mídia, como:

* juntar vídeo e áudio;
* conversão para MP4;
* extração/conversão para MP3.

O programa verifica automaticamente se o FFmpeg está disponível quando necessário.

### Firefox

O programa utiliza:

```text
--cookies-from-browser firefox
```

para permitir que o `yt-dlp` utilize os cookies armazenados no Firefox.

Por isso, o Firefox precisa estar instalado e configurado no computador.

---

## 📂 Local dos arquivos baixados

Os arquivos são salvos automaticamente na pasta:

```text
~/Downloads/Baixador Midia
```

No Windows, o caminho corresponde à pasta `Downloads` do usuário atual.

O botão **"Abrir pasta"** abre automaticamente esse diretório no sistema operacional.

---

## ⚙️ Como funciona

O aplicativo fornece uma interface gráfica para o usuário inserir o endereço da mídia que deseja baixar.

A aplicação monta o comando necessário e executa o `yt-dlp` em segundo plano.

De forma simplificada:

```text
Usuário
   │
   ▼
Interface gráfica
   │
   ▼
Baixador de Mídia
   │
   ▼
yt-dlp
   │
   ├── Node.js
   │
   └── FFmpeg
   │
   ▼
Arquivo de mídia
```

---

## 🎬 Formatos disponíveis

### Vídeo MP4

O modo MP4 utiliza o `yt-dlp` para obter vídeo e áudio e, quando necessário, utiliza o FFmpeg para realizar a junção.

### Áudio MP3

O modo MP3 utiliza o `yt-dlp` para extrair o áudio e convertê-lo para MP3 utilizando o FFmpeg.

---

## 📦 Gerando um executável

O projeto pode ser compilado utilizando o **PyInstaller**.

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Depois execute:

```bash
pyinstaller --onefile --windowed main.py
```

O executável será criado dentro da pasta:

```text
dist/
```

> Dependendo da forma como o projeto for distribuído, os programas externos utilizados pelo aplicativo, como FFmpeg, Node.js e yt-dlp, podem continuar sendo necessários no computador do usuário.

---

## ⚠️ Observações

Este projeto fornece uma interface gráfica para facilitar a utilização do `yt-dlp`.

A disponibilidade dos downloads depende do site de origem, das configurações utilizadas e das condições de acesso aplicáveis ao conteúdo.

O usuário é responsável por garantir que possui autorização para baixar e utilizar o conteúdo escolhido.

O funcionamento também depende da disponibilidade e compatibilidade das ferramentas externas utilizadas pelo projeto.

---

## 📜 Licença

### Código original deste projeto

O código original desenvolvido para este projeto, incluindo a **interface gráfica**, scripts e demais componentes criados pelo autor, é disponibilizado sob a licença **MIT**.

Isso significa que o código original pode ser utilizado, copiado, modificado, distribuído e utilizado comercialmente, desde que os termos da licença sejam respeitados.

### yt-dlp

Este projeto utiliza o **yt-dlp** como componente externo para realizar os downloads.

O **yt-dlp é um projeto independente** e permanece sujeito à sua própria licença e aos seus respectivos direitos autorais.

Mais informações:

* Repositório oficial: https://github.com/yt-dlp/yt-dlp
* Licença do yt-dlp: https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE

### Outras dependências

As demais bibliotecas e componentes utilizados pelo projeto permanecem sujeitos às suas respectivas licenças.

---

## 📄 Licença MIT

Copyright (c) 2026 José Edmar Constantino Gouveia

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.

---

## 👨‍💻 Autor

**José Edmar Constantino Gouveia**

Projeto desenvolvido para facilitar o uso do yt-dlp através de uma interface gráfica simples e prática.