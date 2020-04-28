# Followed Engineer Man Youtube Video (Creating a Snake game with Python in under 5 minutes)

import random 
import curses

'''Import the libraries used.
	
	[random library]- used to generate pseudo-random numbers
	
	[curses library]- library mostly used in the Unix environment. This library provides a terminal-independent screen-painting and keyboard-handling
					  facitlity for text-based terminals. It supports operations such as moving the cursor, scrolling the screen, and erasing areas.
'''

s = curses.initscr() #Initializes curses. Returns a window object representing the entire screen.
curses.curs_set(0) #Sets cursor state to (invisible)
sh, sw = s.getmaxyx() #sh= height of window sw= width of window (.getmaxyx() returns a Tuple)
w = curses.newwin(sh,sw, 0, 0) #Reutrns a new window 
w.keypad(1) #Keyboard ineput will be interpreted by curses.
w.timeout(100) 

snk_x = sw/4  #Define snake starting X 
snk_y = sh/2 #Define snake starting Y


'''
	Define the snake. [Tail][Body][Head]
'''
snake = [
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
]

food = [sh/2, sw/2] #Define first food in the middle of the screen.
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) #Places food on the screen. (PI symbol is used)

key = curses.KEY_RIGHT	 #Initialize the key constant (right-arrow).


#Game Logic
while True:
	next_key = w.getch()  #Get's the character from keyboard.
	key = key if next_key == -1 else next_key


	
	#Establishing the boundaries. Quit if snake reaches out of bounds.
	if snake[0][0] in [9, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	#New head defined
	new_head = [snake[0][0], snake[0][1]]


	#Depending on key press, head of snake will update.
	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	#Adds the new head to the snake.
	snake.insert(0, new_head)

	if snake[0] == food: #If the snake's head finds food.
		food = None #Food is eaten.
		while food is None: #Construct new food position if there is no more food nearby.
			nf = [
				random.randint(1, sh-1),
				random.randint(1, sw-1)
			]
			food = nf if nf not in snake else None #If new food placement is not already in the snake, place new food. Otherwise, find another food position.
		w.addch(food[0], food[1], curses.ACS_PI) #Adds the food to the screen.
	else:
		tail = snake.pop() #Remove snake's tail if not food.
		w.addch(int(tail[0]), int(tail[1]), ' ') #Adds tail to screen.

	w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD) #Adds snake head to screen.