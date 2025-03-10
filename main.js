const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const messageHandler = require("./src/messageHandler");

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

client.on("qr", (qr) => {
  qrcode.generate(qr, { small: true });
});

client.once("ready", () => {
  console.log("Ready to serve!");
});

client.on("message", (message) => {
  messageHandler(client, message);
});

console.log("Initializing client...");
client.initialize();
