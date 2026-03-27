function fbtn_click(){
  document.getElementById("lis").appendChild(document.createTextNode("Oh! What a wonderful world!"))
}

document.getElementById("fbtn").addEventListener("click", fbtn_click)
