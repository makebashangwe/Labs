
function getUsersEmails (users){
    return users.map(user => user.email); 
}
/* 
.map() expects a function as its argument.
the arrow function (user => user.email) is the function,
shorthand for function getEmail(user){return user.email;} is const getEmail (user) => {return user.email;}
can be simplified even more to const getEmail = user => user.email;

=> seperates the parameter from the function body.
user is the function parameter, => is pointing to the function user.email() which is being returned

summary: 
user.map() takes a function adn applies it to each element in teh users array
user = > user.email tells it to take each user and reutnr the email property specigcally.
wich is why map returns an array of emails!
*/
const users = [
    { name: "Alice", email: "alice@example.com" },
    { name: "Bob", email: "bob@example.com" },
  ];
  console.log(getUsersEmails(users)); 