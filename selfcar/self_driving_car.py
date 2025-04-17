import pygame
import math
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Self-Driving Car Simulation")
WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
clock = pygame.time.Clock()
file_path="C:/Users/pavit/OneDrive/Documents/selfcar1/selfcar/car-removebg-preview.png"
car_img = pygame.image.load(file_path)
car_img = pygame.transform.scale(car_img, (100, 60))
car_x, car_y = 100, 500
car_angle =0
car_speed = 2
path = [(100, 500), (200, 400), (300, 300), (400, 200), (500, 300), (600, 400), (700, 500)]
def rotate_car(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=(car_x, car_y))
    return rotated_image, rect
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def main():
    global car_x, car_y, car_angle, car_speed
    target_idx = 0
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(path) - 1):
            pygame.draw.line(screen, BLACK, path[i], path[i + 1], 3)
        if target_idx < len(path):
            target_x, target_y = path[target_idx]
            angle_to_target = math.degrees(math.atan2(target_y - car_y, target_x - car_x))
            car_angle = angle_to_target
            car_x += car_speed * math.cos(math.radians(car_angle))
            car_y += car_speed * math.sin(math.radians(car_angle))
            if distance(car_x, car_y, target_x, target_y) < 10:
                target_idx += 1
        rotated_car, rotated_rect = rotate_car(car_img, -car_angle)
        screen.blit(rotated_car, rotated_rect.topleft)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()
