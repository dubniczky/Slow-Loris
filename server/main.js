const express = require('express')

const app = express()
const port = process.argv[2] ?? 80

app.get('/', (req, res) => {
    res.send('Hello Human!')
})

app.listen(port, () => {
    console.log('Server listening on port:', port)
})