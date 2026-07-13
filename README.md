# Codex Shark Captain Pet

這是一個獨立於 Rune 與 Rook 的 Codex v2 動畫寵物專案。主角暫名 **Reef**：成熟、壯碩、沉著又可靠的藍色虎鯊獸人船長。

<p align="center">
  <img src="docs/assets/reef-base.png" alt="Reef 鯊魚獸人船長主造型" width="360">
</p>

## 視覺方向

- 白色船長帽、深藍帽簷與黃銅飾帶。
- 深藍虎鯊條紋、淺藍胸腹、背鰭與厚實尾鰭。
- 裸露結實上半身，搭配深藍甲板短褲及低調紅藍格紋。
- 乾淨的 2D cel-shaded 插畫、清楚深色輪廓、冷海洋藍配色。
- 使用相連的船舵、纜繩與望遠鏡表達航海，不使用整艘船或海景背景。

## 動畫規劃

| Codex 狀態 | Reef 的水手動作 |
| --- | --- |
| idle | 穩健海腳站姿、呼吸、眨眼、尾鰭輕擺 |
| running-right / left | 抱著繩圈在甲板方向移動 |
| waving | 船長敬禮後揮手 |
| jumping | 模擬船身起伏的收身甲板跳 |
| failed | 船舵卡住，出力後洩氣 |
| waiting | 抱著繫纜等待下一道命令 |
| running | 雙手交替轉動船舵、專注航行 |
| review | 用黃銅望遠鏡巡視地平線 |

最終資產採 Codex v2 規格：`8 × 11`、每格 `192 × 208`、完整 16 向視線循環。

## 標準動畫預覽

<table>
  <tr><th>待機</th><th>抱繩向右</th><th>抱繩向左</th></tr>
  <tr>
    <td><img src="docs/assets/animations/idle.gif" width="180"></td>
    <td><img src="docs/assets/animations/running-right.gif" width="180"></td>
    <td><img src="docs/assets/animations/running-left.gif" width="180"></td>
  </tr>
  <tr><th>敬禮揮手</th><th>甲板跳</th><th>船舵卡住</th></tr>
  <tr>
    <td><img src="docs/assets/animations/waving.gif" width="180"></td>
    <td><img src="docs/assets/animations/jumping.gif" width="180"></td>
    <td><img src="docs/assets/animations/failed.gif" width="180"></td>
  </tr>
  <tr><th>抱纜待命</th><th>轉舵航行</th><th>望遠鏡巡視</th></tr>
  <tr>
    <td><img src="docs/assets/animations/waiting.gif" width="180"></td>
    <td><img src="docs/assets/animations/running.gif" width="180"></td>
    <td><img src="docs/assets/animations/review.gif" width="180"></td>
  </tr>
</table>

![Reef 九列標準動畫接觸表](docs/assets/standard-contact-sheet.png)

## 目前狀態

- 主造型與九列標準動畫已完成 deterministic frame validation 與獨立視覺 QA。
- 16 向視線語意已建立，但跨列封口仍在修復；在通過前不會把 v2 spritesheet 包裝成可安裝 pet。
- `pet-run/` 保留生成規格與本機工作檔；發布資產只會在完整 v2 驗證通過後加入 plugin。

角色與動作規格位於 [`docs/character-design.md`](docs/character-design.md) 與 [`docs/animation-plan.md`](docs/animation-plan.md)。原始參考圖保存在 `references/source/`。
