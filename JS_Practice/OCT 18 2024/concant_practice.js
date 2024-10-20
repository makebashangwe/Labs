function getFullAddress(address){
    return address.street + ", " + address.city + ", " + address.state + ", " + address.zip;
    
}

const address = {
    street: "123 Main St",
    city: "Springfield",
    state: "IL",
    zip: "62701"
};

console.log(getFullAddress(address)); 