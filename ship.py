import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self):
        self.rect = None

    def update(self):
        pass

    def blitme(self):
        pass


def __init__(self, ai_game):
    """Инициализирует корабль и задает его начальную позицию"""
    self.screen = ai_game.screen
    self.setting = ai_game.setting
    self.screen_rect = ai_game.screen.get_rect()
    # Загружаем изображение корабля и получаем прямоуголник.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    # Каждый новый корабль появляется у нижнего края окна.
    self.rect.midbottom = self.screen_rect.midbottom
    # Сохранение вещественной координаты центра корабля.
    self.x = float(self.rect.x)
    # Флаг перемещения.
    self.moving_right = False
    self.moving_left = False


def update(self):
    """Обновляет позицию корабля с флагом."""
    # Обновляет атрибут Х объекта ship, не rect.
    if self.moving_right:
        self.rect.x += 1
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.setting.ship_speed
    if self.moving_left:
        self.rect.x -= 1
    if self.moving_left and self.rect.left > 0:
        self.x -= self.setting.ship_speed
    # Обновление атрибута rec на основаниее self.x.
    self.rect.x = self.x


def blitme(self):
    """Рисует корабль в текущей позиции."""
    self.screen.blit(self.image, self.rect)
