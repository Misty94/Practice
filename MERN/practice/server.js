const express = require('express');
const port = 8000;
const app = express();
const mongoose = require('mongoose');
const cors = require('cors'); // allows the backend api to share resources with our react app

app.use( express.json(), express.urlencoded({ extended: true }) );
app.use(cors());

require("./server/config/mongoose.config") // 
require("./routes/product.routes")(app)


// This needs to be below the other code blocks
app.listen(port, () => console.log(`Listening to this port: ${port}`));