
const express = require('express');
const app = express();
const port = 3000;
 
app.get('/', (req, res) => {
  res.send("Company Name: Wild Rydes, Developer Name: Renee Osbourne, Company ID: 100939044");
});
 
app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
