# Visual style guide: Pratik P Sahoo LinkedIn posts

Every image or video made for a post follows these rules.

## How to build images (preferred: HTML + headless Chromium)
Build each image as a 1080x1350 HTML page and screenshot it. This gives magazine-quality typography.
1. `cd design && npm init -y && npm i @fontsource/inter @fontsource/anton @fontsource/space-grotesk @fontsource/dm-serif-display`
2. Copy the closest template (`eight-weeks.html` = dark stat grid, `rbi.html` = navy header + bar chart + option cards, `trade.html` = light timeline + "My view" banner). All link `base.css`.
3. Render: `python3 render.py $PWD/my.html $PWD/my.png` (Playwright + Chromium are preinstalled; never run `playwright install`).
4. Open the PNG and check for overflow, overlap or empty space before uploading.
Design moves that work: one giant hero number or headline (Anton), a coloured pill tag for the theme, icon chips, big stat numbers (Space Grotesk), a strong closing card ("Which one turns first?" or "My view"), the PS monogram signature. Use the ₹ sign via the `.rs` class.

## Format
- Image: 1080 x 1350 px PNG (4:5 portrait, best reach in the LinkedIn feed).
- Video: 1080 x 1350 or 1080 x 1920, H.264 MP4, yuv420p, `-movflags +faststart`.
- Save to `posts/YYYY-MM-DD/<short-slug>.png|mp4` (date = scheduled post date).
- Public link format: `https://raw.githubusercontent.com/Pratik-Sahoo1/linkedin-media/main/posts/YYYY-MM-DD/<file>`

## Look
- Default: clean, light. Background `#fcfcfb`, primary text `#0b0b0b`, secondary text `#52514e`, muted `#8a8984`, rules `#e4e3df`.
- Dark variant only when the topic suits it (markets at night, crisis, drama): background `#1a1a19`, text `#ffffff` / `#c3c2b7`.
- Data colours, in this fixed order (light / dark):
  1. blue `#2a78d6` / `#3987e5`
  2. orange `#eb6834` / `#d95926`
  3. aqua `#1baf7a` / `#199e70`
  4. yellow `#eda100` / `#c98500`
- Up/down in market visuals: green `#0ca30c` (up) and red `#e34948` (down), always paired with a + / - sign or arrow, never colour alone.
- Font: DejaVu Sans (installed). Big bold headline at the top (2 lines max, ~50pt), one-line subtitle, generous 80 px side margins.
- Footer: left = source or "Illustrative numbers" note in muted text; right = **Pratik P Sahoo** in bold secondary text.

## Content rules
- One idea per visual. The headline should make someone stop scrolling.
- Only numbers that also appear in the post text and were verified. No invented data.
- Charts: thin bars with small rounded ends, direct value labels, a legend when there are 2+ series, no dual axes, no 3D, no clutter.
- Never use logos, brand marks, or copyrighted images. Stock photos only from Unsplash or Pexels (free licence), credited in the sheet.
- Check the rendered image for text overflow or overlap before uploading.
