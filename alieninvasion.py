import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 500))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #отряд пришельцев
        self.aliendar = pygame.sprite.Group() #группа пришельцев
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_limit:
            #создает новый сняряд и добавляет в группу снарядов
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):  # cоздает экземпляр пришельца и добавляет его в группу
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space = self.settings.screen_width - (2 * alien_width)
        alien_number_x = available_space // (2 * alien_width)

        #определить количество рядом которые помещаются в экран
        ship_height = self.ship.rect.height #высота коробля
        available_space_y = self.settings.screen_height - ((3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 *alien_height)

        for row_number in range(number_rows):
            for alien_number in range(alien_number_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliendar.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #выводит экран
        self.ship.blitme() #выводит корабль на экран

        #отрисовывает каждый снаряд в группу снарядов
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliendar.draw(self.screen) #отрисовывает пришельцев

        pygame.display.flip() #отображает последний отрисованный экран, постоянно

    def _update_bullets(self):
        self.bullets.update()
        # повторить для чего делается копия
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliendar, True, True)

    def _update_aliens(self):
        #проверка достижения флотом края экрана и изменение его расположения
        self._check_fleet_edges()
        self.aliendar.update()

    def _check_fleet_edges(self):
        # проверяет если флот достиг края и реагирует на это
        for alien in self.aliendar.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #опускает весь флот и меняет направление
        for alien in self.aliendar.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


