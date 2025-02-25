const express = require('express');
const path = require('path');
const app = express();

// 静的ファイル（HTML, CSS, JS）を公開
app.use(express.static(__dirname));  

// ホームページを表示
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
