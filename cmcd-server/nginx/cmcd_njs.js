let querystring = require('querystring');

async function send(r) {
    try {
        let params = processQueryArgs(r);
        params.time = r.variables.time_iso8601;

        // Detached sub-reqest to send logs
        r.subrequest('/cmcd-bridge', {
            body: JSON.stringify(params),
            detached: true,
            method: 'POST'
        });

        // pass to media source to get file chunk
        function done(res) {
            r.return(res.status, res.responseBody);
        }
        r.subrequest(r.uri.split('/cmcd')[1], r.variables.args, done);
    } catch (e) {
        r.return(500, e);
    }
}

function version(r) {
    r.return(200, njs.version);
}

function processQueryArgs(r) {
    const decodedQueryString = querystring.decode(r.variables.query_string);

    let params = {};
    decodedQueryString.CMCD.split(',').forEach(param => {
        let key,value;
        if (param.includes('=')) {
            key = param.split('=')[0];
            value = param.split('=')[1].replace(/"/g, '');
        }  else {  // e.g. `bs` key does not have a value in CMCD query arg format
            key = param;
            value = 'true';
        }
        params[key] = value;
    });

    return params;
}

export default {send, version}
