**Acceptance criteria (from Ticket-1)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Login with valid email and password | A registered user exists with a known email and password | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Login as a second registered user reaches that user's own account | Two registered users exist (A and B) | 1. Log in as user B with valid credentials. 2. Open the account page. | The account page shows user B's data, not user A's. | positive | AC1 |
| TC-03 | Account locks after the 5th consecutive failed attempt | A registered user exists; account is not locked | 1. Enter the correct email and a wrong password, and submit, 5 times in a row. 2. Enter the correct password and submit. | After the 5th failure the account is locked. The login with the correct password is rejected, and a lock message or the generic error is shown. | boundary | AC2 |
| TC-04 | Account is not locked after 4 failed attempts | A registered user exists; account is not locked | 1. Enter the correct email and a wrong password, and submit, 4 times. 2. Enter the correct password and submit. | Login succeeds. The account is not locked. | boundary | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts less than 15 minutes ago | 1. Wait 15 minutes. 2. Enter the correct email and password. 3. Submit. | Login succeeds. The lock has expired. | boundary | AC2 |
| TC-06 | Wrong password shows generic error | A registered user exists | 1. Enter the correct email and a wrong password. 2. Submit. | An error message such as "Invalid email or password" is shown. It does not say which field is wrong. | negative | AC3 |
| TC-07 | Unregistered email shows the same generic error | No account exists for the email used | 1. Enter an unregistered email and any password. 2. Submit. | The same generic error message as TC-06 is shown. It does not reveal that the email is unregistered. | negative | AC3 |
| TC-08 | Remember me keeps the user logged in for 30 days | A registered user exists | 1. Log in with valid credentials and check "Remember me". 2. Close the browser. 3. Reopen the site on day 29 (or with the session clock set to day 29). | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-09 | Without Remember me the session does not persist | A registered user exists | 1. Log in with valid credentials and leave "Remember me" unchecked. 2. Close the browser. 3. Reopen the site. | User is logged out and must log in again. | negative | AC4 |
| TC-10 | Remember me session expires after 30 days | A registered user exists; login made with "Remember me" checked | 1. Log in with "Remember me" checked. 2. Advance the session clock to day 30 and one minute. 3. Reload the site. | User is logged out and must log in again. | boundary | AC4 |
| TC-11 | Password characters are masked while typing | Login page is open | 1. Click the password field. 2. Type "Secret123". | Each character is displayed as a mask (dot or asterisk), not as plain text. | positive | AC5 |
| TC-12 | Pasted password is masked | Login page is open; a password is copied to the clipboard | 1. Click the password field. 2. Paste the password. | The pasted value is displayed as masked characters. | positive | AC5 |
| TC-13 | Email is accepted regardless of letter case | A registered user exists with a lowercase email | 1. Enter the email in uppercase or mixed case. 2. Enter the correct password. 3. Submit. | Login succeeds. | positive | extra |
| TC-14 | Email with leading and trailing spaces | A registered user exists | 1. Enter " user@example.com " with surrounding spaces. 2. Enter the correct password. 3. Submit. | Login succeeds, or a clear validation error is shown. The behavior is consistent and documented. | boundary | extra |
| TC-15 | Submit with empty email or password is blocked | Login page is open | 1. Leave the email empty and enter a password. 2. Submit. 3. Repeat with the email filled and the password empty. | Form is not submitted. A validation message is shown for the empty field. No failed-attempt count is recorded. | negative | extra |
| TC-16 | Maximum-length password is accepted | A registered user exists whose password is at the maximum allowed length (e.g. 128 characters) | 1. Enter the email. 2. Enter the maximum-length password. 3. Submit. | Login succeeds. | boundary | extra |