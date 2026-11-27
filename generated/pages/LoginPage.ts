import { Page, Locator, expect } from '@playwright/test';

export const LOGIN_URL = 'https://www.saucedemo.com/';

export class LoginPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly alert: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.getByRole('textbox', { name: 'Username', exact: true });
    this.passwordInput = page.getByRole('textbox', { name: 'Password', exact: true });
    this.loginButton = page.getByRole('button', { name: 'Login', exact: true });
    this.alert = page.getByRole('alert');
  }

  async goto(): Promise<void> {
    await this.page.goto(LOGIN_URL);
  }

  async fillUsername(value: string): Promise<void> {
    await this.usernameInput.fill(value);
  }

  async fillPassword(value: string): Promise<void> {
    await this.passwordInput.fill(value);
  }

  async clickLogin(): Promise<void> {
    await this.loginButton.click();
  }

  async login(username: string, password: string): Promise<void> {
    await this.fillUsername(username);
    await this.fillPassword(password);
    await this.clickLogin();
  }

  async expectErrorMessage(message: string): Promise<void> {
    await expect(this.alert).toContainText(message);
  }

  async expectOnLoginPage(): Promise<void> {
    await expect(this.page).toHaveURL(LOGIN_URL);
    await expect(this.loginButton).toBeVisible();
  }
}
