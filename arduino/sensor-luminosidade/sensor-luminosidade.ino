// C++ code
// Gabriel Olavo

int led = 3,
	portaSensor = A0,
	valorSensor = 0;

void setup()
{
	pinMode(led, OUTPUT);
  	Serial.begin(9600);
}

void loop()
{
  valorSensor = analogRead(portaSensor);
  Serial.println(valorSensor);
  delay(100);
  
  if (valorSensor < 900) 
  {
    digitalWrite(led, HIGH);
  } 
  else 
  {
    digitalWrite(led, LOW);
  }
}