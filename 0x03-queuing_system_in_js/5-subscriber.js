import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    console.log(message);
    client.unsubscribe(channel, (err) => {
      if (!err) {
        client.quit();
      };
    });
  } else {
    console.log(message);
  };
});
