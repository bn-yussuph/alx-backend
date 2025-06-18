// const redis = require('redis');

import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.toString());
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const listen = (message) => console.log(message);

client.subscribe('ALXchannel');

client.on('message', (channel, message) => {
  if (channel === 'ALXchannel') {
    if (message === 'KILL_SERVER') {
      client.UNSUBSCRIBE();
      client.QUIT();
    }
    listen(message);
  }
});
