require('dotenv').config();
const cors = require("cors");
const express = require("express");
const app = express();
const path = require('path');
const languageHandler = require("./src/languages");

app.use(cors({}));

app.use('/static', express.static('static'));

app.get('/', (req, res) => {
  res.redirect("/index.html");
})

app.get('/:site_file', (req,res) => {
  let template = req.params.site_file;
  res.sendFile(path.join(`${__dirname}/templates/${template}`));
})

app.get('/language/:lang', (req,res)=>{
  let lang = req.params.lang;
  res.send(languageHandler.languageSwitcher(lang));
})

app.listen(process.env.PORT);
console.log(`Listening On: ${process.env.PORT}`);
