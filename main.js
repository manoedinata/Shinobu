const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const WebSocket = require("ws");
const messageHandler = require("./src/messageHandler");

const wss = new WebSocket.Server({ port: 8080 });

const client = new Client({
  puppeteer: {
    headless: true,
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--disable-infobars",
      "--disable-extensions",
      "--disable-gpu",
      "--no-first-run",
      "--no-zygote",
      "--single-process",
    ],
  },
  authStrategy: new LocalAuth({
    dataPath: "./sessions",
  }),
});
let clientInfo = null;
let qrCode = null;

client.on("qr", (qr) => {
  qrCode = qr;
  qrcode.generate(qr, { small: true });

  broadcast({ event: "qr", data: qrCode });
});

client.once("ready", async () => {
  console.log("Ready to serve!");
  clientInfo = await client.info;

  broadcast({
    event: "ready",
    data: clientInfo,
  });
});

client.on("message", (message) => {
  messageHandler(client, message);
});

// Broadcast data to all connected clients
function broadcast(data) {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
}

wss.on("connection", async (ws) => {
  if (clientInfo) {
    ws.send(JSON.stringify({ event: "ready", data: clientInfo }));
  } else if (qrCode) {
    ws.send(JSON.stringify({ event: "qr", data: qrCode }));
  }

  ws.on("message", (message) => {
    const data = JSON.parse(message);

    switch (data.message) {
      // Probably unused; the client will instead listen to our sent message
      case "status":
        let status = clientInfo
          ? {
              event: "ready",
              data: clientInfo,
            }
          : {
              event: "qr",
              data: qrCode,
            };
        ws.send(JSON.stringify(status));
        break;
    }
  });
});

console.log("Initializing client...");
client.initialize();
