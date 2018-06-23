const express = require('express')
const history = require('connect-history-api-fallback')
const app = express()
// Express server.
const staticFileMiddleware = express.static(__dirname + "/dist")
app.use(staticFileMiddleware)
app.use(history({
 disableDotRule: true,
 verbose: true
}))
app.use(staticFileMiddleware)
var port = process.env.PORT || 5000;
app.listen(port, () => {
 console.log('App listening on port ${5555}!')
})
