# Fruity-Snake
This is a Snake game ,made by using python with pygame library.


![image](https://user-images.githubusercontent.com/104193104/167265865-bf795739-7e49-4cc1-a9c9-4d8f13554c8f.png)

Step 1: Firstly we are importing the necessary libraries.
After that, we are defining the width and height of the window in which the game will be played.
And define the color in RGB format that we are going to use in our game for displaying text and background.


![image](https://user-images.githubusercontent.com/104193104/166729193-29738016-ff0a-4469-a146-d9154a01ef89.png)

Step 2:  Initialize Screen width and Height. Use pygame.display.set_mode to display game window.
Now Use pygame.image.load to load background image , welcome window image, game over image and fruits image.


![image](https://user-images.githubusercontent.com/104193104/167265900-eeaac9a0-07b4-4847-8cc9-cc412fc7852f.png)


Step 3: Set title for game using pygame.display.set_caption("Odyssey").Then use pygame.display.update(),It allows only a portion of the screen to updated, instead of the entire area.clock = pygame.time.Clock(),this function is used to create a clock object which can be used to keep track of time.Now create a Font object using font. Font() method of pygame.text_screen fuction is used to display text on gaming window.


![image](https://user-images.githubusercontent.com/104193104/185969721-97510b2a-9b06-4bbd-b853-b857ba61d6f4.png)

![image](https://user-images.githubusercontent.com/104193104/185970830-701ee5c3-7e78-4d97-9e76-a99663ca317c.png)


Step 4:Now we will create Welcome Screen.
