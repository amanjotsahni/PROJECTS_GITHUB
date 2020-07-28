/*THIS TUTORIAL USED GSM SIM900A MINI V3.9.2
 
  Connect 5VT to D9 and 5VR to D10
  Feed GSM SIM900A with Arduino's 5V

  Code by IDAYU SABRI - MYBOTIC
*/

#include <SoftwareSerial.h>
#include <Wire.h>
#include<LiquidCrystal.h>
SoftwareSerial mySerial(9, 10);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
const int sensor=A1;
float tempc;  //variable to store temperature in degree Celsius
float tempf;  //variable to store temperature in Fahreinheit 
float vout;  // Assigning analog pin A1 to variable 'sensor'
double alpha=0.75;
   int period=20;
   double refresh=0.0;
char msg;
char call;

void setup()
{
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);
   Serial.println("GSM SIM900A BEGIN");
    Serial.println("Enter character for control option:");
    Serial.println("s : to send message");
  delay(100);
  pinMode(sensor,INPUT); // Configuring pin A1 as input
Serial.begin(9600);
lcd.begin(16,2);  
  delay(500);
   pinMode(A0,INPUT);
   lcd.begin(16,2);
//   lcd.backlight(); //Uncomment when using a I2C
   lcd.clear();
   lcd.setCursor(0,0);


}

void loop()
{ 
 vout=analogRead(sensor);
 tempc = (double)vout / 1024;   //find percentage of input reading
  tempc = tempc * 5;                     //multiply by 5V to get voltage
  tempc = tempc - 0.5;                   //Subtract the offset 
  tempc = tempc * 100;
tempf=(vout*1.8)+32; // Converting to Fahrenheit 
lcd.setCursor(0,0);
lcd.print("in DegreeC= ");
lcd.print(tempc);
lcd.setCursor(0,1);
lcd.print("in Fahrenheit=");
lcd.print(tempf);
delay(1000);
static double oldValue=0;
   static double oldrefresh=0;
   int beat=analogRead(A0);
  double value=alpha*oldValue+(0-alpha)*beat;
   refresh=value-oldValue;
   lcd.setCursor(0,0);
   lcd.print(" Heart Monitor "); 
   lcd.setCursor(0,1);
   lcd.print("          ");
   lcd.setCursor(0,1);
   int a=beat/10; 
   lcd.print(a);
     oldValue=value;
   oldrefresh=refresh;
   delay(period*10);
delay(5000);
  if (Serial.available()>0)
  if(a>20){
   switch(Serial.read())
  {
    case 's':
      SendMessage();
      break;
   if (mySerial.available()>0)
 Serial.write(mySerial.read());
}}}

void SendMessage()
{
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"+919877471845\"\r"); // Replace x with mobile number
  delay(1000);
  mySerial.println("heart rate is not normal");// The SMS text you want to send
  delay(100);
   mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(1000);
}
