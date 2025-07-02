### Text-to-Image_lyR4 Model (by daffa)

Model ini digunakan untuk mengubah teks menjadi gambar secara otomatis, cocok untuk keperluan seperti **AI Storybook**, visualisasi narasi, dan kebutuhan kreatif lainnya.

---

### Push Model

```bash
cog login
cog push r8.im/<your-username>/<your-model-name>
```

jalankan di node.js
```bash
npx create-replicate --model=daffadevhosting/text-to-img_lyra
```

Install Replicate’s Node.js client library
```bash
npm install replicate
```

Set REPLICATE_API_TOKEN
```bash
export REPLICATE_API_TOKEN=r8_3**********************
```

Import dan set up client
```js
import Replicate from "replicate";
import fs from "node:fs";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});
```

Jalankan `daffadevhosting/text-to-img_lyra` menggunakan API Replicate.
```js
const output = await replicate.run(
  "daffadevhosting/text-to-img_lyra:7c54a0f4c2032d1948ccb0d9e9c3f16898--------------",
  {
    input: {}
  }
);

// Untuk akses file URL:
console.log(output.url()); //=> "http://example.com"

// Menulis file ke disk:
fs.writeFile("my-image.png", output);
```

🖼️ Output

Model akan menghasilkan 1 gambar (output.png) yang otomatis diunggah oleh Replicate dan dikembalikan sebagai URL publik.


---

💬 Dukungan

Model ini dibuat untuk digunakan bersama Lyra Storybook.
Silakan forking, remix, atau request fitur tambahan via issue.


---

⚠️ Lisensi

Model ini menggunakan runwayml/stable-diffusion-v1-5 di bawah lisensi CreativeML Open RAIL-M.
Penggunaan untuk konten eksplisit atau ilegal dilarang.


---

> Dibuat dengan ✨ oleh Daffa & nDang
