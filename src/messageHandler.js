const image2sticker = require("./functions/image2sticker");

module.exports = async (client, message) => {
  const { body, from } = message;

  const chat = await message.getChat();

  // Don't respond to group tag (for now)
  if (
    chat.isGroup &&
    message.mentionedIds.includes(client.info.wid._serialized)
  ) {
    return await client.sendMessage(
      chat.id._serialized,
      "Halo! Aku hanya bisa merespon di _private chat_. PM aku, ya!"
    );
  }

  // Auto-reply for non-commands
  if (!body.startsWith("/")) {
    return await client.sendMessage(
      from,
      "Hi there! I'm Shinobu. Use /help to see available commands."
    );
  }

  // Basic commands
  const [rawCommand, ...args] = body.slice(1).split(" ");
  const command = rawCommand.toLowerCase();

  switch (command) {
    // Convert to sticker
    case "sticker":
      if (!message.hasMedia) {
        await client.sendMessage(from, "Please send an image to convert.");
        break;
      }

      await image2sticker(message, client, args);
      break;

    // Ping!
    case "ping":
      await client.sendMessage(from, "Pong! 🏓");
      break;

    // Say it out loud!
    case "echo":
      await client.sendMessage(from, args.join(" "));
      break;

    // Help...
    case "help":
      await client.sendMessage(
        from,
        "Available commands: /ping, /echo [text], /help"
      );
      break;

    default:
      await client.sendMessage(
        from,
        "Unknown command. Type /help for the list of commands."
      );
      break;
  }
};
