function instagram_qr() {
    document.getElementById("insta").src = "img/shadowlou_qr.png";
}

function contact_qr_code() {
    document.getElementById("mail_contact").src = "img/contact_qr.png";
    document.getElementById("email").style.display = "block";
}

function changeImg(itemID=String,newIMG=String) {
    document.getElementById(itemID).src = newIMG;
}

function banner_scroll(){
    
}
