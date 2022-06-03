from vector import Vector2 as v2
import math as m
import pygame

WIDTH, HEIGHT = 1600, 900
BG_COL = (20,20,20)
OBJ_COL = (0,0,0)
P_COL = (255,255,255)
CIRCLE_COL = (30,30,30)
RAY_COL = (75,75,75)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray Marcher 2D")

class Circle:
    def __init__(self, centre: v2, radius: int):
        self.centre = centre
        self.radius = radius

    def render(self):
        pygame.draw.circle(display, OBJ_COL, self.centre.get_tuple(), self.radius)

    def signed_dist(self, p: v2):
        return (p - self.centre).length() - self.radius

class Box:
    def __init__(self, centre: v2, size: v2):
        self.centre = centre
        self.size = size

    def render(self):
        pygame.draw.rect(display, OBJ_COL, ((self.centre-self.size).x, (self.centre-self.size).y, self.size.x, self.size.y))

    def signed_dist(self, p: v2):
        offset = (p-(self.centre-self.size/2)).abs() - self.size/2

        unsigned_dst = offset.max(v2(0,0)).length()
        dst_inside_box = min(0.0, max(offset.x, offset.y))
        return unsigned_dst + dst_inside_box


def march_all(p, dir, scene):
    circles = []
    while True:
        smallest_dist = WIDTH
        for obj in scene:
            smallest_dist = min(smallest_dist, obj.signed_dist(p))
        if not 2 < smallest_dist < max(WIDTH, HEIGHT): break
        circles.append(Circle(p, smallest_dist))
        p = p + dir * smallest_dist
    return circles


def render_window(scene, p, march_circles):
    display.fill(BG_COL)
    for obj in scene: obj.render()
    for circle in march_circles:
        pygame.draw.circle(display, CIRCLE_COL, circle.centre.get_tuple(), circle.radius)
    for circle in march_circles:
        pygame.draw.circle(display, RAY_COL, circle.centre.get_tuple(), 5)
        pygame.draw.circle(display, RAY_COL, circle.centre.get_tuple(), circle.radius, width=1)
    pygame.draw.line(display, P_COL, p.get_tuple(), (march_circles[-1].centre - (p-march_circles[-1].centre).normalized() * march_circles[-1].radius).get_tuple(), 3)
    pygame.draw.circle(display, P_COL, p.get_tuple(), 10)


def main():
    p = v2(200,200)
    ray_angle = m.pi / 2
    ray_dir = v2(0,1).normalized()
    scene = [Circle(v2(300,100), 50), Circle(v2(400,600), 120), Circle(v2(1000,600), 150),
             Box(v2(700,400), v2(150,150)), Box(v2(1300,250), v2(100,200))]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: p -= v2(0,1)
        elif keys[pygame.K_DOWN]: p += v2(0,1)
        elif keys[pygame.K_LEFT]: p -= v2(1,0)
        elif keys[pygame.K_RIGHT]: p += v2(1,0)
        elif keys[pygame.K_SPACE]:
            ray_angle -= m.pi/20000
            ray_dir = v2(m.cos(ray_angle), m.sin(ray_angle)).normalized()

        march_circles = march_all(p, ray_dir, scene)
        render_window(scene, p, march_circles)
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()