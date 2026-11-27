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
