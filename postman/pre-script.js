const uuid = require('uuid');
const generatedUUID = uuid.v4();

const jsonData = JSON.parse(pm.request.body);
const email = jsonData.email;

pm.environment.set("CODESQUAD_BLACKLIST_UUID", generatedUUID);
pm.environment.set("CODESQUAD_BLACKLIST_EMAIL", email);