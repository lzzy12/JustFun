import pygame, random, time

screen_height = 500
screen_width = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Race by lzzy12 @ github.com")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
darkGreen = (100, 255, 80)
clock = pygame.time.Clock()

def display_msg(text, color, x, y, fontSize):
	font = pygame.font.Font('freesansbold.ttf', fontSize)
	displayText = font.render(text, True, color)
	screen.blit(displayText, (x, y))

def game_loop():
	score = 0
	carImg = pygame.image.load('car.png')
	done = False
	x_car = (screen_width * 0.3)
	x_car_speed = 80
	y_car = screen_height - 427
	car_width = 340
	object_y = -300
	object_width = 80
	object_height = 80
	object_speed = 3
	object_x = random.randrange(0, screen_width)
	zCross_x = 380
	zCross_y = -100
	zCross_speed = 30
	left = 0
	color = black
	text = ""
	speed_incremented = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and x_car > 1:
					x_car -= x_car_speed

				if event.key == pygame.K_RIGHT and x_car < screen_width - car_width:
					x_car += x_car_speed
		if object_y > screen_height + 5:
			object_y = 0
			object_x = random.randrange(0, screen_width)
		if zCross_y > screen_height:
			zCross_y = -20

		screen.fill(black)
		pygame.draw.rect(screen, darkGreen, (0, 0, 250, screen_height))

		if object_y > y_car  and object_x > x_car and object_x < x_car + car_width:
			score += 1
			color = red
			object_y = -80
			object_x = random.randrange(0, screen_width)
		elif object_y > screen_height:
			left += 1
			color = black
			print(left)

		text = "Score: " + str(score) 
		display_msg(text, color, 0, 0, 30)
		if score != 0 and not speed_incremented:
			if score % 5 == 0:
				object_speed += 1
				speed_incremented = True
				print("First: " + str(speed_incremented))
		elif score != 0:
			if score % 5 == 0:
				 speed_incremented = False
				 print("2nd: " +  str(speed_incremented))

		object_y += object_speed
		zCross_y += zCross_speed
		pygame.draw.rect(screen, darkGreen, ((screen_width - 190), 0, 190, screen_height))
		pygame.draw.rect(screen, white, (zCross_x, zCross_y, 70, 100))
		pygame.draw.rect(screen, red, (object_x, object_y, object_width, object_height))
		screen.blit(carImg, (x_car, y_car))
		if left > 2:
			text = "GAME OVER!!"
			display_msg(text, red, 50, 20, 80)
			time.sleep(10)
			game_loop()

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()

