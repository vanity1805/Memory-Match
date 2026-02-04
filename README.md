# 🎮 Memory Match

A polished memory card matching game built with Python and Pygame featuring smooth animations, custom-drawn symbols, and an elegant dark UI.

## 📖 Description

Memory Match is a classic concentration game where players flip cards to find matching pairs. The game features 16 cards arranged in a 4×4 grid with 8 unique symbol pairs to match. Test your memory and try to complete the game in as few moves as possible!

Each card displays beautifully hand-drawn symbols including an Apple, Orange, Lemon, Grape cluster, Star, Heart, Diamond, and Moon crescent. The game tracks your moves and time, giving you a star rating based on your performance.

## ✨ Features

- **Clean, Modern UI** - Dark theme with smooth animations and polished visual effects
- **Custom-Drawn Symbols** - 8 unique symbols rendered purely with Pygame (no emoji dependencies)
- **Smooth Animations** - Card flip animations, staggered reveal on game start, hover effects, and particle bursts
- **Game States** - Main menu, gameplay screen, and victory screen with statistics
- **Performance Tracking** - Move counter, elapsed time tracker, and star-based rating system
- **Visual Feedback** - Green flash for matches, red flash for mismatches
- **Responsive Controls** - Hover effects on cards and buttons with scaling animations

## 🎯 Gameplay

1. Click **PLAY** from the main menu to start a new game
2. Cards appear face-down in a 4×4 grid
3. Click any card to flip it and reveal the symbol
4. Click a second card to find its match
5. If the symbols match, both cards stay revealed (green flash)
6. If they don't match, both cards flip back over (red flash)
7. Continue until all 8 pairs are matched
8. Win screen shows your final stats and rating:
   - ***** Perfect! - 20 moves or fewer
   - **** Great! - 21-30 moves
   - *** Nice! - 31+ moves

## 🎮 Controls

### Menu
- **Left Click** - Select menu options (PLAY / QUIT)

### Gameplay
- **Left Click** - Flip a card
- **X Button** (top-right) or **ESC** - Return to main menu

### Win Screen
- **PLAY AGAIN** - Start a new game
- **MENU** - Return to main menu
- **ESC** - Return to main menu

## 🛠️ Installation

### Requirements
- Python 3.7 or higher
- Pygame library

### Setup

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd memory-match
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python memory_match.py
   ```

## 🎨 Symbol Gallery

The game features 8 custom-drawn symbols:

- 🍎 **Apple** - Red circle with green leaf
- 🍊 **Orange** - Orange circle with segment lines
- 🍋 **Lemon** - Yellow oval with pointed tips
- 🍇 **Grape** - Purple cluster of circles
- ⭐ **Star** - 5-pointed gold star
- ❤️ **Heart** - Classic red heart shape
- 💎 **Diamond** - Blue faceted gem
- 🌙 **Moon** - Yellow crescent moon

## 📊 Game Stats

- **Grid Size:** 4 × 4 (16 cards)
- **Pairs to Match:** 8
- **Difficulty:** Easy to Medium
- **Average Completion:** 25-35 moves
- **Perfect Score:** 20 moves or fewer

## 🎯 Tips for Better Scores

1. **Focus on positions** - Try to remember where each symbol is located
2. **Create patterns** - Look for visual patterns in the grid layout
3. **Start systematically** - Flip cards in a methodical pattern (e.g., row by row)
4. **Use the reveal animation** - The staggered card reveal gives you a brief glimpse of positions
5. **Minimize random clicks** - Each click counts toward your move total

## 🔧 Technical Details

- **Resolution:** 720 × 800 pixels
- **FPS:** 60
- **Animation System:** Smooth interpolation with easing functions
- **Rendering:** Pure Pygame drawing primitives (no external image assets)
- **State Management:** Clean state machine (menu → playing → win)

## 📝 Code Structure

```
memory_match.py
├── Constants & Configuration
├── Helper Functions (lerp, easing, drawing utilities)
├── Button Class (interactive menu buttons)
├── Card Class (flip animation, hover effects, rendering)
├── Game Class (state management, screens, main loop)
│   ├── setup_menu()
│   ├── draw_menu()
│   ├── start_game()
│   ├── draw_hud()
│   ├── setup_win()
│   ├── draw_win()
│   └── run() - Main game loop
└── Entry Point
```

## 🎨 Customization

Want to modify the game? Here are some easy tweaks:

**Change grid size:**
```python
COLS, ROWS = 6, 6  # For a 6×6 grid (18 pairs)
```

**Adjust difficulty timing:**
```python
self.wait_timer = 1.5  # Longer wait before flipping back
```

**Modify colors:**
```python
BG_DARK = (18, 18, 28)  # Background color
ACCENT_GOLD = (255, 195, 80)  # Highlight color
```

**Add more symbols:**
Add new cases to the `draw_symbol()` function and extend the `SYMBOLS` list.

## 🐛 Troubleshooting

**Game window doesn't open:**
- Ensure Pygame is installed: `pip install pygame --upgrade`
- Check Python version: `python --version` (needs 3.7+)

**Symbols don't appear:**
- This version uses pure Pygame drawing, no fonts needed
- If you see blank cards, check console for errors

**Performance issues:**
- Lower FPS in the constants: `FPS = 30`
- Reduce particle count in win screen

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add difficulty levels (Easy: 3×4, Medium: 4×4, Hard: 6×6)
- Implement high score tracking
- Add sound effects
- Create themed symbol sets (animals, space, food, etc.)
- Add multiplayer mode
- Implement hint system

## 🙏 Credits

Built with Python and Pygame. All graphics rendered programmatically using Pygame's drawing primitives.

---

**Enjoy the game!** 🎉
