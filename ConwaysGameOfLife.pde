// rest in peace mr conway, ur contributions wont be forgotten

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Random;
import java.util.stream.IntStream; 
import java.lang.Math;

int myscreen = 600;
int width = 30;
int length = 30;
int boxLength = myscreen/width;
int[][] arr = new int[width][length];
int[][] newArr = new int[width][length];


void setup(){
    size(600, 600);
    for (int i = 0; i < width; i++) {
      for (int j = 0; j < length; j++) {
        newArr[i][j]=arr[i][j];

      } 
    }
    System.out.println(arr);

}

void draw(){
  for (int i = 0; i < width; i++) {
      for (int j = 0; j < length; j++) {
        if (arr[i][j] == 0){
          fill(255, 255, 255);
          square(boxLength * i, boxLength * j, boxLength);
        }
        if (arr[i][j] == 1){
          fill(0, 0, 0);
          square(boxLength * i, boxLength * j, boxLength);
        }
      }
    }
  if (keyPressed){
    if (key == 'b'){
      loop();
    }
  }
}

void mouseClicked(){
  int x = (int)Math.floor(mouseX/boxLength);
  int y = (int)Math.floor(mouseY/boxLength);

  if (arr[x][y] == 1){
    arr[x][y] = 0;
    return;
  }

  if (arr[x][y] == 0){
    arr[x][y] = 1;
    return;
  }
}

void loop() {
  for (int i = 0; i < width; i++) {
      for (int j = 0; j < length; j++) {
        newArr[i][j]=arr[i][j];
      } 
    }

  for (int i = 0; i < length; i++) {
      for (int j = 0; j < width; j++) {
          int alive = countNeighbors(arr, i, j);

          if ((alive == 3 && arr[i][j] == 0) || ((alive == 2 || alive == 3) && arr[i][j] == 1)){
            newArr[i][j] = 1;
          } else{
            newArr[i][j] = 0;
          }
      }
  }

  for (int i = 0; i < width; i++) {
      for (int j = 0; j < length; j++) {
        arr[i][j]=newArr[i][j];
      } 
    }
}


int countNeighbors(int[][] board, int i, int j) {
    int n = 0;
    for (int k = -1; k <= 1; k++) {
        for (int l = -1; l <= 1; l++) {
            if (i+k < width && i+k >= 0 && j+l >= 0 && j+l < width && board[i+k][j+l] == 1) n++;
        }
    }
    // to avoid counting itself as alive
    if (board[i][j] == 1) n--;

    return n;
}
