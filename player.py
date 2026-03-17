import pygame
from circleshape import CircleShape
from constants import * #PLAYER_RADIUS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # 2. Create the 'image' attribute (the visual)
        # For a simple placeholder, we create a transparent surface
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)

        # 3. Create the 'rect' attribute (the collision/position box)
        self.rect = self.image.get_rect(center=(x, y))

        self.shot_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        self.unit_vector = pygame.Vector2(0, 1)
        self.rotated_vector = self.unit_vector.rotate(self.rotation)
        self.rotated_with_speed_vector = self.rotated_vector * PLAYER_SPEED * dt
        self.position += self.rotated_with_speed_vector

    def shoot(self):
        self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = velocity * PLAYER_SHOOT_SPEED


    def update(self, dt):
        #keys = pygame.key.get_pressed()

        if self.shot_timer > 0:
            self.shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            # ?
        if keys[pygame.K_d]:
            self.rotate(dt)
            # ?
        if keys[pygame.K_s]:
            self.move(-dt)
            # ?
        if keys[pygame.K_w]:
            self.move(dt)
            # ?
        # if keys[pygame.K_SPACE]:
        #     self.shoot()


        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()


