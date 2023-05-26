document.getElementById("passer_admin").addEventListener("click", () => {
    partie_admin = document.getElementsByClassName("admin");
    if (document.getElementById("passer_admin").innerHTML === "Passer en mode administrateur"){
        document.getElementById("passer_admin").innerHTML = "Passer en mode client";
        for(let i = 0; i < partie_admin.length; i++){
            partie_admin[i].style.display = "block";
        }
    } else {
        document.getElementById("passer_admin").innerHTML = "Passer en mode administrateur";
        for(let i = 0; i < partie_admin.length; i++){
            partie_admin[i].style.display = "none";
        }
    }
});
