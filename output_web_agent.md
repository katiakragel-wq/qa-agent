```typescript
// pages/LoginPage.ts
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

// pages/InventoryPage.ts
import { Page, Locator, expect } from '@playwright/test';

export const INVENTORY_URL = 'https://www.saucedemo.com/inventory.html';

export const PRODUCT_NAMES = [
  'Sauce Labs Backpack',
  'Sauce Labs Bike Light',
  'Sauce Labs Bolt T-Shirt',
  'Sauce Labs Fleece Jacket',
  'Sauce Labs Onesie',
  'Test.allTheThings() T-Shirt (Red)',
];

export class InventoryPage {
  readonly page: Page;
  readonly heading: Locator;
  readonly sortCombobox: Locator;
  readonly cartButton: Locator;
  readonly addToCartButtons: Locator;

  constructor(page: Page) {
    this.page = page;
    this.heading = page.getByRole('heading', { name: 'Products', exact: true });
    this.sortCombobox = page.getByRole('combobox', { name: 'Sort products', exact: true });
    this.cartButton = page.getByRole('button', { name: 'Cart, empty', exact: true });
    this.addToCartButtons = page.getByRole('button', { name: 'Add to cart', exact: true });
  }

  async expectLoaded(): Promise<void> {
    await expect(this.page).toHaveURL(INVENTORY_URL);
    await expect(this.page).toHaveTitle('Swag Labs');
    await expect(this.heading).toBeVisible();
    await expect(this.sortCombobox).toBeVisible();
    await expect(this.cartButton).toBeVisible();
    await expect(this.addToCartButtons).toHaveCount(PRODUCT_NAMES.length);
    for (const name of PRODUCT_NAMES) {
      await expect(this.page.getByText(name, { exact: true })).toBeVisible();
    }
  }
}

// tests/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage, LOGIN_URL, } from '../pages/LoginPage';
import { InventoryPage, INVENTORY_URL } from '../pages/InventoryPage';

test('TC-01: valid credentials log in and open the inventory page', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const inventoryPage = new InventoryPage(page);

  await loginPage.goto();
  await loginPage.login('standard_user', 'secret_sauce');

  await inventoryPage.expectLoaded();
});

test('TC-02: valid credentials submitted with the Enter key', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const inventoryPage = new InventoryPage(page);

  await loginPage.goto();
  await loginPage.fillUsername('standard_user');
  await loginPage.fillPassword('secret_sauce');
  await loginPage.passwordInput.press('Enter');

  await inventoryPage.expectLoaded();
});

test('TC-03: valid username with wrong password shows mismatch error', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.login('standard_user', 'wrong_password');

  await expect(page).toHaveURL(LOGIN_URL);
  await loginPage.expectErrorMessage(
    'Epic sadface: Username and password do not match any user in this service'
  );
});

test('TC-04: password with different letter case is rejected', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.login('standard_user', 'Secret_Sauce');

  await expect(page).toHaveURL(LOGIN_URL);
  await loginPage.expectErrorMessage(
    'Epic sadface: Username and password do not match any user in this service'
  );
});

test('TC-05: empty username shows username required error', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.fillPassword('secret_sauce');
  await loginPage.clickLogin();

  await loginPage.expectErrorMessage('Epic sadface: Username is required');
  await expect(page).toHaveURL(LOGIN_URL);
});

test('TC-06: both fields empty shows username required error first', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.clickLogin();

  await loginPage.expectErrorMessage('Epic sadface: Username is required');
  await expect(page).toHaveURL(LOGIN_URL);
});

test('TC-07: empty password with username shows password required error', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.fillUsername('standard_user');
  await loginPage.clickLogin();

  await loginPage.expectErrorMessage('Epic sadface: Password is required');
  await expect(page).toHaveURL(LOGIN_URL);
});

test('TC-08: single-character username with empty password shows password required error', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.fillUsername('a');
  await loginPage.clickLogin();

  await loginPage.expectErrorMessage('Epic sadface: Password is required');
  await expect(page).toHaveURL(LOGIN_URL);
});

test('TC-09: locked-out user sees locked-out message', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.login('locked_out_user', 'secret_sauce');

  await loginPage.expectErrorMessage('Epic sadface: Sorry, this user has been locked out.');
  await expect(page).toHaveURL(LOGIN_URL);
  await expect(loginPage.loginButton).toBeVisible();
});

// BLOCKED: the observation run hit the step limit before this case was finished.
// The direct-access redirect from /inventory.html back to the login page and the
// "no catalog shown" outcome were never verified, so no safe assertion can be written.
// Kept as fixme until the case is re-observed.
test.fixme('TC-10: locked-out user has no session after failed login', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.login('locked_out_user', 'secret_sauce');
  await loginPage.expectErrorMessage('Epic sadface: Sorry, this user has been locked out.');

  await page.goto(INVENTORY_URL);
  // Expected (not yet observed): redirect back to the login page, no catalog shown.
  await expect(page).toHaveURL(LOGIN_URL);
});
```