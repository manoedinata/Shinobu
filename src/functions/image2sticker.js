const { MessageMedia } = require("whatsapp-web.js");

async function image2sticker(message, client, args) {
  const { body, from } = message;

  const media = await message.downloadMedia();
  if (!media)
    // Ensure the media is downloaded
    return await client.sendMessage(
      from,
      "Gambar gagal diunduh. Silahkan kirim ulang gambar."
    );
  if (!media.mimetype.startsWith("image"))
    // Only image, buddy!
    return await client.sendMessage(
      from,
      "Maaf, hanya bisa membuat stiker dari gambar."
    );

  return await client.sendMessage(
    from,
    new MessageMedia(media.mimetype, media.data, media.filename ?? ""),
    {
      caption: args ? args.join(" ") : "Shinobu",
      sendMediaAsSticker: true,
      stickerAuthor: "Sticker2Image by Shinobu",
      stickerName: args ? args.join(" ") : "Shinobu",
    }
  );
}

module.exports = image2sticker;
