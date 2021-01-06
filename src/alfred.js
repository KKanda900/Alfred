
function startSpeech(){
    var T = document.getElementById("al_model");
    T.style.display = "block";

    var python = require('child_process').spawn('python', ['.\\alfred.py'])
    python.stdout.on('data', function(data){
        console.log("data: ", data.toString('utf8'));
    });
}