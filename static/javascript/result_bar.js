var i = 0;
window.onload = function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("likes");
    var total_votes = document.getElementById("total_count").textContent;
    var likes = document.getElementById("true_count").textContent;
    var value = Math.floor(likes * 100 / total_votes);
    var width = 50;
    var id = setInterval(frame, 23);

    function frame() {

        if (width < value) {
          width++;
          elem.style.width = width + "%";
        } 
        else if (width > value) {
          width--;
          elem.style.width = width + "%";
        } else {
          clearInterval(id);
        }

    }
  }
}