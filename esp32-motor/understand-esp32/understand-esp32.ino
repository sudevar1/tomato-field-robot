#define LED_PİN 2
void setup() {
  pinMode(LED_PİN,OUTPUT);
  Serial.begin(115200); //esp32 ile pc arasında seri haberleşme
  Serial.println("esp32 baslatildi");
  

}

void loop() {
 digitalWrite(LED_PİN,HIGH);
 Serial.println("LED ON");
 delay(1000);

 digitalWrite(LED_PİN,LOW);
 Serial.println("LED OFF");
 delay(1000);
}
