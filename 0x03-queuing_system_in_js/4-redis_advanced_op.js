import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.toString());
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client
  .MULTI()
  .HSET('ALX', 'Portland', 50, print)
  .HSET('ALX', 'Seatle', 80, print)
  .HSET('ALX', 'New York', 20, print)
  .HSET('ALX', 'Bogota', 20, print)
  .HSET('ALX', 'Cali', 40, print)
  .HSET('ALX', 'Paris', 2, print)
  .EXEC();

client.HGETALL('ALX', (err, res) => console.log(res));
