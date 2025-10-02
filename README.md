# Snake Game 🐍

A classic Snake game implementation built with Python and Pygame. Navigate the snake around the screen, eat food to grow longer, and try to beat your high score without crashing into walls or yourself!

## Features

- 🎮 **Fullscreen gameplay** - Immersive gaming experience
- 📊 **Score tracking** - Keep track of your progress
- 🎯 **Grid-based movement** - Classic snake mechanics
- 🔄 **Instant restart** - Quick game over recovery
- 🎨 **Clean visual design** - Grid overlay and clear graphics
- ⚡ **Smooth controls** - Responsive arrow key input

## Requirements

- Python 3.x
- Pygame library

## Installation

### 1. Clone this repository:
```bash
git clone https://github.com/kjellevers/snake-game.git
cd snake-game
```

### 2. Install Pygame:
```bash
pip install pygame
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## How to Play

### Starting the Game
Run the game with:
```bash
python snake_game.py
```

The game will launch in fullscreen mode automatically.

### Controls
| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move snake up |
| ↓ (Down Arrow) | Move snake down |
| ← (Left Arrow) | Move snake left |
| → (Right Arrow) | Move snake right |
| ESC | Exit game |
| Any Key | Restart after game over |

### Game Rules
1. **Objective**: Eat the red food blocks to grow your snake and increase your score
2. **Movement**: The snake moves continuously in the current direction
3. **Growing**: Each food item eaten makes the snake grow by one segment
4. **Game Over**: The game ends if you:
   - Hit the screen boundaries (walls)
   - Collide with your own body
5. **Scoring**: Each food item is worth 1 point

### Tips
- Plan your moves ahead - the snake keeps moving!
- Be careful near walls and your own tail
- The snake cannot reverse direction (e.g., if moving right, you can't immediately go left)

## Game Settings

You can modify these constants in `snake_game.py` to customize your experience:

- **`GRID_SIZE`** (line 8): Size of each grid cell (default: 20 pixels)
- **`clock.tick(10)`** (line 145): Game speed in FPS (default: 10, higher = faster)
- **Colors** (lines 18-21): RGB values for game colors

## Technical Details

- Built with Python and Pygame
- Uses grid-based collision detection
- Implements fullscreen rendering with dynamic resolution
- Frame-rate controlled gameplay for consistent speed

## Project Structure

```
snake-game/
├── snake_game.py      # Main game file
├── README.md          # This file
├── requirements.txt   # Python dependencies
└── .gitignore        # Git ignore rules
```

## Future Enhancements

Potential features to add:
- [ ] High score persistence (save best score)
- [ ] Difficulty levels (adjustable speed)
- [ ] Sound effects and background music
- [ ] Pause functionality
- [ ] Obstacles and power-ups
- [ ] Different game modes

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is licensed under the MIT License - feel free to use and modify as you wish.

## Acknowledgments

- Inspired by the classic Nokia Snake game
- Built as a learning project to understand game development with Pygame
- Built with the assistance of Claude using the Sonnet 4.5 model

## Author

**Kjell Evers** - [kjellevers](https://github.com/kjellevers)

---

*Enjoy the game! If you encounter any bugs or have suggestions, feel free to open an issue.*
