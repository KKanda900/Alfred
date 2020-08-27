/* function startAlfred() {
    var {python, PythonShell} = require("python-shell")
    var path = require("path")

    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        pythonScript : 'C:/Python38'
    }

    var alfred = new PythonShell("alfred.py", options);

    alfred.end(function(err, code, message)
    {
        document.getElementById("summon").value = "Summoning Alfred";
    })
} */

/* function startAlfred() {
    var python = require('child_process').spawn('python', ['./alfred.py']);
    python.stdout.on('data', function(data){
        console.log("data:", data.toString('utf8'));
    });
} */
/* 
function startAlfred() {
    const {PythonShell} = require("python-shell");
    PythonShell.run('/alfred.py', {scriptPath: '/Desktop/Personal Projects/ElectronJS/Alfred/src/'}, function(err) {
        if (err) throw err;
        console.log('finished');
    });
} */

function startAlfred() {
    var child = require('child_process').execFile;
    var executablePath = "C:\\Users\\kkand\\Desktop\\Personal Projects\\ElectronJS\\Alfred\\src\\dist\\alfred.exe";

    child(executablePath, function (err, data) {
        if (err) {
            console.error(err);
            return;
        }

        console.log(data.toString());
    });
}
