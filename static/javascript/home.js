var myIndex = 0;

function carousel() {
  console.log('test')
  var i;
  var x = document.getElementsByClassName("slide");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
}
// setTimeout(carousel, 2000); // Change image every 2 seconds

setInterval(carousel,2000)