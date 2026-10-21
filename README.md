# PDF Tools

Free PDF tools: PDF to Word, Scan to Word (OCR), Merge, Split, Compress, Rotate, Watermark, Page numbers, JPG to PDF, PDF to JPG.

## Files
- index.html : poori site (browser mein chalti hai)
- server.py, requirements.txt, render.yaml : asli layout wala PDF to Word + site hosting

## Raasta A: sirf GitHub Pages (aasaan)
1. GitHub par repo banao, saari files upload karo.
2. Settings > Pages > Branch main, folder / (root) > Save.
3. Site: username.github.io/repo-name
PDF to Word mein text aur formatting aayegi, tables/images nahi.

## Raasta B: asli layout (Render par, free)
1. Same repo ko render.com se jodo: New > Blueprint > repo chuno (render.yaml apne aap padh lega).
2. Deploy hone par Render ka URL milega, jaise https://pdf-tools.onrender.com
3. Wo URL seedha site ki tarah khulta hai, aur PDF to Word asli layout (tables, columns, images) se hota hai.
4. Agar site GitHub Pages par hi rakhni hai: site ke upar Server settings mein Render ka URL daalo.

Free Render server idle hone par so jaata hai, pehli request mein ~1 minute lag sakta hai. File limit 30 MB.
