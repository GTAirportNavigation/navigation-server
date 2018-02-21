function searchFlightNo() {
    var test = document.getElementById("flightno").value
    var rf = ""
    var rd = ""
    var rg = ""
    var rs = ""

    if (test == "DL1") {
        rf = test
        rd = "Seattle"
        rg = "T12"
        rs = "<font color='green'>On Time</font>"
        document.getElementById("result").style.visibility = "visible";
    } else if (test == "DL2") {
        rf = test
        rd = "New York"
        rg = "T3"
        rs = "<font color='red'>Delayed</font>"
        document.getElementById("result").style.visibility = "visible";
    } else {
        document.getElementById("result").style.visibility = "hidden";
    }

    document.getElementById("rf").innerHTML = rf
    document.getElementById("rd").innerHTML = rd
    document.getElementById("rg").innerHTML = rg
    document.getElementById("rs").innerHTML = rs
}

function getNavigation() {
    // jQuery.get('http://127.0.0.1:8000/nav')
    console.log(document.location.href)
    document.location.href = document.location.href + "flight/" + document.getElementById("rf").innerHTML
}