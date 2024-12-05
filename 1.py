from playwright.sync_api import sync_playwright
import pytest
def login(page):
    page.goto("https://animated-gingersnap-8cf7f2.netlify.app/")

    email_input = page.locator('input[autocomplete="username"]')
    password_input = page.locator('input[autocomplete="current-password"]')

    email_input.fill("admin")
    password_input.fill("password123")

    submit_button = page.locator('button[type="submit"]')
    submit_button.click()

    page.wait_for_load_state("load")


def test_case_1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        button = page.locator('button.bg-gray-700')
        button.wait_for(state='visible')
        button.click()

        todo_column = page.locator('.p-4', has_text='To Do')
        todo_column.wait_for(state='visible')
        assert todo_column.is_visible(), "'To Do' column is not visible"

        task = page.locator('h3.font-medium', has_text="Implement user authentication")
        task.wait_for(state='visible')
        task_is_present = task.is_visible()
        assert task_is_present, "'Implement user authentication' task is not in 'To Do' column"

        feature_tag = page.locator('.px-2', has_text='Feature').nth(0)
        feature_tag_is_visible = feature_tag.is_visible()

        assert feature_tag_is_visible, "'Feature' tag is not visible in task"

        high_priority_tag = page.locator('.px-2', has_text= 'High Priority').nth(0)
        high_priority_tag_is_visible = high_priority_tag.is_visible()

        assert high_priority_tag_is_visible, "'High Priority' tag is not visible in task"

        browser.close()


def test_case_2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        button = page.locator('button.bg-gray-700')
        button.wait_for(state='visible')
        button.click()

        todo_column = page.locator('.p-4', has_text='To Do')
        todo_column.wait_for(state='visible')

        task = page.locator('h3.font-medium', has_text='Fix navigation bug')
        task_is_present = task.is_visible()
        assert task_is_present, "'Fix navigation bug' task is not in 'To Do' column"

        bug_tag = page.locator('.px-2', has_text='Bug')
        bug_tag.wait_for(state='visible')
        bug_tag_is_visible = bug_tag.is_visible()

        assert bug_tag_is_visible, "'Bug' tag is not visible in task"

        browser.close()


def test_case_3():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        page.locator('button.bg-gray-700').click()

        page.locator('h2', has_text='In Progress').wait_for(state='visible')

        task = page.locator('h3.font-medium',has_text='Design system updates')
        task.wait_for(state='visible')
        task_is_present = task.is_visible()
        assert task_is_present, "'Design system updates' task is not in 'In Progress' column"

        design_tag = page.locator('.px-2', has_text='Design')
        design_tag.wait_for(state='visible')
        design_tag_is_visible = design_tag.is_visible()

        assert design_tag_is_visible, "'Design' tag is not visible in task"

        browser.close()


def test_case_4():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        page.locator('h2.font-medium', has_text='Mobile Application').click()

        page.locator('h2', has_text='To Do').wait_for(state='visible')

        task = page.locator('h3.font-medium', has_text='Push notification system')
        task_is_present = task.is_visible()
        assert task_is_present, "'Push notification system' task is not in 'To Do' column"


        feature_tag = page.locator('.px-2', has_text='Feature').nth(1)
        feature_tag.wait_for(state='visible')
        feature_tag_is_visible = feature_tag.is_visible()

        assert feature_tag_is_visible, "'Feature' tag is not visible in task"

        browser.close()

# Test Case 5: Verify task "Offline mode" in "In Progress" column under "Mobile Application"
def test_case_5():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        page.locator('h2.font-medium', has_text='Mobile Application').click()

        page.locator('h2', has_text='In Progress').wait_for(state='visible')

        task = page.locator('h3.font-medium', has_text='Offline mode')
        task_is_present = task.is_visible()
        assert task_is_present, "'Offline mode' task is not in 'In Progress' column"

        feature_tag = page.locator('.px-2', has_text='Feature').nth(0)
        feature_tag.wait_for(state='visible')
        feature_tag_is_visible = feature_tag.is_visible()

        assert feature_tag_is_visible, "'Feature' tag is not visible in task"

        high_priority_tag = page.locator('.px-2', has_text='High Priority')
        high_priority_tag_is_visible = high_priority_tag.is_visible()

        assert high_priority_tag_is_visible, "'High Priority' tag is not visible in task"

        browser.close()


def test_case_6():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        page.locator('h2.font-medium', has_text='Mobile Application').click()

        page.locator('h2', has_text='Done').wait_for(state='visible')

        task = page.locator('h3.font-medium', has_text='App icon design')
        task_is_present = task.is_visible()
        assert task_is_present, "'App icon design' task is not in 'Done' column"

        design_tag = page.locator('.px-2', has_text='Design')
        design_tag.wait_for(state='visible')
        design_tag_is_visible = design_tag.is_visible()

        browser.close()

