import random
import string
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage


def generate_random_username():
    """生成随机用户名，避免和之前测试跑过的用户名重复"""
    return "jora_test_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


def test_register_and_login_success(page):
    """
    场景：新用户注册成功后，用刚注册的账号密码登录，应成功进入账户总览页
    技术：等价类划分 — 有效分区（正确的用户名+密码组合）
    """
    username = generate_random_username()
    password = "TestPass123"

    register_page = RegisterPage(page)
    register_page.goto()
    register_page.register_new_user(username, password)
    assert page.locator("#rightPanel h1.title").is_visible(), "注册成功后应显示欢迎标题"
    assert "created successfully" in page.locator("#rightPanel").text_content(), "注册应成功"

    login_page = LoginPage(page)
    login_page.logout()
    login_page.goto()
    login_page.login(username, password)
    assert "overview.htm" in page.url, f"登录后应跳转到账户总览页，实际URL：{page.url}"
    assert page.locator("#leftPanel").is_visible(), "登录后左侧账户面板应可见"


def test_login_with_wrong_password_fails(page):
    """
    场景：使用不存在的用户名登录，应登录失败并显示错误提示
    技术：等价类划分 — 无效分区（错误的用户名+密码组合）
    """
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("nonexistent_user_xyz", "wrongpassword")
    assert "overview.htm" not in page.url, "错误凭证不应登录成功"
    assert page.locator(".error").is_visible(), "应显示错误提示信息"