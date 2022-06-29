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

// the sidebar is closed ... show hamburger menue
function openNav() {
  if (document.getElementById("mySideNavOpen").classList.contains("block")){
    document.getElementById("mySideNavOpen").classList.replace("block", "hidden");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("sm:block")){
    document.getElementById("mySideNavOpen").classList.replace("sm:block", "sm:hidden");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("md:block")){
    document.getElementById("mySideNavOpen").classList.replace("md:block", "md:hidden");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("lg:block")){
    document.getElementById("mySideNavOpen").classList.replace("lg:block", "lg:hidden");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("xl:block")){
    document.getElementById("mySideNavOpen").classList.replace("xl:block", "xl:hidden");
  };

  if (document.getElementById("mySideNavClose").classList.contains("hidden")){
    document.getElementById("mySideNavClose").classList.replace("hidden", "block");
  };
  if (document.getElementById("mySideNavClose").classList.contains("sm:hidden")){
    document.getElementById("mySideNavClose").classList.replace("sm:hidden", "sm:block");
  };
  if (document.getElementById("mySideNavClose").classList.contains("md:hidden")){
    document.getElementById("mySideNavClose").classList.replace("md:hidden", "md:block");
  };
  if (document.getElementById("mySideNavClose").classList.contains("lg:hidden")){
    document.getElementById("mySideNavClose").classList.replace("lg:hidden", "lg:block");
  };
  if (document.getElementById("mySideNavClose").classList.contains("xl:hidden")){
    document.getElementById("mySideNavClose").classList.replace("xl:hidden", "xl:block");
  };

  if (document.getElementById("mySideBar").classList.contains("hidden")){
    document.getElementById("mySideBar").classList.replace("hidden", "block");
  };
  if (document.getElementById("mySideBar").classList.contains("sm:hidden")){
    document.getElementById("mySideBar").classList.replace("sm:hidden", "sm:block");
  };
  if (document.getElementById("mySideBar").classList.contains("md:hidden")){
    document.getElementById("mySideBar").classList.replace("md:hidden", "md:block");
  };
  if (document.getElementById("mySideBar").classList.contains("lg:hidden")){
    document.getElementById("mySideBar").classList.replace("lg:hidden", "lg:block");
  };
  if (document.getElementById("mySideBar").classList.contains("xl:hidden")){
    document.getElementById("mySideBar").classList.replace("xl:hidden", "xl:block");
  };

  if( document.getElementById("mySideRight").classList.contains("col-start-1")){
    document.getElementById("mySideRight").classList.replace("col-start-1", "hidden");
  };
  if( document.getElementById("mySideRight").classList.contains("sm:col-start-1")){
    document.getElementById("mySideRight").classList.replace("sm:col-start-1", "hidden");
  };
  if( document.getElementById("mySideRight").classList.contains("md:col-start-1")){
    document.getElementById("mySideRight").classList.replace("md:col-start-1", "md:col-start-2");
  };
  if( document.getElementById("mySideRight").classList.contains("lg:col-start-1")){
    document.getElementById("mySideRight").classList.replace("lg:col-start-1", "lg:col-start-2");
  };
  if( document.getElementById("mySideRight").classList.contains("xl:col-start-1")){
    document.getElementById("mySideRight").classList.replace("xl:col-start-1", "xl:col-start-2");
  };  
    

}

//the sidebar is open ... show X to close sidebar
function closeNav() {
  if (document.getElementById("mySideNavClose").classList.contains("block")){
    document.getElementById("mySideNavClose").classList.replace("block", "hidden");
  };
  if (document.getElementById("mySideNavClose").classList.contains("sm:block")){
    document.getElementById("mySideNavClose").classList.replace("sm:block", "sm:hidden");
  };
  if (document.getElementById("mySideNavClose").classList.contains("md:block")){
    document.getElementById("mySideNavClose").classList.replace("md:block", "md:hidden");
  };
  if (document.getElementById("mySideNavClose").classList.contains("lg:block")){
    document.getElementById("mySideNavClose").classList.replace("lg:block", "lg:hidden");
  };
  if (document.getElementById("mySideNavClose").classList.contains("xl:block")){
    document.getElementById("mySideNavClose").classList.replace("xl:block", "xl:hidden");
  };
  console.log("start NavOpen")
  if (document.getElementById("mySideNavOpen").classList.contains("hidden")){
    document.getElementById("mySideNavOpen").classList.replace("hidden", "block");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("sm:hidden")){
    document.getElementById("mySideNavOpen").classList.replace("sm:hidden", "sm:block");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("md:hidden")){
    document.getElementById("mySideNavOpen").classList.replace("md:hidden", "md:block");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("lg:hidden")){
    document.getElementById("mySideNavOpen").classList.replace("lg:hidden", "lg:block");
  };
  if (document.getElementById("mySideNavOpen").classList.contains("xl:hidden")){
    document.getElementById("mySideNavOpen").classList.replace("xl:hidden", "xl:block");
  };
  console.log("start SideBar")
  if (document.getElementById("mySideBar").classList.contains("block")){
    document.getElementById("mySideBar").classList.replace("block", "hidden");
  };
  if (document.getElementById("mySideBar").classList.contains("sm:block")){
    document.getElementById("mySideBar").classList.replace("sm:block", "sm:hidden");
  };
  if (document.getElementById("mySideBar").classList.contains("md:block")){
    document.getElementById("mySideBar").classList.replace("md:block", "md:hidden");
  };
  if (document.getElementById("mySideBar").classList.contains("lg:block")){
    document.getElementById("mySideBar").classList.replace("lg:block", "lg:hidden");
  };
  if (document.getElementById("mySideBar").classList.contains("xl:block")){
    document.getElementById("mySideBar").classList.replace("xl:block", "xl:hidden");
  };
  
  console.log("start SideRight")
  if( document.getElementById("mySideRight").classList.contains("hidden")){
    document.getElementById("mySideRight").classList.replace("hidden", "col-span-6");
  };
  if( document.getElementById("mySideRight").classList.contains("sm:hidden")){
    document.getElementById("mySideRight").classList.replace("sm:hidden", "sm:col-span-6");
  };
  if( document.getElementById("mySideRight").classList.contains("md:col-start-2")){
    document.getElementById("mySideRight").classList.replace("md:col-start-2", "md:col-start-1");
  };
  if( document.getElementById("mySideRight").classList.contains("lg:col-start-2")){
    document.getElementById("mySideRight").classList.replace("lg:col-start-2", "lg:col-start-1");
  };
  if( document.getElementById("mySideRight").classList.contains("xl:col-start-2")){
    document.getElementById("mySideRight").classList.replace("xl:col-start-2", "xl:col-start-1");
  };  
  
   
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