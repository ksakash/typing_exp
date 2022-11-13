const express = require("express");
const path = require("path");

const code_snippets = require('./data/data.json');

function getRandomCodeSnippet() {
    const randomIndex = Math.floor(Math.random() * code_snippets.length);
    return code_snippets[randomIndex];
}

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", function(req, res) {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.get("/new_code", function(req, res) {
    let code_snippet = getRandomCodeSnippet()
    res.json({
      data: code_snippet
    })
    .end();
});

app.use("/public", express.static("./public"));

app.listen(3000);
console.log("listening on http://localhost:3000");
