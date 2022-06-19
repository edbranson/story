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
  document.getElementById("mySideNavClose").classList.remove("hidden");
  document.getElementById("mySideBar").classList.remove("hidden");
  document.getElementById("mySideRight").classList.remove("col-start-1");
  document.getElementById("mySideRight").classList.add("col-start-3");
  document.getElementById("mySideNavOpen").classList.add("hidden");
}

//display and hide the sidebar
function closeNav() {
  document.getElementById("mySideNavClose").classList.add("hidden");
  document.getElementById("mySideBar").classList.add("hidden");
  document.getElementById("mySideRight").classList.remove("col-start-3");
  document.getElementById("mySideRight").classList.add("col-start-1");
  document.getElementById("mySideNavOpen").classList.remove("hidden");    
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

//for implementing loading spinner


function myFunction() { 
  var myVar; 
  myVar = setTimeout(showPage, 2000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  // document.getElementById("mySideRight").style.display = "block";
}