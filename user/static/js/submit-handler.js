// function for highlighting the nav bar with Active page
let pathname = window.location.pathname;
pathname = pathname.split("user/")[1].toLowerCase();

function handleClient(client) {
  document.querySelector("." + client + "-icon").style.display = "block";
  document.querySelector(".sidebar-nav-itm-" + client).classList.add("active");
}

if (pathname.includes("login")) {
  document.querySelector(".heading").innerHTML = "Login";
  document.querySelector(".heading").style.display = "block";
}

