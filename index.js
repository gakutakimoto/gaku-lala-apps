const express = require('express');
const path = require('path');
const app = express();

// 静的ファイル（HTML, CSS, JS）を `public` フォルダから配信
app.use(express.static(path.join(__dirname, 'public')));

// ルート (`/`) にアクセスしたら `index.html` を返す
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
