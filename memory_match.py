import pygame
import random
import math
import sys
import time

# ─── INIT ────────────────────────────────────
pygame.init()

# ─── CONSTANTS ───────────────────────────────
WIDTH, HEIGHT = 720, 800
FPS = 60

# Colors
BG_DARK = (18, 18, 28)
CARD_BACK = (38, 40, 55)
CARD_BACK_BORDER = (60, 63, 85)
CARD_FACE = (255, 255, 255)
TEXT_WHITE = (240, 240, 245)
TEXT_DIM = (140, 142, 160)
ACCENT_GOLD = (255, 195, 80)
ACCENT_GOLD_DIM = (200, 155, 60)
MATCH_FLASH = (80, 220, 140)
MISMATCH_FLASH = (220, 80, 80)
MENU_CARD_COLOR = (45, 47, 65)
HIGHLIGHT = (100, 105, 140)

# Card layout
COLS, ROWS = 4, 4
TOTAL_CARDS = COLS * ROWS
CARD_W, CARD_H = 130, 155
PAD_X = (WIDTH - COLS * CARD_W) // (COLS + 1)
PAD_Y_START = 120
PAD_Y = (HEIGHT - PAD_Y_START - ROWS * CARD_H) // (ROWS + 1)

# Symbol IDs (pairs) — drawn as shapes, no emoji needed
SYMBOLS = [0, 1, 2, 3, 4, 5, 6, 7]
SYMBOL_NAMES = ["Apple", "Orange", "Lemon", "Grape", "Star", "Heart", "Diamond", "Moon"]

def draw_symbol(surface, symbol_id, cx, cy, size=38):
    """Draw each symbol as pure pygame shapes."""
    if symbol_id == 0:
        # 🍎 Apple — red circle + green leaf
        pygame.draw.circle(surface, (220, 50, 50), (cx, cy + 4), size)
        pygame.draw.circle(surface, (200, 40, 40), (cx - 8, cy - 2), size - 12)
        # leaf
        leaf_points = [(cx + 2, cy - size + 2), (cx + 16, cy - size - 8), (cx + 8, cy - size + 12)]
        pygame.draw.polygon(surface, (60, 180, 60), leaf_points)
        # stem
        pygame.draw.line(surface, (80, 50, 30), (cx + 2, cy - size + 2), (cx + 5, cy - size - 4), 3)

    elif symbol_id == 1:
        # 🍊 Orange — orange circle with segments
        pygame.draw.circle(surface, (255, 145, 30), (cx, cy), size)
        pygame.draw.circle(surface, (240, 130, 20), (cx, cy), size - 6)
        # segments
        for angle in [0, 60, 120, 180, 240, 300]:
            rad = math.radians(angle)
            ex = cx + int((size - 8) * math.cos(rad))
            ey = cy + int((size - 8) * math.sin(rad))
            pygame.draw.line(surface, (220, 110, 10), (cx, cy), (ex, ey), 2)
        pygame.draw.circle(surface, (240, 120, 15), (cx, cy), 5)

    elif symbol_id == 2:
        # 🍋 Lemon — yellow oval
        pygame.draw.ellipse(surface, (255, 230, 50), (cx - size, cy - size + 8, size * 2, (size - 8) * 2))
        pygame.draw.ellipse(surface, (240, 215, 40), (cx - size + 4, cy - size + 12, size * 2 - 8, (size - 8) * 2 - 8))
        # tips
        pygame.draw.ellipse(surface, (255, 230, 50), (cx - size - 6, cy - 5, 14, 10))
        pygame.draw.ellipse(surface, (255, 230, 50), (cx + size - 8, cy - 5, 14, 10))

    elif symbol_id == 3:
        # 🍇 Grape — cluster of purple circles
        positions = [(-12, -10), (12, -10), (0, -22), (-18, 6), (18, 6), (0, 8), (-6, 18), (6, 18)]
        for (ox, oy) in positions:
            pygame.draw.circle(surface, (100, 50, 160), (cx + ox, cy + oy), 13)
            pygame.draw.circle(surface, (130, 80, 200), (cx + ox - 3, cy + oy - 3), 6)
        # stem
        pygame.draw.line(surface, (80, 50, 30), (cx, cy - 28), (cx, cy - 36), 3)

    elif symbol_id == 4:
        # ⭐ Star — 5-pointed
        points = []
        for i in range(10):
            angle = math.radians(-90 + i * 36)
            r = size if i % 2 == 0 else size * 0.42
            points.append((cx + int(r * math.cos(angle)), cy + int(r * math.sin(angle))))
        pygame.draw.polygon(surface, (255, 200, 50), points)
        pygame.draw.polygon(surface, (255, 220, 100), points, 0)
        # inner highlight
        inner = []
        for i in range(10):
            angle = math.radians(-90 + i * 36)
            r = (size * 0.55) if i % 2 == 0 else size * 0.24
            inner.append((cx + int(r * math.cos(angle)), cy + int(r * math.sin(angle))))
        pygame.draw.polygon(surface, (255, 230, 130), inner)

    elif symbol_id == 5:
        # ❤️ Heart
        s = size - 4
        # Two circles on top
        pygame.draw.circle(surface, (220, 55, 75), (cx - s // 2, cy - s // 3), s // 2 + 2)
        pygame.draw.circle(surface, (220, 55, 75), (cx + s // 2, cy - s // 3), s // 2 + 2)
        # Bottom triangle
        points = [(cx - s, cy - s // 3), (cx + s, cy - s // 3), (cx, cy + s)]
        pygame.draw.polygon(surface, (220, 55, 75), points)
        # Highlight
        pygame.draw.circle(surface, (255, 100, 120), (cx - s // 2 - 2, cy - s // 3 - 4), s // 4)

    elif symbol_id == 6:
        # 💎 Diamond
        points = [(cx, cy - size), (cx + size - 4, cy - 4), (cx, cy + size - 2), (cx - size + 4, cy - 4)]
        pygame.draw.polygon(surface, (100, 190, 255), points)
        # facets
        pygame.draw.polygon(surface, (140, 210, 255), [(cx, cy - size), (cx + size - 4, cy - 4), (cx, cy - 4)])
        pygame.draw.polygon(surface, (70, 160, 230), [(cx, cy - 4), (cx + size - 4, cy - 4), (cx, cy + size - 2)])
        pygame.draw.polygon(surface, (50, 140, 210), [(cx, cy - 4), (cx - size + 4, cy - 4), (cx, cy + size - 2)])
        pygame.draw.polygon(surface, (160, 220, 255), [(cx, cy - size), (cx - size + 4, cy - 4), (cx, cy - 4)])

    elif symbol_id == 7:
        # 🌙 Moon crescent
        # Big circle (moon)
        pygame.draw.circle(surface, (255, 230, 120), (cx, cy), size)
        # Cutout circle offset to the right to create crescent
        pygame.draw.circle(surface, BG_DARK, (cx + 18, cy - 6), size - 4)
        # Highlight glow edge
        pygame.draw.circle(surface, (255, 245, 180), (cx - 6, cy + 4), size - 14)

# ─── FONTS ───────────────────────────────────
pygame.font.init()
FONT_TITLE = pygame.font.SysFont("arial", 52, bold=True)
FONT_SUBTITLE = pygame.font.SysFont("arial", 22)
FONT_BUTTON = pygame.font.SysFont("arial", 28, bold=True)
FONT_SCORE = pygame.font.SysFont("arial", 22, bold=True)
FONT_WIN_TITLE = pygame.font.SysFont("arial", 56, bold=True)
FONT_WIN_SUB = pygame.font.SysFont("arial", 26)
FONT_SMALL = pygame.font.SysFont("arial", 18)

# ─── HELPERS ─────────────────────────────────
def lerp(a, b, t):
    return a + (b - a) * t

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3

def ease_in_cubic(t):
    return t ** 3

def draw_rounded_rect(surface, color, rect, radius=12, border_color=None, border_width=2):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    if border_color:
        pygame.draw.rect(surface, border_color, rect, width=border_width, border_radius=radius)

def draw_text_centered(surface, text, font, color, cx, cy):
    surf = font.render(text, True, color)
    surface.blit(surf, (cx - surf.get_width() // 2, cy - surf.get_height() // 2))

def draw_text_left(surface, text, font, color, x, y):
    surf = font.render(text, True, color)
    surface.blit(surf, (x, y))

# ─── BUTTON CLASS ────────────────────────────
class Button:
    def __init__(self, cx, cy, w, h, label, color, hover_color, text_color=TEXT_WHITE):
        self.rect = pygame.Rect(cx - w // 2, cy - h // 2, w, h)
        self.label = label
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hovered = False
        self.scale = 1.0

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)
        target_scale = 1.04 if self.hovered else 1.0
        self.scale = lerp(self.scale, target_scale, 0.15)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

    def draw(self, surface):
        # Scale around center
        cx, cy = self.rect.centerx, self.rect.centery
        w = int(self.rect.width * self.scale)
        h = int(self.rect.height * self.scale)
        draw_rect = pygame.Rect(cx - w // 2, cy - h // 2, w, h)

        color = self.hover_color if self.hovered else self.color
        draw_rounded_rect(surface, color, draw_rect, radius=14)

        # Shadow
        shadow_rect = draw_rect.move(0, 3)
        shadow_rect.inflate_ip(-10, -6)
        # subtle inner shine on top
        shine_rect = pygame.Rect(draw_rect.x + 10, draw_rect.y + 4, draw_rect.width - 20, 6)
        pygame.draw.rect(surface, (255, 255, 255, 30), shine_rect, border_radius=3)

        draw_text_centered(surface, self.label, FONT_BUTTON, self.text_color, cx, cy)


# ─── CARD CLASS ──────────────────────────────
class Card:
    def __init__(self, index, symbol, col, row):
        self.index = index
        self.symbol = symbol
        self.col = col
        self.row = row
        self.x = PAD_X + col * (CARD_W + PAD_X)
        self.y = PAD_Y_START + row * (CARD_H + PAD_Y)
        self.rect = pygame.Rect(self.x, self.y, CARD_W, CARD_H)

        self.flipped = False       # target state
        self.matched = False
        self.flip_progress = 0.0   # 0 = back, 1 = face
        self.flip_speed = 0.08
        self.flash_timer = 0.0     # for match/mismatch flash
        self.flash_color = None
        self.hover = False
        self.scale = 1.0
        # Stagger reveal animation
        self.reveal_delay = index * 0.06
        self.reveal_progress = 0.0
        self.revealed = False

    def update(self, mouse_pos, dt):
        # Staggered reveal on game start
        if not self.revealed:
            self.reveal_delay -= dt
            if self.reveal_delay <= 0:
                self.revealed = True
                self.reveal_progress = 1.0

        # Flip animation
        target = 1.0 if self.flipped else 0.0
        if abs(self.flip_progress - target) > 0.01:
            if self.flip_progress < target:
                self.flip_progress = min(self.flip_progress + self.flip_speed, target)
            else:
                self.flip_progress = max(self.flip_progress - self.flip_speed, target)

        # Flash timer
        if self.flash_timer > 0:
            self.flash_timer -= dt

        # Hover
        if not self.matched and self.revealed:
            self.hover = self.rect.collidepoint(mouse_pos) and not self.flipped
        else:
            self.hover = False

        # Scale
        target_scale = 1.03 if self.hover else 1.0
        self.scale = lerp(self.scale, target_scale, 0.12)

    def draw(self, surface):
        if not self.revealed:
            return

        cx, cy = self.rect.centerx, self.rect.centery
        w = int(CARD_W * self.scale)
        h = int(CARD_H * self.scale)
        draw_rect = pygame.Rect(cx - w // 2, cy - h // 2, w, h)

        # Shadow
        shadow = draw_rect.move(0, 4)
        shadow_surf = pygame.Surface((shadow.width, shadow.height), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 60), (0, 0, shadow.width, shadow.height), border_radius=14)
        surface.blit(shadow_surf, shadow.topleft)

        # Determine color based on flip
        face_show = self.flip_progress > 0.5

        if not face_show:
            # BACK
            color = CARD_BACK
            border = CARD_BACK_BORDER
            if self.hover:
                color = (48, 50, 68)
                border = HIGHLIGHT
            draw_rounded_rect(surface, color, draw_rect, radius=14, border_color=border, border_width=2)
            # Pattern on back: small grid dots
            dot_color = (55, 58, 78)
            for r in range(3, 7):
                for c in range(2, 6):
                    dx = draw_rect.x + c * 22 - 10
                    dy = draw_rect.y + r * 22 - 10
                    pygame.draw.circle(surface, dot_color, (dx, dy), 3)
        else:
            # FACE
            color = (250, 250, 255)
            border = (200, 200, 215)

            # Flash overlay
            if self.flash_timer > 0:
                t = self.flash_timer / 0.35
                if self.flash_color == MATCH_FLASH:
                    color = tuple(int(lerp(color[i], MATCH_FLASH[i], t * 0.5)) for i in range(3))
                    border = MATCH_FLASH
                else:
                    color = tuple(int(lerp(color[i], MISMATCH_FLASH[i], t * 0.4)) for i in range(3))
                    border = MISMATCH_FLASH

            if self.matched:
                color = (230, 250, 235)
                border = MATCH_FLASH

            draw_rounded_rect(surface, color, draw_rect, radius=14, border_color=border, border_width=2)

            # Symbol (drawn as shapes)
            draw_symbol(surface, self.symbol, draw_rect.centerx, draw_rect.centery)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


# ─── GAME STATE ──────────────────────────────
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Memory Match")
        self.clock = pygame.time.Clock()
        self.state = "menu"  # menu | playing | win
        self.cards = []
        self.selected = []
        self.moves = 0
        self.matches = 0
        self.start_time = 0
        self.elapsed = 0
        self.waiting = False
        self.wait_timer = 0
        self.particles = []
        self.menu_buttons = []
        self.win_buttons = []
        self.setup_menu()

    # ── MENU ──────────────────────────────────
    def setup_menu(self):
        self.menu_buttons = [
            Button(WIDTH // 2, 380, 220, 60, "PLAY", (70, 130, 180), (90, 155, 210)),
            Button(WIDTH // 2, 455, 220, 60, "QUIT", (80, 75, 90), (100, 95, 110)),
        ]

    def draw_menu(self):
        self.screen.fill(BG_DARK)

        # Decorative floating cards in background
        for i in range(len(SYMBOLS)):
            t = time.time() * 0.6 + i * 0.8
            x = 60 + (i % 4) * 180 + math.sin(t) * 15
            y = 100 + (i // 4) * 100 + math.cos(t * 1.1) * 12
            rect = pygame.Rect(int(x) - 30, int(y) - 38, 60, 75)
            # Faint card
            card_surf = pygame.Surface((60, 75), pygame.SRCALPHA)
            pygame.draw.rect(card_surf, (45, 47, 65, 60), (0, 0, 60, 75), border_radius=10)
            pygame.draw.rect(card_surf, (65, 68, 90, 80), (0, 0, 60, 75), width=1, border_radius=10)
            self.screen.blit(card_surf, rect.topleft)
            draw_symbol(self.screen, SYMBOLS[i], rect.centerx, rect.centery, size=18)

        # Title
        draw_text_centered(self.screen, "Memory Match", FONT_TITLE, ACCENT_GOLD, WIDTH // 2, 260)
        draw_text_centered(self.screen, "Flip cards and find all matching pairs", FONT_SUBTITLE, TEXT_DIM, WIDTH // 2, 315)

        # Buttons
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.menu_buttons:
            btn.update(mouse_pos)
            btn.draw(self.screen)

        # Footer
        draw_text_centered(self.screen, "4 × 4 Grid  •  8 Pairs", FONT_SMALL, TEXT_DIM, WIDTH // 2, 540)

    # ── GAME SETUP ────────────────────────────
    def start_game(self):
        self.state = "playing"
        self.moves = 0
        self.matches = 0
        self.selected = []
        self.waiting = False
        self.wait_timer = 0
        self.start_time = time.time()
        self.elapsed = 0
        self.particles = []

        # Create pairs and shuffle
        symbols = SYMBOLS * 2
        random.shuffle(symbols)

        self.cards = []
        for i in range(TOTAL_CARDS):
            col = i % COLS
            row = i // COLS
            self.cards.append(Card(i, symbols[i], col, row))

    # ── PLAYING HUD ───────────────────────────
    def draw_hud(self):
        # Top bar bg
        hud_surf = pygame.Surface((WIDTH, 75), pygame.SRCALPHA)
        pygame.draw.rect(hud_surf, (25, 26, 40, 200), (0, 0, WIDTH, 75))
        self.screen.blit(hud_surf, (0, 0))

        # Moves
        draw_text_left(self.screen, "Moves", FONT_SMALL, TEXT_DIM, 30, 18)
        draw_text_left(self.screen, str(self.moves), FONT_SCORE, TEXT_WHITE, 30, 38)

        # Time
        draw_text_centered(self.screen, f"{int(self.elapsed // 60)}:{int(self.elapsed % 60):02d}", FONT_SCORE, ACCENT_GOLD, WIDTH // 2, 42)
        draw_text_centered(self.screen, "Time", FONT_SMALL, TEXT_DIM, WIDTH // 2, 22)

        # Matches
        draw_text_left(self.screen, "Matches", FONT_SMALL, TEXT_DIM, WIDTH - 130, 18)
        draw_text_left(self.screen, f"{self.matches}/8", FONT_SCORE, TEXT_WHITE, WIDTH - 130, 38)

        # Back button
        back_rect = pygame.Rect(WIDTH - 60, 12, 40, 28)
        mouse_pos = pygame.mouse.get_pos()
        col = (70, 75, 95) if back_rect.collidepoint(mouse_pos) else (50, 52, 68)
        draw_rounded_rect(self.screen, col, back_rect, radius=6)
        draw_text_centered(self.screen, "X", FONT_SMALL, TEXT_DIM, back_rect.centerx, back_rect.centery)

    # ── WIN SCREEN ────────────────────────────
    def setup_win(self):
        self.state = "win"
        self.win_buttons = [
            Button(WIDTH // 2, 470, 220, 55, "PLAY AGAIN", (70, 130, 180), (90, 155, 210)),
            Button(WIDTH // 2, 540, 220, 55, "MENU", (80, 75, 90), (100, 95, 110)),
        ]
        # Burst particles
        for _ in range(40):
            self.particles.append({
                "x": WIDTH // 2, "y": HEIGHT // 2,
                "vx": random.uniform(-8, 8),
                "vy": random.uniform(-8, 8),
                "life": random.uniform(0.6, 1.2),
                "color": random.choice([ACCENT_GOLD, MATCH_FLASH, (180, 160, 255), (255, 150, 200)]),
                "size": random.randint(4, 9),
            })

    def draw_win(self, dt):
        self.screen.fill(BG_DARK)

        # Update & draw particles
        alive = []
        for p in self.particles:
            p["life"] -= dt
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.15  # gravity
            if p["life"] > 0:
                alpha = max(0, min(255, int(p["life"] * 255)))
                s = pygame.Surface((p["size"]*2, p["size"]*2), pygame.SRCALPHA)
                pygame.draw.circle(s, (*p["color"], alpha), (p["size"], p["size"]), p["size"])
                self.screen.blit(s, (int(p["x"]) - p["size"], int(p["y"]) - p["size"]))
                alive.append(p)
        self.particles = alive

        # Card silhouettes floating in background
        for i in range(len(SYMBOLS)):
            t = time.time() * 0.5 + i
            x = 60 + (i % 4) * 180 + math.sin(t) * 12
            y = 80 + (i // 4) * 90 + math.cos(t * 1.2) * 10
            rect = pygame.Rect(int(x) - 30, int(y) - 38, 60, 75)
            card_surf = pygame.Surface((60, 75), pygame.SRCALPHA)
            pygame.draw.rect(card_surf, (45, 47, 65, 40), (0, 0, 60, 75), border_radius=10)
            self.screen.blit(card_surf, rect.topleft)
            draw_symbol(self.screen, SYMBOLS[i], rect.centerx, rect.centery, size=16)

        # Title
        draw_text_centered(self.screen, "You Win!", FONT_WIN_TITLE, ACCENT_GOLD, WIDTH // 2, 300)

        # Stats
        mins = int(self.elapsed // 60)
        secs = int(self.elapsed % 60)
        time_str = f"{mins}m {secs}s" if mins > 0 else f"{secs}s"
        draw_text_centered(self.screen, f"Completed in {self.moves} moves  •  {time_str}", FONT_WIN_SUB, TEXT_DIM, WIDTH // 2, 365)

        # Rating
        if self.moves <= 20:
            rating, rcolor = "*** Perfect!", ACCENT_GOLD
        elif self.moves <= 30:
            rating, rcolor = "** Great!", (180, 200, 255)
        else:
            rating, rcolor = "* Nice!", (180, 180, 180)
        draw_text_centered(self.screen, rating, FONT_SUBTITLE, rcolor, WIDTH // 2, 405)

        # Buttons
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.win_buttons:
            btn.update(mouse_pos)
            btn.draw(self.screen)

    # ── MAIN LOOP ─────────────────────────────
    def run(self):
        running = True
        prev_time = time.time()

        while running:
            now = time.time()
            dt = now - prev_time
            prev_time = now

            mouse_pos = pygame.mouse.get_pos()

            # ── EVENTS ──
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.state == "playing":
                        self.state = "menu"
                    elif self.state == "win":
                        self.state = "menu"

                # Menu clicks
                if self.state == "menu":
                    if self.menu_buttons[0].is_clicked(event):
                        self.start_game()
                    if self.menu_buttons[1].is_clicked(event):
                        running = False

                # Win clicks
                if self.state == "win":
                    if self.win_buttons[0].is_clicked(event):
                        self.start_game()
                    if self.win_buttons[1].is_clicked(event):
                        self.state = "menu"

                # Playing clicks
                if self.state == "playing" and not self.waiting:
                    # Back button
                    back_rect = pygame.Rect(WIDTH - 60, 12, 40, 28)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_rect.collidepoint(event.pos):
                        self.state = "menu"
                        continue

                    for card in self.cards:
                        if card.is_clicked(event):
                            if card.flipped or card.matched:
                                continue
                            if len(self.selected) >= 2:
                                continue

                            card.flipped = True
                            self.selected.append(card)

                            if len(self.selected) == 2:
                                self.moves += 1
                                self.waiting = True
                                self.wait_timer = 0.7

            # ── UPDATE ──
            if self.state == "playing":
                self.elapsed = time.time() - self.start_time

                for card in self.cards:
                    card.update(mouse_pos, dt)

                if self.waiting:
                    self.wait_timer -= dt
                    if self.wait_timer <= 0:
                        self.waiting = False
                        c1, c2 = self.selected
                        if c1.symbol == c2.symbol:
                            c1.matched = True
                            c2.matched = True
                            c1.flash_timer = 0.35
                            c2.flash_timer = 0.35
                            c1.flash_color = MATCH_FLASH
                            c2.flash_color = MATCH_FLASH
                            self.matches += 1
                            if self.matches == len(SYMBOLS):
                                self.setup_win()
                        else:
                            c1.flash_timer = 0.35
                            c2.flash_timer = 0.35
                            c1.flash_color = MISMATCH_FLASH
                            c2.flash_color = MISMATCH_FLASH
                            c1.flipped = False
                            c2.flipped = False
                        self.selected = []

            # ── DRAW ──
            if self.state == "menu":
                self.draw_menu()

            elif self.state == "playing":
                self.screen.fill(BG_DARK)
                self.draw_hud()
                for card in self.cards:
                    card.draw(self.screen)

            elif self.state == "win":
                self.draw_win(dt)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# ─── ENTRY ───────────────────────────────────
if __name__ == "__main__":
    game = Game()
    game.run()