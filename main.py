#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keystroke Overlay - COM MENU DE SELECAO DE LAYOUT
====================================================

ESCOLHA SEU LAYOUT:
    1. WASD + Mouse        -> W, A, S, D, Espaco + Mouse
    2. Teclado Completo    -> QWERTY completo + numeros + F1-F12 + Setas
    3. Numpad + Setas      -> Teclado numerico + Setas + Mouse
    4. Parte Direita       -> Setas + Insert/Home/PgUp/PgDn + Numpad + Mouse
    5. Mao Esquerda        -> Teclas da esquerda ate G + Mouse (branco)
    6. Mao Direita         -> Teclas da direita a partir de H + Mouse (cores por dedo)

COMO USAR:
    python main.py

CONTROLES (no overlay):
    - CLIQUE E ARRASTE em qualquer lugar = move o overlay
    - END = fecha
"""

import tkinter as tk
from tkinter import ttk
import math
import ctypes
from ctypes import wintypes


# =============================================================================
# API DO WINDOWS
# =============================================================================
user32 = ctypes.windll.user32
user32.GetAsyncKeyState.argtypes = [wintypes.INT]
user32.GetAsyncKeyState.restype = wintypes.SHORT

HWND_TOPMOST = -1
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010
SWP_SHOWWINDOW = 0x0040

user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT,
                                 wintypes.INT, wintypes.INT, wintypes.UINT]
user32.SetWindowPos.restype = wintypes.BOOL
SetWindowPos = user32.SetWindowPos

# Virtual Key Codes
VK_CODES = {
    "W": 0x57, "A": 0x41, "S": 0x53, "D": 0x44,
    "Q": 0x51, "E": 0x45, "R": 0x52, "T": 0x54,
    "Y": 0x59, "U": 0x55, "I": 0x49, "O": 0x4F, "P": 0x50,
    "F": 0x46, "G": 0x47, "H": 0x48, "J": 0x4A, "K": 0x4B, "L": 0x4C,
    "Z": 0x5A, "X": 0x58, "C": 0x43, "V": 0x56, "B": 0x42, "N": 0x4E, "M": 0x4D,
    "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35,
    "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39, "0": 0x30,
    "F1": 0x70, "F2": 0x71, "F3": 0x72, "F4": 0x73,
    "F5": 0x74, "F6": 0x75, "F7": 0x76, "F8": 0x77,
    "F9": 0x78, "F10": 0x79, "F11": 0x7A, "F12": 0x7B,
    "SPACE": 0x20, "ENTER": 0x0D, "SHIFT": 0x10, "CTRL": 0x11,
    "RSHIFT": 0xA1, "RCTRL": 0xA3,
    "ALT": 0x12, "TAB": 0x09, "BACK": 0x08, "CAPS": 0x14,
    "UP": 0x26, "DOWN": 0x28, "LEFT": 0x25, "RIGHT": 0x27,
    "INS": 0x2D, "HOME": 0x24, "PGUP": 0x21, "PGDN": 0x22, "DEL": 0x2E, "END": 0x23,
    "NUM0": 0x60, "NUM1": 0x61, "NUM2": 0x62, "NUM3": 0x63,
    "NUM4": 0x64, "NUM5": 0x65, "NUM6": 0x66, "NUM7": 0x67,
    "NUM8": 0x68, "NUM9": 0x69, "NUM.": 0x6E,
    "NUM+": 0x6B, "NUM-": 0x6D, "NUM*": 0x6A, "NUM/": 0x6F,
    "LMB": 0x01, "RMB": 0x02,
    "OEM1": 0xBA, "OEM2": 0xBF, "OEM3": 0xC0,
    "OEM4": 0xDB, "OEM5": 0xDC, "OEM6": 0xDD,
    "OEM7": 0xDE, "OEM102": 0xE2,
}

VK_END_CLOSE = 0x23


# =============================================================================
# CORES POR DEDO
# =============================================================================
CORES_DEDOS = {
    "mindinho_esq":  {"idle": "#ff9999", "active": "#ff3333"},
    "anelar_esq":    {"idle": "#99e6e6", "active": "#ff3333"},
    "medio_esq":     {"idle": "#fff099", "active": "#ff3333"},
    "indicador_esq": {"idle": "#99ffcc", "active": "#ff3333"},
    "polegar_esq":   {"idle": "#a8d8ea", "active": "#ff3333"},
    "indicador_dir": {"idle": "#99ffcc", "active": "#ff3333"},
    "medio_dir":     {"idle": "#fff099", "active": "#ff3333"},
    "anelar_dir":    {"idle": "#99e6e6", "active": "#ff3333"},
    "mindinho_dir":  {"idle": "#ff9999", "active": "#ff3333"},
    "polegar_dir":   {"idle": "#a8d8ea", "active": "#ff3333"},
    "padrao":        {"idle": "#ffffff", "active": "#ff3333"},
}


# =============================================================================
# FUNCOES AUXILIARES DE DESENHO
# =============================================================================
def arco(cx, cy, r, start, end, steps=5):
    pts = []
    for i in range(steps + 1):
        ang = math.radians(start + (end - start) * i / steps)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts

def rounded_rect(cx, cy, w, h, r):
    x1, y1 = cx - w // 2, cy - h // 2
    x2, y2 = cx + w // 2, cy + h // 2
    pts = []
    pts.extend(arco(x1 + r, y1 + r, r, 180, 270))
    pts.append((x2 - r, y1))
    pts.extend(arco(x2 - r, y1 + r, r, 270, 360))
    pts.append((x2, y2 - r))
    pts.extend(arco(x2 - r, y2 - r, r, 0, 90))
    pts.append((x1 + r, y2))
    pts.extend(arco(x1 + r, y2 - r, r, 90, 180))
    pts.append((x1, y1 + r))
    flat = []
    for px, py in pts:
        flat.extend([px, py])
    return flat


# =============================================================================
# DEFINICAO DOS LAYOUTS
# =============================================================================
LAYOUTS = {
    "wasd": {
        "name": "WASD + Mouse",
        "win_size": (220, 120),
        "keys": [
            ("W", "W", 87, 28, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("A", "A", 52, 63, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("S", "S", 87, 63, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("D", "D", 122, 63, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("____", "SPACE", 87, 98, 82, 32, ("Segoe UI", 7, "bold"), "padrao"),
        ],
        "mouse": (160, 63, 22, 40),
    },
    "full": {
        "name": "Teclado Completo",
        "win_size": (580, 220),
        "keys": [
            ("F1", "F1", 30, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F2", "F2", 62, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F3", "F3", 94, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F4", "F4", 126, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F5", "F5", 168, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F6", "F6", 200, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F7", "F7", 232, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F8", "F8", 264, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F9", "F9", 306, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F10", "F10", 338, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F11", "F11", 370, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("F12", "F12", 402, 20, 28, 18, ("Segoe UI", 6, "bold"), "padrao"),
            ("1", "1", 20, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("2", "2", 48, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("3", "3", 76, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("4", "4", 104, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("5", "5", 132, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("6", "6", 160, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("7", "7", 188, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("8", "8", 216, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("9", "9", 244, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("0", "0", 272, 48, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("Q", "Q", 32, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("W", "W", 60, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("E", "E", 88, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("R", "R", 116, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("T", "T", 144, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("Y", "Y", 172, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("U", "U", 200, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("I", "I", 228, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("O", "O", 256, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("P", "P", 284, 78, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("A", "A", 44, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("S", "S", 72, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("D", "D", 100, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("F", "F", 128, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("G", "G", 156, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("H", "H", 184, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("J", "J", 212, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("K", "K", 240, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("L", "L", 268, 108, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("Z", "Z", 56, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("X", "X", 84, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("C", "C", 112, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("V", "V", 140, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("B", "B", 168, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("N", "N", 196, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("M", "M", 224, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("SHIFT", "SHIFT", 50, 168, 50, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("____", "SPACE", 140, 168, 100, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("ENTER", "ENTER", 260, 168, 50, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("CTRL", "CTRL", 320, 168, 40, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("^", "UP", 480, 138, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("<", "LEFT", 452, 168, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("v", "DOWN", 480, 168, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            (">", "RIGHT", 508, 168, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("TAB", "TAB", 320, 48, 36, 24, ("Segoe UI", 6, "bold"), "padrao"),
            ("CAPS", "CAPS", 320, 78, 40, 24, ("Segoe UI", 5, "bold"), "padrao"),
            ("BKSP", "BACK", 320, 108, 40, 24, ("Segoe UI", 5, "bold"), "padrao"),
            ("ALT", "ALT", 370, 168, 36, 22, ("Segoe UI", 6, "bold"), "padrao"),
        ],
        "mouse": (420, 78, 22, 40),
    },
    "numpad": {
        "name": "Numpad + Setas + Mouse",
        "win_size": (280, 200),
        "keys": [
            ("7", "NUM7", 30, 30, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("8", "NUM8", 68, 30, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("9", "NUM9", 106, 30, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("4", "NUM4", 30, 68, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("5", "NUM5", 68, 68, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("6", "NUM6", 106, 68, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("1", "NUM1", 30, 106, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("2", "NUM2", 68, 106, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("3", "NUM3", 106, 106, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("0", "NUM0", 30, 144, 70, 32, ("Segoe UI", 11, "bold"), "padrao"),
            (".", "NUM.", 106, 144, 32, 32, ("Segoe UI", 11, "bold"), "padrao"),
            ("/", "NUM/", 150, 30, 28, 28, ("Segoe UI", 9, "bold"), "padrao"),
            ("*", "NUM*", 150, 62, 28, 28, ("Segoe UI", 9, "bold"), "padrao"),
            ("-", "NUM-", 150, 94, 28, 28, ("Segoe UI", 9, "bold"), "padrao"),
            ("+", "NUM+", 150, 126, 28, 50, ("Segoe UI", 9, "bold"), "padrao"),
            ("^", "UP", 68, 182, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("<", "LEFT", 40, 182, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("v", "DOWN", 68, 182, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            (">", "RIGHT", 96, 182, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
        ],
        "mouse": (230, 100, 22, 40),
    },
    "right": {
        "name": "Parte Direita + Mouse",
        "win_size": (320, 180),
        "keys": [
            ("INS", "INS", 30, 25, 36, 22, ("Segoe UI", 7, "bold"), "padrao"),
            ("HOME", "HOME", 72, 25, 36, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("PGUP", "PGUP", 114, 25, 36, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("DEL", "DEL", 30, 52, 36, 22, ("Segoe UI", 7, "bold"), "padrao"),
            ("END", "END", 72, 52, 36, 22, ("Segoe UI", 7, "bold"), "padrao"),
            ("PGDN", "PGDN", 114, 52, 36, 22, ("Segoe UI", 6, "bold"), "padrao"),
            ("^", "UP", 72, 90, 28, 28, ("Segoe UI", 10, "bold"), "padrao"),
            ("<", "LEFT", 40, 122, 28, 28, ("Segoe UI", 10, "bold"), "padrao"),
            ("v", "DOWN", 72, 122, 28, 28, ("Segoe UI", 10, "bold"), "padrao"),
            (">", "RIGHT", 104, 122, 28, 28, ("Segoe UI", 10, "bold"), "padrao"),
            ("7", "NUM7", 160, 25, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("8", "NUM8", 190, 25, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("9", "NUM9", 220, 25, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("4", "NUM4", 160, 55, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("5", "NUM5", 190, 55, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("6", "NUM6", 220, 55, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("1", "NUM1", 160, 85, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("2", "NUM2", 190, 85, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("3", "NUM3", 220, 85, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("0", "NUM0", 160, 115, 56, 26, ("Segoe UI", 8, "bold"), "padrao"),
            (".", "NUM.", 220, 115, 26, 26, ("Segoe UI", 8, "bold"), "padrao"),
            ("ENTER", "ENTER", 30, 160, 60, 24, ("Segoe UI", 7, "bold"), "padrao"),
            ("SHIFT", "RSHIFT", 100, 160, 50, 24, ("Segoe UI", 7, "bold"), "padrao"),
            ("CTRL", "RCTRL", 160, 160, 40, 24, ("Segoe UI", 7, "bold"), "padrao"),
            ("ALT", "ALT", 206, 160, 36, 24, ("Segoe UI", 7, "bold"), "padrao"),
        ],
        "mouse": (280, 90, 22, 40),
    },
    # =============================================================================
    # MAO ESQUERDA - TUDO BRANCO (padrao) + MOUSE
    # =============================================================================
    "mao_esq": {
        "name": "Mao Esquerda + Mouse (branco)",
        "win_size": (420, 210),
        "keys": [
            # MINDINHO (branco)
            ("'", "OEM3", 22, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("1", "1", 50, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("Q", "Q", 50, 52, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("A", "A", 50, 82, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("Z", "Z", 50, 112, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("SHIFT", "SHIFT", 22, 142, 54, 24, ("Segoe UI", 6, "bold"), "padrao"),
            ("CTRL", "CTRL", 22, 172, 44, 24, ("Segoe UI", 6, "bold"), "padrao"),
            ("CAPS", "CAPS", 22, 82, 44, 24, ("Segoe UI", 5, "bold"), "padrao"),
            ("TAB", "TAB", 22, 52, 44, 24, ("Segoe UI", 6, "bold"), "padrao"),

            # ANELAR (branco)
            ("2", "2", 78, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("W", "W", 78, 52, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("S", "S", 78, 82, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("X", "X", 78, 112, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),

            # MEDIO (branco)
            ("3", "3", 106, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("E", "E", 106, 52, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("D", "D", 106, 82, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("C", "C", 106, 112, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),

            # INDICADOR COL 1 (branco)
            ("4", "4", 134, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("R", "R", 134, 52, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("F", "F", 134, 82, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("V", "V", 134, 112, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),

            # INDICADOR COL 2 (branco)
            ("5", "5", 162, 22, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("T", "T", 162, 52, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("G", "G", 162, 82, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),
            ("B", "B", 162, 112, 24, 24, ("Segoe UI", 8, "bold"), "padrao"),

            # POLEGAR (branco)
            ("____", "SPACE", 100, 172, 90, 24, ("Segoe UI", 6, "bold"), "padrao"),
        ],
        "mouse": (340, 80, 22, 40),
    },
    # =============================================================================
    # MAO DIREITA - COM CORES POR DEDO + MOUSE
    # =============================================================================
    "mao_dir": {
        "name": "Mao Direita + Mouse (cores por dedo)",
        "win_size": (520, 230),
        "keys": [
            # INDICADOR COL 1 (verde)
            ("6", "6", 22, 22, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("Y", "Y", 22, 52, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("H", "H", 22, 82, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("N", "N", 22, 112, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),

            # INDICADOR COL 2 (verde)
            ("7", "7", 50, 22, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("U", "U", 50, 52, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("J", "J", 50, 82, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),
            ("M", "M", 50, 112, 24, 24, ("Segoe UI", 8, "bold"), "indicador_dir"),

            # MEDIO (amarelo)
            ("8", "8", 78, 22, 24, 24, ("Segoe UI", 8, "bold"), "medio_dir"),
            ("I", "I", 78, 52, 24, 24, ("Segoe UI", 8, "bold"), "medio_dir"),
            ("K", "K", 78, 82, 24, 24, ("Segoe UI", 8, "bold"), "medio_dir"),
            (",", "OEM102", 78, 112, 24, 24, ("Segoe UI", 8, "bold"), "medio_dir"),

            # ANELAR (turquesa)
            ("9", "9", 106, 22, 24, 24, ("Segoe UI", 8, "bold"), "anelar_dir"),
            ("O", "O", 106, 52, 24, 24, ("Segoe UI", 8, "bold"), "anelar_dir"),
            ("L", "L", 106, 82, 24, 24, ("Segoe UI", 8, "bold"), "anelar_dir"),
            (".", "OEM2", 106, 112, 24, 24, ("Segoe UI", 8, "bold"), "anelar_dir"),

            # MINDINHO (vermelho)
            ("0", "0", 134, 22, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("-", "OEM4", 162, 22, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("=", "OEM6", 190, 22, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("P", "P", 134, 52, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("´", "OEM7", 162, 52, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("[", "OEM5", 190, 52, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("Ç", "OEM1", 134, 82, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("~", "OEM3", 162, 82, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("]", "OEM6", 190, 82, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            (";", "OEM2", 134, 112, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("/", "OEM102", 162, 112, 24, 24, ("Segoe UI", 8, "bold"), "mindinho_dir"),
            ("BKSP", "BACK", 218, 22, 48, 24, ("Segoe UI", 5, "bold"), "mindinho_dir"),
            ("ENTER", "ENTER", 218, 82, 48, 24, ("Segoe UI", 6, "bold"), "mindinho_dir"),
            ("SHIFT", "RSHIFT", 190, 142, 54, 24, ("Segoe UI", 6, "bold"), "mindinho_dir"),

            # POLEGAR (azul)
            ("____", "SPACE", 100, 172, 90, 24, ("Segoe UI", 6, "bold"), "polegar_dir"),
        ],
        "mouse": (440, 100, 22, 40),
        "legenda": True,
    },
}


# =============================================================================
# MENU DE SELECAO (TKINTER)
# =============================================================================
class MenuSelecao:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keystroke Overlay - Selecione o Layout")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w, h = 520, 560
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        # Titulo
        tk.Label(self.root, text="ESCOLHA SEU LAYOUT", font=("Segoe UI", 22, "bold"),
                 bg="#1a1a1a", fg="white").pack(pady=(20, 5))

        tk.Label(self.root, text="Selecione qual parte do teclado voce quer exibir",
                 font=("Segoe UI", 10), bg="#1a1a1a", fg="#aaaaaa").pack(pady=(0, 10))

        # Frame dos botoes
        frame = tk.Frame(self.root, bg="#1a1a1a")
        frame.pack(pady=5)

        layouts = [
            ("wasd", "WASD + Mouse", "W, A, S, D, Espaco\n+ Botao Esquerdo e Direito do Mouse", "#ff4444"),
            ("full", "Teclado Completo", "QWERTY + Numeros + F1-F12\n+ Setas + Shift/Ctrl/Enter/Tab", "#4488ff"),
            ("numpad", "Numpad + Setas + Mouse", "Teclado Numerico (0-9)\n+ Operadores + Setas + Mouse", "#44ff88"),
            ("right", "Parte Direita + Mouse", "Setas + Insert/Home/PgUp/PgDn\n+ Numpad + Enter/Shift + Mouse", "#ffaa44"),
            ("mao_esq", "Mao Esquerda + Mouse", "Teclas da esquerda ate G\nTUDO BRANCO + Mouse", "#dddddd"),
            ("mao_dir", "Mao Direita + Mouse", "Teclas da direita a partir de H\nCOM CORES POR DEDO + Mouse", "#4ecdc4"),
        ]

        for key, titulo, desc, cor in layouts:
            btn_frame = tk.Frame(frame, bg="#1a1a1a")
            btn_frame.pack(pady=4)

            btn = tk.Button(btn_frame, text=titulo, font=("Segoe UI", 13, "bold"),
                           bg="#2a2a2a", fg="white", activebackground=cor,
                           activeforeground="white", bd=2, relief="solid",
                           cursor="hand2", width=30, height=2,
                           command=lambda k=key: self.selecionar(k))
            btn.pack()

            tk.Label(btn_frame, text=desc, font=("Segoe UI", 8),
                    bg="#1a1a1a", fg="#888888").pack(pady=(2, 0))

        # Legenda de cores
        legenda_frame = tk.Frame(self.root, bg="#1a1a1a")
        legenda_frame.pack(pady=(10, 5))
        tk.Label(legenda_frame, text="Legenda das Cores (Mao Direita):", font=("Segoe UI", 9, "bold"),
                bg="#1a1a1a", fg="white").pack()

        cores_txt = "Mindinho=Vermelho | Anelar=Turquesa | Medio=Amarelo | Indicador=Verde | Polegar=Azul"
        tk.Label(legenda_frame, text=cores_txt, font=("Segoe UI", 8),
                bg="#1a1a1a", fg="#aaaaaa").pack()

        # Rodape
        tk.Label(self.root, text="Depois de selecionar, arraste o overlay para posicionar\nPressione END para fechar",
                 font=("Segoe UI", 9), bg="#1a1a1a", fg="#666666").pack(side="bottom", pady=10)

    def selecionar(self, layout_key):
        self.root.destroy()
        app = KeystrokeOverlay(layout_key)
        app.executar()

    def executar(self):
        self.root.mainloop()


# =============================================================================
# OVERLAY PRINCIPAL
# =============================================================================
class KeystrokeOverlay:
    def __init__(self, layout_key):
        self.layout = LAYOUTS[layout_key]
        self.win_w, self.win_h = self.layout["win_size"]

        # JANELA
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.root.configure(bg="black")

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.win_x = (sw - self.win_w) // 2
        self.win_y = (sh - self.win_h) // 2
        self.root.geometry(f"{self.win_w}x{self.win_h}+{self.win_x}+{self.win_y}")

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0,
                                width=self.win_w, height=self.win_h)
        self.canvas.pack()

        self.root.update_idletasks()
        self.hwnd = self.root.winfo_id()

        # ESTADOS
        self.items = {}
        self.drag = None
        self.states = {}

        # DESENHAR
        self._desenhar()

        # BINDINGS
        self.canvas.bind("<Button-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)

        print(f"[Overlay] Layout: {self.layout['name']}")
        print("[Overlay] Pressione END para fechar.")

    def _desenhar(self):
        OUT = "#444444"
        R = 4

        for texto, vk_name, x, y, w, h, fonte, cor_dedo in self.layout["keys"]:
            pts = rounded_rect(x, y, w, h, R)
            cor_idle = CORES_DEDOS[cor_dedo]["idle"]
            rect = self.canvas.create_polygon(pts, fill=cor_idle, outline=OUT, width=1, smooth=True)
            txt = self.canvas.create_text(x, y, text=texto, font=fonte, fill="#111")
            self.items[vk_name] = {"rect": rect, "text": txt, "cor": cor_dedo}
            self.states[vk_name] = False

        # Mouse
        if self.layout.get("mouse"):
            mx, my, mw, mh = self.layout["mouse"]
            x1, y1 = mx - mw, my - mh // 2
            x2, y2 = mx + mw, my + mh // 2
            self.items["LMB"] = {
                "rect": self.canvas.create_oval(x1, y1, x2, y2, fill="#ffffff", outline=OUT, width=1),
                "left": self.canvas.create_rectangle(x1 + 2, y1 + 2, mx, y1 + 9, fill="#ffffff", outline=OUT, width=1),
                "right": self.canvas.create_rectangle(mx, y1 + 2, x2 - 2, y1 + 9, fill="#ffffff", outline=OUT, width=1),
                "cor": "padrao",
            }
            self.states["LMB"] = False
            self.states["RMB"] = False

    def _on_press(self, e):
        self.drag = {"mx": e.x_root, "my": e.y_root, "wx": self.win_x, "wy": self.win_y}

    def _on_drag(self, e):
        if self.drag is None:
            return
        self.win_x = self.drag["wx"] + e.x_root - self.drag["mx"]
        self.win_y = self.drag["wy"] + e.y_root - self.drag["my"]
        self.root.geometry(f"{self.win_w}x{self.win_h}+{self.win_x}+{self.win_y}")

    def _on_release(self, e):
        self.drag = None

    def _atualizar(self):
        # Forca no topo (Roblox-proof)
        SetWindowPos(self.hwnd, HWND_TOPMOST, 0, 0, 0, 0,
                     SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE | SWP_SHOWWINDOW)

        # Fechar
        if user32.GetAsyncKeyState(VK_END_CLOSE) & 0x8000:
            self.root.destroy()
            return

        # Atualiza estados
        for vk_name in list(self.states.keys()):
            if vk_name in VK_CODES:
                on = (user32.GetAsyncKeyState(VK_CODES[vk_name]) & 0x8000) != 0
                self.states[vk_name] = on

                if vk_name == "LMB":
                    cor = CORES_DEDOS["padrao"]["active"] if on else CORES_DEDOS["padrao"]["idle"]
                    self.canvas.itemconfig(self.items["LMB"]["left"], fill=cor)
                elif vk_name == "RMB":
                    cor = CORES_DEDOS["padrao"]["active"] if on else CORES_DEDOS["padrao"]["idle"]
                    self.canvas.itemconfig(self.items["LMB"]["right"], fill=cor)
                elif vk_name in self.items:
                    cor_dedo = self.items[vk_name]["cor"]
                    cor = CORES_DEDOS[cor_dedo]["active"] if on else CORES_DEDOS[cor_dedo]["idle"]
                    self.canvas.itemconfig(self.items[vk_name]["rect"], fill=cor)

        self.root.after(16, self._atualizar)

    def executar(self):
        self._atualizar()
        self.root.mainloop()


# =============================================================================
# ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    menu = MenuSelecao()
    menu.executar()