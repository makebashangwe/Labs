//console.log("PeePee");
//console.log("I like peeepeeeee")

//window.alert("You can't pee here!")

//document.getElementById("myH1").textContent = "Hello World";
//document.getElementById("myP").textContent= "I like PeePee";
//this is a comment (wont appear in the console either)
function showContent() {
    let ageInput = document.getElementById('ageInput').value;
    let contentContainer = document.getElementById('content');
    let ageInputContainer = document.getElementById('ageInputContainer');

    if (ageInput >= 18) {
        contentContainer.style.display = 'block';
        ageInputContainer.style.display = 'none';
    } else {
        alert('You may not proceed.');
    }
}


document.getElementById("mySubmit").onclick = function(){
    username = document.getElementById("myText").value;
    document.getElementById("myH1").textContent = "Welcome, " + username + "!"
}