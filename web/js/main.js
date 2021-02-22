async function pythonjs(){
    let data = await eel.display()();
    document.getElementById("eel").innerHTML = data;
}

function generateQRCode(){
    event.preventDefault();
    var detail = document.forms["detail"]["value"].value;
    var name = document.forms["detail"]["name"].value;
    var extension = document.forms["detail"]["extension"].value;
    if(detail=="" || extension==""){
        //pass
    }else{
        eel.generateQRCode(detail, name, extension)(changeImage);
    }
}

function changeImage(fileName){
    console.log("Working")
    document.getElementById("show-img").src = "QRcode/"+fileName;
}