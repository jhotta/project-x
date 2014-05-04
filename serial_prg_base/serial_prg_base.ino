
// serial_voltage_2byte_sample1

const int led_pin = 5;
const int vol_pin = 0;
const int lt_pin = 1;
const int tact_pin1 = 2;

int buttonState1 = 0; 
int vol_value = 0;
int lt_value = 0;
int tact_value = 0;

void setup() {
  pinMode(led_pin, OUTPUT);
  pinMode(tact_pin1, INPUT);
  Serial.begin( 9600 );
}

void loop() {
  byte buffer[8];

  vol_value = analogRead( vol_pin );
  lt_value = analogRead( lt_pin );
  tact_value = map(digitalRead(tact_pin1), 0, 1, 0, 255);
  
  analogWrite( led_pin, lt_value/32 );
 
  buffer[0] = byte( 'A');
  buffer[1] = byte( 0 );
  buffer[2] = byte( vol_value );
  buffer[3] = byte( vol_value >> 8 );
  buffer[4] = byte( lt_value );
  buffer[5] = byte( lt_value >> 8 );
  buffer[6] = byte( tact_value );
  buffer[7] = byte( 0 );
 
  Serial.write( buffer, 8 );
  Serial.read();

}
