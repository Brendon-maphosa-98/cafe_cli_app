CREATE TABLE IF NOT EXISTS products (
    "Product ID" UUID NOT NULL,
    "Name" VARCHAR(200) NOT NULL,
    "Price" MONEY NOT NULL,
    PRIMARY KEY ("Product ID")
);