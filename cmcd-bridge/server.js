'use strict'

const express = require('express');
const mysql = require('mysql');

const app = express();

app.use(express.json());

// MySQL Connection
const connection = mysql.createConnection({
	host: 'mysql',
	user: 'node',
	password: 'password',
	database: 'cmcd'
});

// Connect to MySQL
connection.connect((err) => {
	if (err) throw err;
	console.log('Connected to MySQL');
});

// Route for POST request
app.post('/cmcd-logs', (req, res) => {
	const data = req.body;

	// MySQL Query to insert data
	const query = `INSERT INTO cmcd_data (time, br, bl, bs, cid, d, dl, mtp, nor, nrr, ot, pr, rtp, sf, sid, st, su, tb) VALUES (?)`;
	const values = [[
		data.time || null,
		data.br || null,
		data.bl || null,
		data.bs === undefined ? null : data.bs === 'true' ? 1 : 0,
		data.cid || null,
		data.d || null,
		data.dl || null,
		data.mtp || null,
		data.nor || null,
		data.nrr || null,
		data.ot || null,
		data.pr || null,
		data.rtp || null,
		data.sf || null,
		data.sid || null,
		data.st || null,
		data.su === undefined ? null : data.su === 'true' ? 1 : 0,
		data.tb || null
	]];

	// Execute MySQL Query
	connection.query(query, values, (err, result) => {
		if (err) throw err;
		console.log(`[${data.time}] Data inserted successfully`);
		res.status(200).send('Data inserted successfully');
	});
});

// Start Server
app.listen(8088, () => {
	console.log('Server started on port 8088');
});
