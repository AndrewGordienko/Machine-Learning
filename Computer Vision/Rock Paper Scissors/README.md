This was my first time building a classifier! It was really fun!

The end product is by using a training set found at http://www.laurencemoroney.com/rock-paper-scissors-dataset/, I created a program which will win at rock paper scissors almost every single time. It works by using opencv to grab a frame from your webcam, processing it with the DNN trained, and then outputing what it believes you are showing. From there, the program prints out whatever would make you lose in that case + a little bit of ui to make stuff pretty :)

All in all this was a really fun small project to do! It was my first time, and I learned a lot about building keras models and using tensorflow, to ultimately make an unwinnable game :)

RPS Full has the entire code all in one place if you're interested in running it only once.

RPS Model has the code for the model which then saves with the name lilo... after lilo and stitch

RPS Game has the game element of the code which imports the saved model, uses opencv to process the frame, and ultimately is responsible for the final UI
