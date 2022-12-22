// this code runs on the arduino
void setup() {
	Serial.begin(9600); // use the same baud-rate as the python side
  pinMode(3, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
}

int lastButtonState[9] = {0,0,0,0,0,0,0,0,0};


void loop() {
  for (int index = 3; index < 12; index++) // reading the input of the buttons
  {
    int currentButtonState = digitalRead(index);
    if (currentButtonState != lastButtonState[index - 3])
    {
      lastButtonState[index - 3] = currentButtonState;
      
    }
  }

  // sending the inputs to the computer

  Serial.print(lastButtonState[0]);
  Serial.print(lastButtonState[1]);
  Serial.print(lastButtonState[2]);
  Serial.print(lastButtonState[3]);
  Serial.print(lastButtonState[4]);
  Serial.print(lastButtonState[5]);
  Serial.print(lastButtonState[6]);
  Serial.print(lastButtonState[7]);
  Serial.println(lastButtonState[8]);
  delay(35);
}


