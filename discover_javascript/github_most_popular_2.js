var https = require('https');

var options = {
    host: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc' ,
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 6e7f3146a1a9d7a12e4aceac3f3918c2fa57be6a'
    }
}

var req = https.request(options, function(res) {
    res.on('data',  function(d)  {
    console.log("Some data was received")
    
    });

});
req.end();

req.on('error', function(e) {
    console.error(e);
})

function streamToString(d, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}

