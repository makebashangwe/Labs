function getUserNames(users){
    return users.map(user => user.name)
}


const users = [
    { name: "Alice", email: "alice@example.com" },
    { name: "Bob", email: "bob@example.com" },
    { name: "Charlie", email: "charlie@example.com" },
];

console.log(getUserNames(users)); 

