"""Visit the three lab apps with a real browser so Streamlit Community Cloud
never hibernates them. A plain HTTP GET returns 200 but does not count as
viewer activity; only a browser session does. If an app is already asleep,
click Streamlit's "Yes, get this app back up!" button and wait for boot.
"""
import sys

from playwright.sync_api import sync_playwright

APPS = (
    "https://beforeyouship.streamlit.app/",
    "https://testarchitect.streamlit.app/",
    "https://metricready.streamlit.app/",
)

WAKE_BUTTON_TEXT = "get this app back up"
STREAMLIT_APP_SELECTOR = '[data-testid="stApp"]'


def visit(page, url: str) -> None:
    page.goto(url, wait_until="load", timeout=120_000)
    page.wait_for_timeout(10_000)  # let the SPA shell settle
    wake = page.get_by_text(WAKE_BUTTON_TEXT, exact=False)
    if wake.count() > 0:
        print(f"{url}: asleep - clicking the wake button")
        wake.first.click()
        page.wait_for_timeout(90_000)  # give the container time to boot
    page.wait_for_timeout(20_000)  # hold the session so the visit registers
    # Confirm the app actually came up rather than trusting the sleep above:
    # a still-asleep or broken-render app must fail the job, not report OK.
    if wake.count() > 0:
        raise RuntimeError(f"{url}: still showing the wake button after waiting")
    page.wait_for_selector(STREAMLIT_APP_SELECTOR, timeout=15_000)
    print(f"{url}: OK")


def main() -> int:
    failures: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for url in APPS:
            page = browser.new_page()
            try:
                visit(page, url)
            except Exception as exc:  # report and continue to the next app
                print(f"{url}: FAILED - {exc}", file=sys.stderr)
                failures.append(url)
            finally:
                page.close()
        browser.close()
    if failures:
        print(f"{len(failures)} app(s) unreachable: {', '.join(failures)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
