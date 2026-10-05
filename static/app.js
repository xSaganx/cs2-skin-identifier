body {
  margin: 0;
  background: linear-gradient(135deg, #0d1117, #161b22);
  color: white;
  font-family: Arial, sans-serif;
}

.container {
  max-width: 900px;
  margin: 48px auto;
  padding: 24px;
}

h1 {
  font-size: 2.8rem;
  margin-bottom: 8px;
}

.subtitle {
  color: #c7d1dc;
  margin-bottom: 28px;
}

#upload-form {
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.upload-box {
  display: inline-block;
  background: #21262d;
  border: 2px dashed #4d8df8;
  border-radius: 12px;
  padding: 18px 22px;
  cursor: pointer;
  min-width: 220px;
  text-align: center;
}

.upload-box input {
  display: none;
}

button {
  background: #238636;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 14px 22px;
  cursor: pointer;
  font-weight: bold;
}

button:hover {
  background: #2ea043;
}

#preview-wrap {
  margin-top: 20px;
}

#preview {
  max-width: 420px;
  max-height: 320px;
  border-radius: 12px;
  border: 1px solid #30363d;
}

.result,
.alternatives {
  margin-top: 24px;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 12px;
  padding: 20px;
}

.hidden {
  display: none;
}

#match-list {
  padding-left: 18px;
  color: #d5dde8;
}

#match-list li {
  margin-bottom: 8px;
}
