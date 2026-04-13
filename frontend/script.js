const API = "http://127.0.0.1:5000";

function addSQL() {
    const name = document.getElementById("name").value;

    fetch(API + "/add_sql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.msg;
    });
}

function addNoSQL() {
    const name = document.getElementById("name").value;

    fetch(API + "/add_nosql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.msg;
    });
}