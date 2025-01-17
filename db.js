let mysql = require('mysql2');

            let con = mysql.createConnection({
            host: "localhost",
            user: "root",
            password: "root",
            database: "paymentdb",
            });

            con.connect(function(err) {
            if (err) throw err;
            console.log("Connected!");
            let sql = "INSERT INTO users (email,password) VALUES (registeremail,registerpassword)";
            con.query(sql, function (err, result) {
                if (err) throw err;
                console.log("1 record inserted");
            });
            }); 