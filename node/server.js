const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");
const math = require("math");

http.createServer((req, res) => {
    if (req.url === "/") {
            fs.readFile("./Public/index.html", "UTF-8", (err, body) => {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(body)
        });
    } else if (req.url.match("/sysinfo")) {
        // hostname
        myHostName = os.hostname()
        
        // days, hours, minutes, seconds
        let days = math.floor(os.uptime() / (3600 * 24))
        let hours = math.floor((os.uptime() % (3600 * 24)) / 3600)
        let minutes = math.floor((os.uptime() % 3600) / 60)
        let seconds = math.floor(os.uptime() % 60)
        
        // total memory and free memory
        let totalMemMB = os.totalmem() / (1024 * 1024)
        let freeMemMB = os.freemem() / (1024 * 1024)

        // total cpu
        let cpus = os.cpus().length
         
        html = 
       `<!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: days: ${days}, hours: ${hours}, minutes: ${minutes}, seconds: ${seconds}</p>
                <p>Total Memory: ${totalMemMB} MB</p>
                <p>Free Memory: ${freeMemMB} MB</p>
                <p>Number of CPUs: ${cpus}</p>
            </body>
        </html>`
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(html)
    } else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end(`404 File Not Found at ${req.url}`)
    }
}).listen(3000)

console.log("Server listening on port 3000")