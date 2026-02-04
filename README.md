📖 Description
Memory Match is a classic concentration game where players flip cards to find matching pairs. The game features 16 cards arranged in a 4×4 grid with 8 unique symbol pairs to match. Test your memory and try to complete the game in as few moves as possible!
Each card displays beautifully hand-drawn symbols including an Apple, Orange, Lemon, Grape cluster, Star, Heart, Diamond, and Moon crescent. The game tracks your moves and time, giving you a star rating based on your performance.
✨ Features

Clean, Modern UI - Dark theme with smooth animations and polished visual effects
Custom-Drawn Symbols - 8 unique symbols rendered purely with Pygame (no emoji dependencies)
Smooth Animations - Card flip animations, staggered reveal on game start, hover effects, and particle bursts
Game States - Main menu, gameplay screen, and victory screen with statistics
Performance Tracking - Move counter, elapsed time tracker, and star-based rating system
Visual Feedback - Green flash for matches, red flash for mismatches
Responsive Controls - Hover effects on cards and buttons with scaling animations

🎯 Gameplay

Click PLAY from the main menu to start a new game
Cards appear face-down in a 4×4 grid
Click any card to flip it and reveal the symbol
Click a second card to find its match
If the symbols match, both cards stay revealed (green flash)
If they don't match, both cards flip back over (red flash)
Continue until all 8 pairs are matched
Win screen shows your final stats and rating:

***** Perfect! - 20 moves or fewer
**** Great! - 21-30 moves
*** Nice! - 31+ moves



🎮 Controls
Menu

Left Click - Select menu options (PLAY / QUIT)

Gameplay

Left Click - Flip a card
X Button (top-right) or ESC - Return to main menu

Win Screen

PLAY AGAIN - Start a new game
MENU - Return to main menu
ESC - Return to main menu

🛠️ Installation
Requirements

Python 3.7 or higher
Pygame library

Setup

Clone or download this repository

bash   git clone <your-repo-url>
   cd memory-match

Install Pygame

bash   pip install pygame

Run the game

bash   python memory_match.py

🎨 Symbol Gallery
The game features 8 custom-drawn symbols:

🍎 Apple - Red circle with green leaf
🍊 Orange - Orange circle with segment lines
🍋 Lemon - Yellow oval with pointed tips
🍇 Grape - Purple cluster of circles
⭐ Star - 5-pointed gold star
❤️ Heart - Classic red heart shape
💎 Diamond - Blue faceted gem
🌙 Moon - Yellow crescent moon

📊 Game Stats

Grid Size: 4 × 4 (16 cards)
Pairs to Match: 8
Difficulty: Easy to Medium
Average Completion: 25-35 moves
Perfect Score: 20 moves or fewer

🎯 Tips for Better Scores

Focus on positions - Try to remember where each symbol is located
Create patterns - Look for visual patterns in the grid layout
Start systematically - Flip cards in a methodical pattern (e.g., row by row)
Use the reveal animation - The staggered card reveal gives you a brief glimpse of positions
Minimize random clicks - Each click counts toward your move total

🔧 Technical Details

Resolution: 720 × 800 pixels
FPS: 60
Animation System: Smooth interpolation with easing functions
Rendering: Pure Pygame drawing primitives (no external image assets)
State Management: Clean state machine (menu → playing → win)