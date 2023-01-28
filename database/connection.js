 
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });
const fs = require('fs');


client.connect((err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log("Connected to MongoDB");

    const db = client.db("cmcd-metrics");
    const collection = db.createCollection("cmcd-collection", (err, res) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log("CMCD Time series collection created");
        client.close();
    });
});
