# WowThatsFishy - World of Warcraft Fishing Bot

Um projeto de automação de pesca para World of Warcraft usando visão computacional e detecção de imagem em tempo real.

## Visão Geral

Este é o início de um bot de pesca automatizado para World of Warcraft que utiliza técnicas de visão computacional para detectar elementos do jogo e automatizar o processo de pesca.

## Status do Projeto

🚧 **Em Desenvolvimento** - Atualmente implementando a captura de tela base

## Funcionalidades Atuais

- **Captura de tela em tempo real**: Captura continuamente toda a tela
- **Exibição ao vivo**: Mostra a tela capturada em uma janela OpenCV
- **Monitoramento de FPS**: Exibe frames por segundo no console
- **Saída fácil**: Pressione 'q' para sair da aplicação

## Funcionalidades Planejadas

- 🎣 **Detecção de bobber de pesca**: Identificar a boia de pesca na tela
- 🌊 **Detecção de movimento da água**: Detectar quando um peixe morde a isca
- 🖱️ **Automação de cliques**: Clicar automaticamente quando detectar uma fisgada
- 🎯 **Detecção de interface do WoW**: Reconhecer elementos específicos da UI do jogo
- ⚙️ **Configurações personalizáveis**: Ajustes de sensibilidade e regiões de detecção

## Requisitos

- Python 3.x
- PIL (Pillow) - para captura de tela
- OpenCV (cv2) - para processamento de imagem e detecção
- NumPy - para operações com arrays
- World of Warcraft instalado e rodando

## Como Funciona (Versão Atual)

A aplicação utiliza:
- `ImageGrab.grab()` da PIL para capturar screenshots
- `cv2` (OpenCV) para exibir as imagens e lidar com entrada do usuário
- `numpy` para operações com arrays e conversão entre formatos PIL e OpenCV
- Conversão de espaço de cor de RGB para BGR (necessário pelo OpenCV)

## Aviso Legal

Este projeto é para fins educacionais e de aprendizado em visão computacional. O uso de bots em jogos online pode violar os termos de serviço do jogo. Use por sua própria conta e risco.

## License

This project is open source and available under the [MIT License](LICENSE).
