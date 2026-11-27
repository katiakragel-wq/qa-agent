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
    this.heading = page.getByText('Products', { exact: true });
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
