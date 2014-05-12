void setup() {
for(int i=12;i<4;--i)
{
  pinMode(i,LOW);
}
Serial.begin(1000000);
}

void loop() {
  Serial.print(!(bool)(PIND & (1 << 5)));
  Serial.print(!(bool)(PIND & (1 << 6)));
  Serial.print(!(bool)(PIND & (1 << 7)));
  Serial.print(!(bool)(PINB & (1 << 0)));
  Serial.print(!(bool)(PINB & (1 << 1)));
  Serial.print(!(bool)(PINB & (1 << 2)));
  Serial.print(!(bool)(PINB & (1 << 3)));
  Serial.print(!(bool)(PINB & (1 << 4)));
  Serial.print('\n'); 
}
