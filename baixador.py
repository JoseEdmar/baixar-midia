#!/usr/bin/env python3

import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO
# ============================================================

APP_DIR = Path.home() / "Downloads" / "Baixador Midia"
APP_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOCALIZAR PROGRAMAS
# ============================================================

def find_cmd(name):
    return shutil.which(name)


# ============================================================
# MONTAR COMANDO
# ============================================================

def build_cmd(url, mode):

    ytdlp = find_cmd("yt-dlp")
    node = find_cmd("node")

    if not ytdlp:
        raise RuntimeError(
            "yt-dlp não foi encontrado.\n\n"
            "Instale o yt-dlp e tente novamente."
        )

    if not node:
        raise RuntimeError(
            "Node.js não foi encontrado.\n\n"
            "Instale o Node.js e tente novamente."
        )

    if mode == "MP4" and not find_cmd("ffmpeg"):
        raise RuntimeError(
            "FFmpeg não foi encontrado.\n\n"
            "O FFmpeg é necessário para juntar vídeo e áudio em MP4."
        )

    cmd = [
        ytdlp,
        "--no-playlist",
        "--remote-components",
        "ejs:github",
        "--js-runtimes",
        "node",
        "--cookies-from-browser",
        "firefox",
    ]

    if mode == "MP4":
        cmd += [
            "-f",
            "bv*+ba/b",
            "--merge-output-format",
            "mp4",
            "-o",
            str(APP_DIR / "%(title)s.%(ext)s"),
            url,
        ]

    else:
        cmd += [
            "-x",
            "--audio-format",
            "mp3",
            "--audio-quality",
            "0",
            "-o",
            str(APP_DIR / "%(title)s.%(ext)s"),
            url,
        ]

    return cmd


# ============================================================
# ABRIR PASTA
# ============================================================

def open_folder():

    try:
        if shutil.which("xdg-open"):
            subprocess.Popen(
                ["xdg-open", str(APP_DIR)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        elif shutil.which("explorer.exe"):
            subprocess.Popen(
                ["explorer.exe", str(APP_DIR)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        elif shutil.which("open"):
            subprocess.Popen(
                ["open", str(APP_DIR)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        else:
            messagebox.showinfo("Pasta", str(APP_DIR))

    except Exception as error:
        messagebox.showerror("Erro", f"Não foi possível abrir a pasta:\n\n{error}")


# ============================================================
# DOWNLOAD
# ============================================================

def download():

    url = url_var.get().strip()
    mode = mode_var.get()

    if not url:
        messagebox.showwarning(
            "Falta o link",
            "Cole a URL do vídeo.",
        )
        return

    try:
        cmd = build_cmd(url, mode)

    except Exception as error:
        messagebox.showerror("Erro", str(error))
        return

    # Abre a pasta para acompanhar o arquivo.
    open_folder()

    def run_download():

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            # Mantém o processo independente da interface.
            process.wait()

        except Exception as error:
            root.after(
                0,
                lambda: messagebox.showerror(
                    "Erro no download",
                    str(error),
                ),
            )

    threading.Thread(
        target=run_download,
        daemon=True,
    ).start()

    status_var.set(
        "Download iniciado. Acompanhe o arquivo na pasta."
    )

    url_var.set("")
    entry.focus_set()


# ============================================================
# JANELA
# ============================================================

root = tk.Tk()

root.title("Baixador de Vídeos")
root.geometry("650x330")
root.resizable(False, False)


# ============================================================
# TÍTULO
# ============================================================

tk.Label(
    root,
    text="Baixador de Vídeos",
    font=("Arial", 20, "bold"),
).pack(pady=(25, 5))

tk.Label(
    root,
    text="Cole o link e escolha o formato",
).pack(pady=(0, 20))


# ============================================================
# URL
# ============================================================

frame = tk.Frame(root)
frame.pack(fill="x", padx=30)

tk.Label(
    frame,
    text="URL:",
    font=("Arial", 11, "bold"),
).pack(anchor="w")

url_var = tk.StringVar()

entry = tk.Entry(
    frame,
    textvariable=url_var,
    font=("Arial", 11),
)

entry.pack(
    fill="x",
    pady=(5, 15),
)

entry.focus()


# ============================================================
# FORMATO
# ============================================================

mode_var = tk.StringVar(value="MP4")

opts = tk.Frame(frame)
opts.pack(anchor="w", pady=(0, 15))

tk.Label(
    opts,
    text="Formato:",
    font=("Arial", 11, "bold"),
).pack(side="left", padx=(0, 10))

tk.Radiobutton(
    opts,
    text="Vídeo MP4",
    variable=mode_var,
    value="MP4",
).pack(side="left", padx=5)

tk.Radiobutton(
    opts,
    text="Áudio MP3",
    variable=mode_var,
    value="MP3",
).pack(side="left", padx=5)


# ============================================================
# BOTÕES
# ============================================================

buttons = tk.Frame(root)
buttons.pack(pady=5)

tk.Button(
    buttons,
    text="BAIXAR",
    width=18,
    height=2,
    command=download,
).pack(side="left", padx=5)

tk.Button(
    buttons,
    text="Abrir pasta",
    width=18,
    height=2,
    command=open_folder,
).pack(side="left", padx=5)


# ============================================================
# STATUS
# ============================================================

status_var = tk.StringVar(
    value=f"Arquivos serão salvos em: {APP_DIR}"
)

tk.Label(
    root,
    textvariable=status_var,
    fg="gray",
    wraplength=580,
).pack(pady=20)


# ============================================================
# INICIAR
# ============================================================

root.mainloop()
