function startAlfred() {
    var python = require("python-shell")
    var path = require("path")

    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        pythonScript : 'C:/Python38'
    }

    var alfred = new python('/Alfred/alfred.py', options)

    alfred.on('message', function(message){
        swal(message)        
    })
}
