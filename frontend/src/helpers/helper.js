function getIpPort() {
  var ip = location.hostname;
  if (location.port == "") {
    var port = 80;
  } else {
    var port = location.port;
  }

  return { ip: ip, port: port };
}

export { getIpPort };
