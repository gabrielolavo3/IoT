// C++ code
// Gabriel Olavo

int buzzer = 3;

void setup() {
	pinMode(buzzer, OUTPUT);
}

void loop() {
  digitalWrite(buzzer, HIGH);
  delay(500);
  digitalWrite(buzzer, LOW);
  delay(500);
}