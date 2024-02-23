const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send("Company Name: Wild Rydes, Developer Name: Renee Osbourne, Company ID: 100939044");
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:3000`);
});
