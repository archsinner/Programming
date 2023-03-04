int throttlePin = 8;
int elevationPin = 13;
int gearPin = 7;
int ailePin = 2;
int ruddPin = 10;
int throttleVal = 0;
int elevationVal = 0;
int gearVal = 0;
int aileVal = 0;
int ruddVal = 0;
void setup()
{
 pinMode(throttlePin, INPUT);
 pinMode(elevationPin, INPUT);
 pinMode(gearPin, INPUT);
 pinMode(ailePin, INPUT);
 pinMode(ruddPin, INPUT);
 Serial.begin(115200);
}
void loop()
{
 throttleVal = pulseIn(throttlePin, HIGH);
 elevationVal = pulseIn(elevationPin, HIGH);
 gearVal = pulseIn(gearPin, HIGH);
 aileVal = pulseIn(ailePin, HIGH);
 ruddVal = pulseIn(ruddPin, HIGH);
 
 Serial.println(throttleVal);
 Serial.println(elevationVal);
 Serial.println(gearVal);
 Serial.println(aileVal);
 Serial.println(ruddVal);
 Serial.println()
 // ? delay ?
 //delay(DELAY_DURATION);
}
