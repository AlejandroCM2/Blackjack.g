# Juego de Blackjack

## Descripción
El Blackjack es un juego de cartas de casino ampliamente conocido en el que los jugadores compiten contra la casa para alcanzar o acercarse a un valor de mano de 21 sin pasarse. El proyecto de Blackjack implementa una versión simplificada de este juego en Python.

## Funcionalidades
El juego de Blackjack implementa las siguientes funcionalidades clave:

- Registro de Jugadores: Permite registrar jugadores con nombres únicos.
- Iniciar Juego: Los jugadores pueden iniciar un juego al realizar una apuesta.
- Pedir Cartas: Los jugadores pueden pedir cartas para mejorar su mano.
- Plantarse: Los jugadores pueden decidir plantarse y finalizar su turno.
- Jugada de la Casa: La casa realiza su jugada siguiendo reglas predefinidas.
- Determinar Ganador: Se determina al ganador según las reglas del Blackjack.
- Mostrar Información del Jugador: Los jugadores pueden ver su información, como fichas disponibles.

## Estructura del Código
El proyecto se estructura en las siguientes clases principales:

- `Carta`: Representa una carta con pinta y valor.
- `Baraja`: Gestiona una baraja de cartas, permitiendo revolverla y repartir cartas.
- `Mano`: Representa la mano de un jugador o de la casa.
- `Jugador`: Representa a un jugador con un nombre, mano y fichas.
- `Casa`: Representa a la casa con su mano.
- `Blackjack`: Controla el flujo del juego y contiene los métodos principales.
