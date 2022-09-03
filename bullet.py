import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблём."""

    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.screen
        self.color = self.settings.bullet_color

        # Создание снарядов в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряла хранится в вес=щественном формате.
        self.y = float(self.rect.y)


def update(self):
    """Перемещение снаряда вверх по экрану."""

    # Обновление позциии снаряда в вещественном формате.
    self.y -= self.settings.bullet_speed
    # Обновление позции прямоугольника.
    self.rect.y = self.y


def draw_bullet(self):
    """Вывод снаряда на экран"""
    pygame.draw.rect(self.screen, self.color, self.rect)
