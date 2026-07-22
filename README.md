🎮 Keystroke Overlay
Overlay de Teclas em Tempo Real para Windows — Visualize cada pressionamento de tecla e clique do mouse diretamente na tela, com estilo profissional e baixo consumo de recursos.
📋 Índice
Sobre o Projeto
Funcionalidades
Requisitos do Sistema
Instalação
Como Usar
Layouts Disponíveis
Como Funciona
Controles e Atalhos
Tabela de Teclas Suportadas
Roadmap
Licença
Contato e Comunidade
🧠 Sobre o Projeto
O Keystroke Overlay é uma aplicação desktop desenvolvida em Python 3 com Tkinter, projetada para criar um overlay transparente e sempre no topo da tela que exibe em tempo real quais teclas do teclado e botões do mouse estão sendo pressionados.
💡 Ideal para:
🎮 Gamers que querem mostrar suas jogadas em streams (Twitch, YouTube, Kick)
🎹 Músicos que usam teclado MIDI ou controles virtuais
🖥️ Criadores de conteúdo que gravam tutoriais de software
🧑‍🏫 Educadores que ensinam atalhos de teclado
🏆 Jogadores competitivos que analisam suas mecânicas
🛠️ Informações do Desenvolvimento
Planilhas
Campo	Detalhe
Desenvolvedor	Desenvolvedor Pleno
Tempo de Desenvolvimento	3 semanas de trabalho intensivo
Linguagem	Python 3
Bibliotecas Principais	Tkinter, ctypes, math
Plataforma	Windows (Win32 API)
Versão Atual	1.0.0
Licença	MIT (Open Source)
Repositório	GitHub - Keystroke Overlay
✨ Funcionalidades
🎯 Principais Recursos
Planilhas
Recurso	Descrição	Status
🖱️ Detecção de Mouse	Botão Esquerdo (LMB) e Direito (RMB) em tempo real	✅ Implementado
⌨️ Detecção de Teclado	Suporte a letras, números, funções (F1-F12) e especiais	✅ Implementado
🎨 6 Layouts Diferentes	WASD, Teclado Completo, Numpad, Parte Direita, Mão Esquerda, Mão Direita	✅ Implementado
🌈 Cores por Dedo	Layout "Mão Direita" com cores identificando cada dedo	✅ Implementado
🖐️ Drag & Drop	Mova o overlay para qualquer posição da tela com o mouse	✅ Implementado
🔝 Always on Top	Sempre visível, mesmo em jogos em tela cheia (Roblox-proof)	✅ Implementado
🪟 Janela Sem Bordas	Overlay limpo e profissional, sem barra de título	✅ Implementado
🎭 Transparência	Fundo transparente, apenas as teclas aparecem	✅ Implementado
⚡ Baixa Latência	Atualização a cada ~16ms (60 FPS)	✅ Implementado
🔴 Feedback Visual	Teclas mudam de cor ao serem pressionadas	✅ Implementado
💻 Requisitos do Sistema
Planilhas
Requisito	Mínimo	Recomendado
Sistema Operacional	Windows 7/8/10/11	Windows 10/11
Python	3.7+	3.11+
Memória RAM	50 MB livres	100 MB livres
CPU	Qualquer processador moderno	Dual Core 2.0 GHz+
GPU	Integrada	Dedicada (para streaming)
Permissões	Usuário padrão	Administrador (opcional)
📦 Instalação
Método 1: Clonando o Repositório (Recomendado)
bash
# Clone o repositório
git clone https://github.com/nicezinks/keystroke-overlay.git

# Entre na pasta
cd keystroke-overlay

# Execute o projeto
python main.py
Método 2: Download Direto
Baixe o arquivo overdey.py do repositório
Salve em uma pasta de sua preferência
Execute com: python overdey.py
Método 3: Executável (Em Breve)
🚧 Estamos trabalhando em um executável .exe standalone para facilitar a distribuição. Fique atento às releases!
🚀 Como Usar
Passo a Passo
Execute o programa
bash
python overdey.py
Escolha seu Layout na tela de seleção:
Planilhas
Layout	Descrição	Ideal Para
WASD + Mouse	W, A, S, D, Espaço + Mouse	Jogos FPS (CS:GO, Valorant, Fortnite)
Teclado Completo	QWERTY completo + F1-F12 + Setas	Tutoriais, programação, geral
Numpad + Setas	Teclado numérico + Setas + Mouse	Jogos de estratégia, Excel
Parte Direita	Setas + Insert/Home/PgUp + Numpad	Navegação, edição de texto
Mão Esquerda	Teclas da esquerda até G (branco)	Jogos com mão esquerda
Mão Direita	Teclas da direita a partir de H (cores por dedo)	Aprendizado de digitação
Posicione o overlay arrastando-o com o mouse para o local desejado
Use normalmente — o overlay detectará automaticamente suas teclas e cliques!
Para fechar, pressione a tecla END (ou clique no X do menu de seleção)
🎨 Layouts Disponíveis
Layout 1: WASD + Mouse 🎯
plain
    ┌───┐
    │ W │
┌───┼───┼───┬──────────┐
│ A │ S │ D │  [MOUSE] │
└───┴───┴───┴──────────┘
    │ ESPAÇO │
    └────────┘
Tamanho da janela: 220 x 120 px
Teclas: W, A, S, D, Espaço, LMB, RMB
Público-alvo: Jogadores de FPS e jogos de ação
Layout 2: Teclado Completo ⌨️
plain
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ F1 │ F2 │ F3 │ F4 │ F5 │ F6 │ F7 │ F8 │ F9 │F10 │F11 │F12 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ S │ D │ F │ G │ H │ J │ K │ L │
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
┌───┬───┬───┬───┬───┬───┬───┐
│ Z │ X │ C │ V │ B │ N │ M │
└───┴───┴───┴───┴───┴───┴───┘
Tamanho da janela: 580 x 220 px
Teclas: QWERTY completo, números, F1-F12, Setas, Shift, Ctrl, Enter, Tab, Caps, Alt, Backspace
Público-alvo: Tutoriais gerais, demonstrações de software
Layout 3: Numpad + Setas + Mouse 🔢
plain
┌───┬───┬───┬────┐
│ 7 │ 8 │ 9 │ /  │
├───┼───┼───┼────┤
│ 4 │ 5 │ 6 │ *  │
├───┼───┼───┼────┤
│ 1 │ 2 │ 3 │ -  │
├───┴───┼───┼────┤
│   0   │ . │ +  │
└───────┴───┴────┘
    ┌───┐
    │ ↑ │
┌───┼───┼───┬──────────┐
│ ← │ ↓ │ → │  [MOUSE] │
└───┴───┴───┴──────────┘
Tamanho da janela: 280 x 200 px
Teclas: Numpad 0-9, operadores, Setas direcionais, Mouse
Público-alvo: Jogos de estratégia, planilhas, navegação
Layout 4: Parte Direita + Mouse ➡️
plain
┌────┬────┬────┐
│INS │HOME│PGUP│
├────┼────┼────┤
│DEL │END │PGDN│
└────┴────┴────┘
    ┌───┐
    │ ↑ │
┌───┼───┼───┐
│ ← │ ↓ │ → │
└───┴───┴───┘
┌───┬───┬───┐
│ 7 │ 8 │ 9 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 1 │ 2 │ 3 │
├───┴───┼───┤
│   0   │ . │
└───────┴───┘
Tamanho da janela: 320 x 180 px
Teclas: Setas, Insert, Home, PgUp, PgDn, Numpad, Enter, Shift, Ctrl, Alt, Mouse
Público-alvo: Edição de texto, navegação avançada
Layout 5: Mão Esquerda + Mouse (Branco) ✋⬜
plain
┌────┬───┬───┬───┬───┬───┐
│ '  │ 1 │ 2 │ 3 │ 4 │ 5 │
├────┼───┼───┼───┼───┼───┤
│TAB │ Q │ W │ E │ R │ T │
├────┼───┼───┼───┼───┼───┤
│CAPS│ A │ S │ D │ F │ G │
├────┼───┼───┼───┼───┼───┤
│SHFT│ Z │ X │ C │ V │ B │
├────┼───┴───┴───┴───┴───┤
│CTRL│      ESPAÇO        │
└────┴────────────────────┘
Tamanho da janela: 420 x 210 px
Teclas: Todas as teclas da mão esquerda até a coluna G, todas em branco
Público-alvo: Jogos que usam apenas a mão esquerda
Layout 6: Mão Direita + Mouse (Cores por Dedo) 🎨
plain
┌───┬───┬───┬───┬───┬───┬────┐
│ 6 │ 7 │ 8 │ 9 │ 0 │ - │ =  │  🟢 Indicador
├───┼───┼───┼───┼───┼───┼────┤  🟡 Médio
│ Y │ U │ I │ O │ P │ ´ │ [  │  🔵 Anelar
├───┼───┼───┼───┼───┼───┼────┤  🔴 Mindinho
│ H │ J │ K │ L │ Ç │ ~ │ ]  │  ⚪ Polegar
├───┼───┼───┼───┼───┼───┼────┤
│ N │ M │ , │ . │ ; │ / │    │
├───┴───┴───┴───┴───┴───┤ENT │
│        ESPAÇO          │    │
└────────────────────────┴────┘
Tamanho da janela: 520 x 230 px
Teclas: Todas as teclas da mão direita a partir de H, com cores por dedo
Público-alvo: Aprendizado de digitação, análise de mecânica de dedos
🌈 Legenda de Cores (Mão Direita)
Planilhas
Dedo	Cor Idle	Cor Ativa	Teclas Associadas
Mindinho Direito	Vermelho Claro (#ff9999)	Vermelho Intenso (#ff3333)	0, -, =, P, ´, [, Ç, ~, ], ;, /, Backspace, Enter, RShift
Anelar Direito	Turquesa (#99e6e6)	Vermelho Intenso (#ff3333)	9, O, L, .
Médio Direito	Amarelo (#fff099)	Vermelho Intenso (#ff3333)	8, I, K, ,
Indicador Direito	Verde (#99ffcc)	Vermelho Intenso (#ff3333)	6, 7, Y, U, H, J, N, M
Polegar Direito	Azul (#a8d8ea)	Vermelho Intenso (#ff3333)	Espaço
⚙️ Como Funciona
Arquitetura do Sistema
plain
┌─────────────────────────────────────────┐
│           MENU DE SELEÇÃO               │
│  (Tkinter - Janela com bordas normais)  │
│         Escolha um dos 6 layouts        │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│         KEYSTROKE OVERLAY               │
│  (Janela sem bordas, transparente,     │
│   always-on-top, drag & drop)           │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  LOOP PRINCIPAL (60 FPS)        │    │
│  │  ├── Win32 API: GetAsyncKeyState│    │
│  │  ├── Verifica VK_CODES          │    │
│  │  ├── Atualiza Canvas (Tkinter)  │    │
│  │  └── Verifica tecla END         │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
Fluxo de Dados
Planilhas
Etapa	Tecnologia	Descrição
1. Captura	user32.GetAsyncKeyState()	API Win32 que consulta o estado de cada tecla virtual
2. Mapeamento	Dicionário VK_CODES	Converte nomes de teclas para códigos virtuais do Windows
3. Renderização	Tkinter Canvas	Desenha retângulos arredondados e texto para cada tecla
4. Atualização	root.after(16, ...)	Loop de ~60 FPS para feedback em tempo real
5. Posicionamento	SetWindowPos (Win32)	Garante que o overlay fique sempre no topo
Detecção de Teclas
O projeto utiliza a função nativa do Windows GetAsyncKeyState para detectar pressionamentos de tecla em nível de sistema, o que significa que funciona em qualquer aplicação, incluindo jogos em tela cheia como Roblox, Fortnite, Valorant, CS:GO, entre outros.
Python
# Exemplo de detecção
if user32.GetAsyncKeyState(VK_CODES["W"]) & 0x8000:
    # A tecla W está pressionada!
    canvas.itemconfig(rect_w, fill="#ff3333")  # Vermelho ativo
else:
    canvas.itemconfig(rect_w, fill="#ffffff")  # Branco idle
🎮 Controles e Atalhos
Dentro do Overlay
Planilhas
Ação	Controle	Descrição
Mover Overlay	🖱️ Clique e Arraste	Segure o botão esquerdo do mouse em qualquer lugar do overlay e arraste
Fechar Overlay	⌨️ Tecla END	Pressione a tecla END no teclado para fechar imediatamente
Minimizar	❌ Não disponível	Use a tecla END para fechar e reabra pelo menu
No Menu de Seleção
Planilhas
Ação	Controle	Descrição
Selecionar Layout	🖱️ Clique no botão	Escolha um dos 6 layouts disponíveis
Fechar Menu	❌ X da janela	Fecha o programa completamente
📊 Tabela de Teclas Suportadas
Teclas Alfanuméricas
Planilhas
Categoria	Teclas
Letras	A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
Números (Top Row)	1, 2, 3, 4, 5, 6, 7, 8, 9, 0
Números (Numpad)	NUM0, NUM1, NUM2, NUM3, NUM4, NUM5, NUM6, NUM7, NUM8, NUM9
Teclas de Função
Planilhas
Categoria	Teclas
F1-F12	F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12
Teclas de Navegação
Planilhas
Categoria	Teclas
Setas	UP (↑), DOWN (↓), LEFT (←), RIGHT (→)
Navegação Extendida	INS, HOME, PGUP, PGDN, DEL, END
Teclas de Modificação
Planilhas
Categoria	Teclas
Shift	SHIFT (esquerdo), RSHIFT (direito)
Ctrl	CTRL (esquerdo), RCTRL (direito)
Outros	ALT, TAB, BACK (Backspace), CAPS, ENTER, SPACE
Mouse
Planilhas
Botão	Código	Descrição
LMB	0x01	Botão Esquerdo do Mouse
RMB	0x02	Botão Direito do Mouse
Teclas Especiais (OEM)
Planilhas
Tecla	Código	Caractere
OEM1	0xBA	Ç (Portuguese ABNT)
OEM2	0xBF	; /
OEM3	0xC0	' / ~
OEM4	0xDB	- / _
OEM5	0xDC	[ / {
OEM6	0xDD	] / }
OEM7	0xDE	´ / `
OEM102	0xE2	, / <
🗺️ Roadmap
Planilhas
Versão	Recurso	Status
v1.0.0	Lançamento inicial com 6 layouts	✅ Concluído
v1.1.0	Suporte a rolagem do mouse (scroll)	🚧 Em planejamento
v1.2.0	Customização de cores e tamanhos	🚧 Em planejamento
v1.3.0	Salvamento de posição e preferências	🚧 Em planejamento
v1.4.0	Suporte a múltiplos monitores	🚧 Em planejamento
v2.0.0	Versão executável (.exe) standalone	🚧 Em desenvolvimento
📜 Licença
Este projeto está licenciado sob a Licença MIT.
plain
MIT License

Copyright (c) 2026 Keystroke Overlay

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
🤝 Contato e Comunidade
📧 Contato
Planilhas
Canal	Link
GitHub	github.com/seu-usuario/keystroke-overlay
Issues	Reportar Bug
Discussions	Discussões
⭐ Como Contribuir
⭐ Dê uma estrela no repositório se gostou do projeto!
🐛 Reporte bugs abrindo uma Issue no GitHub
💡 Sugira recursos nas Discussões
🔀 Faça um Fork e envie um Pull Request com melhorias
📢 Compartilhe com amigos gamers e streamers!
🎯 Apresentação do Projeto
🎬 Em Resumo
O Keystroke Overlay nasceu da necessidade de ter uma ferramenta leve, profissional e open source para exibir pressionamentos de tecla em tempo real durante streams, tutoriais e jogos.
Desenvolvido por um Desenvolvedor Pleno ao longo de 3 semanas de trabalho intensivo, este projeto combina:
💻 Python puro com Tkinter (sem dependências externas pesadas)
⚡ Win32 API para detecção de baixo nível
🎨 Design minimalista com transparência e always-on-top
🎮 Foco em gamers com layouts específicos para diferentes gêneros de jogos
🌈 Análise ergonômica com cores por dedo para treinamento de digitação
🏆 Destaques
✅ 100% Open Source — Código completo disponível no GitHub
✅ Zero dependências externas — Apenas Python padrão + Tkinter
✅ Roblox-proof — Funciona em jogos em tela cheia graças à API Win32
✅ 6 layouts especializados — Do básico (WASD) ao avançado (cores por dedo)
✅ Drag & Drop intuitivo — Posicione onde quiser com um clique
✅ Fácil de fechar — Apenas pressione a tecla END
🔗 Acesse o Projeto no GitHub
🚀 O código-fonte completo está disponível gratuitamente no GitHub!
👉 Clique aqui para acessar o repositório
⭐ Não esqueça de dar uma estrela no projeto!

Feito com ❤️ e muito ☕ por um Desenvolvedor Pleno
3 semanas de dedicação para a comunidade gamer e de criação de conteúdo
⭐ Star no GitHub · 🐛 Reportar Bug · 💡 Sugerir Feature
