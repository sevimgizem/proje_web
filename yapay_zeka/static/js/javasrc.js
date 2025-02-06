function soruGonder() {
    var soru = document.getElementById("soru").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cevap", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var cevap = JSON.parse(xhr.responseText);
            document.getElementById("cevap").innerText = cevap;
        }
    };
    var data = JSON.stringify({"soru": soru});
    xhr.send(data);
}
