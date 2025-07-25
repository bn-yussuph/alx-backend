#!/usr/bin/node
/*
 *
 *
 *
 */
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.error(error);
});

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  console.log(`reserved qty: ${stock}`);
  return stock !== null ? parseInt(stock, 10) : null;
}

app.get('/list_products', (request, response) => response.json(listProducts));

app.get('/list_products/:itemId', async (request, response) => {
  const itemId = parseInt(request.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return response.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  console.log(`route stock qty: ${currentStock}`);

  const stock = currentStock !== null ? currentStock : product.initialAvailableQuantity;
  console.log(`stock: ${stock}`);

  return response.json({ ...product, currentQuantity: stock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  let currentStock = await getCurrentReservedStockById(itemId);

  if (currentStock === null) {
    currentStock = product.initialAvailableQuantity;
  }
  if (currentStock < 1) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`server listening on port ${port}.`);
});
