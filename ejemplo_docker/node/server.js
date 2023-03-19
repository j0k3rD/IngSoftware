var http = require('http').Server(); // Creamos el servidor HTTP
var io = require('socket.io')(http); // Creamos el servidor Socket.IO y lo asociamos al servidor HTTP, sobre este va a escuchar
var redis = require('redis'); // Vamos a estar escuchando desde Node un canal de Redis para saber que pasa con la task de Celery

var redisClient = redis.createClient(6379, 'redis'); // Creamos el cliente de Redis

io.on('connection', function(socket) { // Cuando se conecte un cliente Socket.IO vamos a escuchar el canal de Redis
    console.log('A User has Connected...');

    socket.on('subscribe', function(celeryTaskId) { // Cuando se conecte un cliente Socket.IO vamos a escuchar el canal de Redis
        redisClient.subscribe(celeryTaskId); // Nos suscribimos al canal de Redis.
    }); 

    redisClient.on('message', function(channel, message) { // Cuando se publique un mensaje en el canal de Redis
        socket.emit('result', message); // Emitimos el mensaje al cliente Socket.IO
    });
});

http.listen(3000, function() { // Escuchamos en el puerto 3000
    console.log('Listening on Port 3000...');
});