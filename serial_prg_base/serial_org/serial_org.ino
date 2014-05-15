
// serial_voltage_2byte_sample1

const int led_pin = 5;
const int vol_pin = 0;

int vol_value = 0;

void setup() {
  pinMode(led_pin, OUTPUT);
  Serial.begin( 9600 );
}

void loop() {
  byte buffer[9];
  int c = 0;
  int c1 = 0;

  vol_value = analogRead( vol_pin );
  analogWrite( led_pin, vol_value/32 );

  buffer[0] = byte( '~');
  buffer[1] = byte( '1' );
  buffer[2] = byte( vol_value );
  buffer[3] = byte( vol_value >> 8 );
  c = buffer[1] + buffer[2] + buffer[3] ;
  buffer[4] = byte ( c );
  buffer[5] = byte( '~' );
  Serial.write( buffer, 6 );
  //Serial.println(c);  

  buffer[0] = byte( '~');
  buffer[1] = byte( '2' );
  buffer[2] = byte( '}' );
  buffer[3] = byte( vol_value ) ^ 32;
  buffer[4] = byte( '}' );
  buffer[5] = byte( vol_value >> 8 ) ^ 32;
  buffer[6] = byte( '}' );
  c = buffer[1] + byte( vol_value ) + byte( vol_value >> 8 );
  buffer[7] = byte( c );
  buffer[8] = byte( '~' );
  Serial.write( buffer, 9 );
  // Serial.println(c);  

  buffer[0] = byte( '~');
  buffer[1] = byte( '3' );
  buffer[2] = byte( vol_value );
  buffer[3] = byte( vol_value >> 8 );
  buffer[4] = byte( '}' );
  c1 = buffer[1] + buffer[2] + buffer[3];
  c = c1 ^ 32;
  buffer[5] = byte( c );
  buffer[6] = byte( '~' );
  Serial.write( buffer, 7 );
  //Serial.println(c);  


  buffer[0] = byte( '~');
  buffer[1] = byte( '4' );
  buffer[2] = byte( '}' );
  buffer[3] = byte( vol_value );
  buffer[4] = byte( '}' );
  buffer[5] = byte( vol_value >> 8 ) ^ 32;
  c = buffer[1] + buffer[3] + byte( vol_value >> 8 );
  buffer[6] = byte( c );
  buffer[7] = byte( '~' );
  Serial.write( buffer, 8 );
}
