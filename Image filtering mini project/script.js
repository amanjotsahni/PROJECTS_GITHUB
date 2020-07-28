var image = null;
var redfilter=null;
var grayfilter=null;
var rainbowfilter=null;
var blurfilter=null;
var canvas1;
var imgFile;
var ra;
var r2,r3;

function upload(){
  image=document.getElementById("finput");
   imgFile=new SimpleImage(image);
   canvas1=      document.getElementById("can1");
  redfilter = new SimpleImage(image);
  grayfilter = new SimpleImage(image);
  rainbowfilter = new SimpleImage(image);
  blurfilter = new SimpleImage(image);
  imgFile.drawTo(canvas1);
  
}
function makeredfilter(){
  for (var pixel of redfilter.values()){
   var avg = (pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    if(avg<128){
      pixel.setRed(2*avg);
      pixel.setGreen(0);
      pixel.setBlue(0);
    }
    else
     { pixel.setRed(255);
      pixel.setGreen((2*avg)-255);
      pixel.setBlue((2*avg)-255);
     }
  }
  redfilter.drawTo(canvas1);
}
function makegrayscale(){
  x=grayfilter.getWidth();
  y=grayfilter.getHeight();
  for (var pixel of grayfilter.values()){
   
    var avg = (pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    pixel.setRed(avg);
    pixel.setGreen(avg);
    pixel.setBlue(avg);
  }
  grayfilter.drawTo(canvas1);
}

function resetImage(){
  imgFile.drawTo(canvas1);
  redfilter = new SimpleImage(image);
  grayfilter = new SimpleImage(image);
  rainbowfilter = new SimpleImage(image);
  blurfilter = new SimpleImage(image);
}
function rainbow(){
  
  for( var pixel of rainbowfilter.values()){
    var avg = (pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    if(pixel.getY()<=rainbowfilter.getHeight()*1/7){
      //for red color
      if(avg<128){
      pixel.setRed(2*avg);
      pixel.setGreen(0);
      pixel.setBlue(0);
    }
    else
     { pixel.setRed(255);
      pixel.setGreen((2*avg)-255);
      pixel.setBlue((2*avg)-255);
     }
    }
else if(pixel.getY()>rainbowfilter.getHeight()*1/7 && pixel.getY()<=rainbowfilter.getHeight()*2/7){
  // for orange color.
  if(avg<128){
      pixel.setRed(2*avg);
      pixel.setGreen(0.8*avg);
      pixel.setBlue(0);
    }
    else
     { pixel.setRed(255);
      pixel.setGreen((1.2*avg)-51);
      pixel.setBlue((2*avg)-255);
     }  
   }
    
    else if(pixel.getY()>rainbowfilter.getHeight()*2/7 && pixel.getY()<=rainbowfilter.getHeight()*3/7){
      //for YELLOW COLOR
  if(avg<128){
      pixel.setRed(2*avg);
      pixel.setGreen(2*avg);
      pixel.setBlue(0);
    }
    else
     { pixel.setRed(255);
      pixel.setGreen(255);
      pixel.setBlue((2*avg)-255);
     }     
   }
    
    else if(pixel.getY()>rainbowfilter.getHeight()*3/7 && pixel.getY()<=rainbowfilter.getHeight()*4/7){
      //for GREEN COLOR
  if(avg<128){
      pixel.setRed(0);
      pixel.setGreen(2*avg);
      pixel.setBlue(0);
    }
    else
     { pixel.setRed((2*avg)-255);
      pixel.setGreen(255);
      pixel.setBlue((2*avg)-255);
     }
   }
    
       else if(pixel.getY()>rainbowfilter.getHeight()*4/7 && pixel.getY()<=rainbowfilter.getHeight()*5/7){
      //for BLUE COLOR
  if(avg<128){
      pixel.setRed(0);
      pixel.setGreen(0);
      pixel.setBlue(2*avg);
    }
    else
     { pixel.setRed((2*avg)-255);
      pixel.setGreen((2*avg)-255);
      pixel.setBlue(255);
     }    
   }
    
    else if(pixel.getY()>rainbowfilter.getHeight()*5/7 && pixel.getY()<=rainbowfilter.getHeight()*6/7){
      //for INDIGO COLOR
  if(avg<128){
      pixel.setRed(0.8*avg);
      pixel.setGreen(0);
      pixel.setBlue(2*avg);
    }
    else
     { pixel.setRed((1.2*avg)-51);
      pixel.setGreen((2*avg)-255);
      pixel.setBlue(255);
     }    
   }
    else if(pixel.getY()>rainbowfilter.getHeight()*6/7 ){
      //for VIOLET COLOR
  if(avg<128){
      pixel.setRed(1.6*avg);
      pixel.setGreen(0);
      pixel.setBlue(1.6*avg);
    }
    else
     { pixel.setRed((0.4*avg)+153);
      pixel.setGreen((2*avg)-255);
      pixel.setBlue((0.4*avg)+153);
     }  
   }
  }
  rainbowfilter.drawTo(canvas1);
}

function getRandom() {
  return Math.random();
}
function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}
function blur(){
  for(var pixel of blurfilter.values()){
    ra=getRandom();
    if(ra<0.5){
       pixel.setX()=pixel.getX;
    pixel.setY()=pixel.getY;
    
    }
    if(ra>0.5){
       r2=getRandomArbitrary(0, 10);
      r3=getRandomArbitrary(0, 10);
       pixel.setX()=pixel.getX-r2;
    pixel.setY()=pixel.getY-r3;
    
      
      if(pixel.setX()<0 || pixel.setX()>blurfilter.getWidth()-1){
         r2=getRandomArbitrary(0, 10);
         pixel.setX()=pixel.getX-r2;
      }
       if(pixel.setY()<0 || pixel.setY()>blurfilter.getHeight()-1){
         r3=getRandomArbitrary(0, 10);
          pixel.setY()=pixel.getY-r3;
       }
    } 
  }
  blurfilter.drawTo(canvas1);
  
}