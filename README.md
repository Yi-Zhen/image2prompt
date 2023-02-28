# image2prompt

### Step 1 開啟虛擬環境
在image2prompt目錄下
```
i2p\Scripts\activate
```

### Step 2 建立環境變數
```
$env:REPLICATE_API_TOKEN = 'API'
```

### Step 3 打開Port
```
Windows Defender 防火牆
進階設定
輸入規則
```

### Step 4 Run Server
在i2p_site目錄下
```
python manage.py runserver 0.0.0.0:port
```

### Step 5 別人連線
```
cmd ipconfig (192.168.x.x)
192.168.x.x: port
```
