import nodriver as uc
import asyncio

async def name_scraper(name):
    # Start a new Chrome instance
    driver = await uc.start(browser="firefox", no_sandbox=True)

    # Navigate to Google
    page = await driver.get("https://google.com")

    # Wait for the input field to be available
    input_field = await page.wait_for_selector("#APjFqb")  # Use the proper selector for the Google search input

    if input_field:
        await input_field.fill(name)  # Fill in the input field with the name
        await page.keyboard.press("Enter")  # Press Enter to submit

    # Wait for some time to see the results or handle further actions
    await page.wait_for_timeout(2000)  # Adjust this timeout as needed

    # Close the page and the driver
    await page.close()
    await driver.close()  # Properly close the driver

def go(name):
    asyncio.run(name_scraper(name))

go("Nodriver tutorial")
