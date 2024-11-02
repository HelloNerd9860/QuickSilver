import nodriver as uc
import asyncio

async def name_scraper(name):
    # Start a new Firefox instance with specific arguments
    driver = await uc.start(
        browser="firefox",
        executable_path="/usr/bin/firefox",  # Make sure to specify the path to Firefox
        no_sandbox=True,
        headless=False,  # Open in non-headless mode if you want to see the UI
        args=[
            "--private-window",  # Example argument to start in private mode
            "--disable-gpu"  # Example argument to disable GPU acceleration
        ]
    )

    # Navigate to Google
    page = await driver.get("https://google.com")

    signed_out = await page.query_selector(".M6CB1crr4y5c")
    signed_out.click()

    # Try selecting the search input field
    input_field = await page.query_selector("#input")  # Google search input selector

    if input_field:
        await input_field.fill(name)  # Fill in the input field with the name
        await page.keyboard.press("Enter")  # Press Enter to submit

    # Use asyncio.sleep for a delay instead of wait_for_timeout
    await asyncio.sleep(200)  # Adjust this timeout as needed

    # Close the page and the driver
    await driver.close()  # Properly close the driver

def go(name):
    asyncio.run(name_scraper(name))

go("Nodriver tutorial")
