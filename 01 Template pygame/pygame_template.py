#########################################################################
# PROG2 Starter-Template: Game Loop & Update Pattern
#
# SEMESTERPLAN FÜR DIESES REPO:
# ============================================================
# Wochen 1-6:  Bauen Sie Ihr Spiel auf diesem Template auf.
#              Der Code darf "hässlich" sein – Hauptsache,
#              er funktioniert.
#
# Wochen 6-10: Refactoring! Strukturieren Sie den Code um:
#              - Klassen in eigene Dateien auslagern (src/)
#              - Vererbungshierarchien einführen
#              - SOLID-Prinzipien anwenden
#              - Design Patterns einbauen
#              WICHTIG: Dieses Refactoring muss in der
#              Git-History sichtbar sein!
#
# Woche 11-12:   Finalisieren, README aktualisieren, UML pflegen.
# ============================================================
#
# GenAI-Hinweis: GenAI-generierter Code muss in der
# Commit-Message gekennzeichnet werden:
# [GenAI: Tool, "Prompt-Zusammenfassung"]
#########################################################################

#########################################################################
# Import:     Alle Abhängigkeiten werden am Anfang eingebunden
#########################################################################

import pygame
import random
import os

#########################################################################
# Settings:   Hier stehen alle Konstanten Variablen für das Spiel.
#             Diese könnten auch ausgelagert werden in settings.py
#             und per import eingebunden werden
#########################################################################

WIDTH = 400
HEIGHT = 300
FPS = 60

#########################################################################
# Initialisierung:    pygame wird gestartet
#                     und eine Bildschirm-Ausgabe wird generiert
#########################################################################

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My Game")

#########################################################################
# Das Clock-Objekt:    Damit lassen sich Frames und Zeiten messen
#                      Sehr wichtig für Animationen etc.
#########################################################################

clock = pygame.time.Clock()

#########################################################################
# Das screen-Objekt:    Auf dem screen werden alle Grafiken gerendert
# Cooles Feature: pygame.SCALED(verdoppelte Auflösung für einen Retro-Effekt)
#########################################################################

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

#########################################################################
# Grafiken:    Das Einbinden von Grafiken kann auch ausgelagert werden
#########################################################################

game_folder = os.path.dirname(__file__)

#########################################################################
# Flyweight-Pattern: Gemeinsame Images werden nur einmal geladen
#########################################################################

sprite_images = {}
sprite_images["ball"] = pygame.image.load(
    os.path.join(game_folder, "_images/ball.png")
).convert_alpha()

#########################################################################
# Spielobjekte: Diese Klasse z. B. in src/ auslagern und von einer
#               Basisklasse (z.B. GameObject oder Sprite) erben lassen
#########################################################################

class Ball:
    """Ein einfacher Ball Sprite mit Wandkollision."""
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = sprite_images["ball"]
        self.imageRect = self.image.get_rect()

    def update(self):
        # Bewegung
        self.x += self.sx
        self.y += self.sy

        # Image Position setzen
        self.imageRect.topleft = (self.x,self.y)
        
        # Wandkollision: Richtung umkehren wenn Bildrand
        # den Screenrand erreicht
        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.sx *= -1

        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.sy *= -1

    def draw(self, surface):
        surface.blit(self.image, self.imageRect)


#########################################################################
# Sprite Factory: Erstelle mehr als ein Objekt mittels Klasse Ball()
#########################################################################

sprites = []
for _ in range(10):
    sprites.append(Ball(
        random.randint(64, WIDTH - 64),
        random.randint(64, HEIGHT - 64),
        random.choice([-3, -2, -1, 1, 2, 3]),
        random.choice([-3, -2, -1, 1, 2, 3]),
    ))

#########################################################################
# Game Loop:  Hier ist das Herzstück des Templates
# Im Game Loop laufen immer 5 Phasen ab:
# 1. Wait: Die Zeit zwischen 2 Frames wird mit Wartezeit gefüllt
# 2. Input: Alle (Input-)Events werden verarbeitet (Maus, Tastatur, etc.)
# 3. Update: Alle Sprites werden aktualisert inkl. Spiellogik
# 4. Render: Alle Sprites werden auf den Bildschirm gezeichnet
# 5. Double Buffering: Der Screen wird geswitcht und angezeigt
#########################################################################

running = True

while running:

    #########################################################################
    # 1. Wait-Phase:
    # Die pygame-interne Funktion clock.tick(FPS) berechnet die
    # tatsächliche Zeit zwischen zwei Frames und limitiert diese
    # auf einen Wert(z. B. 1/60). Diese tatsächliche verbrauchte
    # Zeit wird dann bei der Aktualisierung des Spiels benötigt,
    # um dieGeschwindigkeit der Objekte anzupassen.

    dt = clock.tick(FPS) / 1000

    #########################################################################
    # 2. Input-Phase:
    # Mit pygame.event.get() leeren wir den Event-Speicher.
    # Das ist wichtig, sonst läuft dieser voll und das Spiel stürzt ab.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #########################################################################
    # 3. Update-Phase: Hier ist die komplette Game Logik untergebracht.

    for sprite in sprites:
        sprite.update()

    #########################################################################
    # 4. Render-Phase: Zeichne alle Objekte auf den Bildschirm

    # Hintergrund
    screen.fill((255, 255, 255))    # RGB weiß

    # Zeichne Objekte an Position auf den Screen
    for sprite in sprites:
        sprite.draw(screen)

    #########################################################################
    # 5. Double Buffering mittels flip()

    pygame.display.flip()

###########################
# Spiel verlassen mit quit

pygame.quit()