function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//display and hide the sidebar
function openNav() {
    document.getElementById("mySideBar").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
    document.getElementById("mySideBarX").style.display= "block";
    document.getElementById("openbtn").style.display = "none";
}

//display and hide the sidebar
function closeNav() {
    document.getElementById("mySideBarX").style.display = "none";
    document.getElementById("openbtn").style.display = "block";
    document.getElementById("mySideBar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}

//for implementing class "collapsible"
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}