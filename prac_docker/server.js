import express from "express";
import {v4} from "uuid"

const app = express();

app.get('/', (req, res) => {
    res.json({
        id: v4() 
     })
    res.send('Hello World!')
})

app.listen(3000);
console.log('Server running on port 3000');
