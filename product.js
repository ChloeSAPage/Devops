const product = {
    name: "Cup",
    price: 5,
    getDetails() {
        return `Price of ${this.name} is £${this.price}`;
    },
};

const updatePrice = (product, new_price) => {
    const newProduct = { ...product };
    newProduct.price = new_price;
    return newProduct;
};

const newProduct = updatePrice(product, 10);
console.log(product.getDetails());
console.log(newProduct.getDetails());
