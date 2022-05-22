const http = require('http')

const port = process.argv[2] ?? 80

const requestListener = function (req, res) {
    console.log(req.headers)
    res.writeHead(200)
    res.send('Hello Human!')
}

const server = http.createServer(requestListener)
server.listen(port)