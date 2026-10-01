import sys, asyncio
from playwright.async_api import async_playwright

async def main(pairs):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for src, out in pairs:
            await pg.goto(f"file://{src}")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=out, full_page=False)
        await b.close()

args = sys.argv[1:]
asyncio.run(main(list(zip(args[0::2], args[1::2]))))
