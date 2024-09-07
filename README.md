# Asteroids Game

A classic arcade-style space shooter game built with Pygame.

## Why This Project?

1. **Learning**: This project serves as an excellent way to practice object-oriented programming and game development concepts.

2. **Nostalgia**: Asteroids is a timeless game that many people remember fondly, making it a great choice for recreation.

3. **Simplicity with Depth**: The game mechanics are straightforward, but there's room for complexity in physics simulations and gameplay features.

## How It Works

### Core Components

1. **CircleShape**: A base class for circular objects in the game.
   - Why? It provides a reusable foundation for both asteroids and potentially the player's ship.

2. **Asteroid**: Inherits from CircleShape, representing the main obstacles in the game.
   - Why? Inheritance allows for easy creation of multiple asteroid types with shared behaviors.

3. **Constants**: A separate file for game constants.
   - Why? Centralizing constants makes tweaking game parameters easier and keeps the code organized.

### Game Loop

1. The game continuously updates object positions and checks for collisions.
2. Asteroids move across the screen based on their velocity.
3. When hit, asteroids split into smaller pieces, increasing difficulty.

### Physics Simulation

- Simple vector-based movement is used for asteroid trajectories.
- Rotation is applied when asteroids split, creating more dynamic movement.

## How to Play

(Add instructions on how to run the game and basic controls here)

## Future Enhancements

1. Add a player-controlled spaceship
2. Implement shooting mechanics
3. Create a scoring system
4. Add sound effects and background music

## Contributing

Feel free to fork this project and submit pull requests with improvements or new features!
