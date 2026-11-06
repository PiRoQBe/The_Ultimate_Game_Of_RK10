from __future__ import annotations

from typing import Any, final, override

import pygame


@final
class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        bullet_groups: pygame.sprite.Group[Any],
        *groups: pygame.sprite.Group[Any],
    ) -> None:
        super().__init__(*groups)

        self.image: pygame.Surface = pygame.image.load("img/Player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect: pygame.FRect = self.image.get_frect(bottomleft=(50, 550))

        self.speed = 75

        self.bullet_groups: pygame.sprite.Group[Any] = bullet_groups

    @override
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        move = pygame.Vector2((keys[pygame.K_d] - keys[pygame.K_a]), 0)
        if move.length() > 0:
            self.rect.center += move.normalize() * self.speed * dt

    def shoot(self) -> Bullet:
        return Bullet(self.get_plater_pos(), self.bullet_groups)

    def get_plater_pos(self) -> pygame.Vector2:
        return pygame.Vector2(self.rect.center)


@final
class Bullet(pygame.sprite.Sprite):
    def __init__(
        self, start_pos: pygame.Vector2, *groups: pygame.sprite.Group[Any]
    ) -> None:
        super().__init__(*groups)

        self.image: pygame.Surface = pygame.image.load("img/Bullet.png").convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(midbottom=start_pos)

        self.speed = 200

    @override
    def update(self, dt: float) -> None:
        move = pygame.Vector2(0, -1)
        self.rect.center += move.normalize() * self.speed * dt
