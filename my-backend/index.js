const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MySQL connection setup
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Walf000@', // Replace with your MySQL password
  database: 'mydatabase1' // Replace with your database name
});

db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database');
});

// API endpoint for contact form submission
app.post('/api/contact', (req, res) => {
  const { name, email, message, website } = req.body;
  const sql = 'INSERT INTO contacts (name, email, message, website) VALUES (?, ?, ?, ?)';
  db.query(sql, [name, email, message, website], (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Server error');
    } else {
      res.status(200).send('Message received');
    }
  });
});

app.post('/api/email', (req, res) => {
    const { email} = req.body;
    const sql = 'INSERT INTO emails (email) VALUES (?)';
    db.query(sql, [email], (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Server error');
      } else {
        res.status(200).send('Message received');
      }
    });
  });


const port = process.env.PORT || 5001;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});