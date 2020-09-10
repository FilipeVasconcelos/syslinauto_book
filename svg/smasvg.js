var files =[];
for (let i = 1; i <= 298; i++) {
      files.push("sma_auto"+i+".svg");
} 

var arr = new collection(files);

function collection(imgs) {
  this.imgs = imgs;
  this.i = 0;
  this.next = function(id) {
    var img = document.getElementById(id);
    this.i++;
    if (this.i >= imgs.length) {
      this.i = 0;
    }
    img.src = imgs[this.i];
  };
 
  this.prev = function(id) {
    var img = document.getElementById(id);
  
    this.i--;
    if (this.i < 0) {
      this.i = imgs.length - 1;
    }
  
    img.src = imgs[this.i];
  };
  
    //  this.next("Img"); // to initialize with some image
}
