var request = require("request")

var jsondata = require("./main.json");

request.post({
    "headers": { "content-type": "application/json" },
    "url": "http://localhost:5000/sql_generate",
    "body": JSON.stringify({jsondata})
}, (error, response, body) => {
    if(error) {
        return console.dir(error);
    }
    console.log(body);
});