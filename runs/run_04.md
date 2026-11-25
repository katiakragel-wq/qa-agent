**Acceptance criteria (Ticket-1: Login with email and password)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Login with valid email and password | A registered account exists and is not locked | 1. Open the login page. 2. Enter the registered email and correct password. 3. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Account page is accessible after valid login | A registered account exists and is not locked | 1. Log in with valid credentials. 2. Navigate to the account settings page. | The account page loads and shows the logged-in user's data. | positive | AC1 |
| TC-03 | Account is locked on the 5th consecutive failed attempt | A registered account exists and is not locked | 1. Enter the correct email and a wrong password 5 times in a row. 2. Attempt to log in with the correct password. | After the 5th failure the account is locked, and the login with the correct password is refused. | boundary | AC2 |
| TC-04 | Account is not locked after 4 failed attempts | A registered account exists and is not locked | 1. Enter the correct email and a wrong password 4 times. 2. Log in with the correct password. | No lock is applied. The login with the correct password succeeds. | boundary | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts less than 15 minutes ago | 1. Wait 15 minutes from the lock. 2. Log in with the correct password. | Login succeeds after the lock period ends. | positive | AC2 |
| TC-06 | Login is refused during the 15-minute lock | Account was locked by 5 failed attempts less than 15 minutes ago | 1. Wait 10 minutes. 2. Log in with the correct password. | Login is refused and a lock message is shown. | negative | AC2 |
| TC-07 | Error shown for wrong password with a valid email | A registered account exists and is not locked | 1. Enter the registered email and a wrong password. 2. Click "Log in". | A generic invalid-credentials error is shown and the user is not logged in. | negative | AC3 |
| TC-08 | Same error shown for an unregistered email | No account exists for the email used | 1. Enter an unregistered email and any password. 2. Click "Log in". | The same generic error as for a wrong password is shown. The message does not say the email is unknown. | negative | AC3 |
| TC-09 | "Remember me" keeps the session for 30 days | A registered account exists and is not locked | 1. Log in with valid credentials and check "Remember me". 2. Close the browser. 3. Reopen the app after 1 day and again after 29 days. | The user is still logged in at both checks. | positive | AC4 |
| TC-10 | Session expires after 30 days with "Remember me" | User logged in with "Remember me" checked 30 days earlier | 1. Reopen the app on day 31. | The user is logged out and must log in again. | boundary | AC4 |
| TC-11 | Session ends without "Remember me" | A registered account exists and is not locked | 1. Log in with "Remember me" unchecked. 2. Close the browser and reopen the app the next day. | The user is no longer logged in. | negative | AC4 |
| TC-12 | Password characters are masked while typing | Login page is open | 1. Click in the password field. 2. Type a password. | Each character is shown as a mask symbol, not as plain text. | positive | AC5 |
| TC-13 | Pasted password is also masked | Login page is open and a password is in the clipboard | 1. Click in the password field. 2. Paste the password. | The pasted characters are shown as mask symbols. | negative | AC5 |
| TC-14 | Login with leading and trailing spaces in email | A registered account exists and is not locked | 1. Enter the registered email with a space before and after it. 2. Enter the correct password. 3. Click "Log in". | Login succeeds, or a clear validation message is shown. The result is consistent. | boundary | extra |
| TC-15 | Submitting empty email and password | Login page is open | 1. Leave both fields empty. 2. Click "Log in". | Field validation messages are shown and no login request succeeds. | negative | extra |
| TC-16 | Maximum-length password is accepted | A registered account exists with a password of maximum allowed length (e.g. 128 characters) | 1. Enter the correct long password. 2. Click "Log in". | Login succeeds. | boundary | extra |
| TC-17 | Failed-attempt counter resets after a successful login | A registered account exists and has 4 failed attempts recorded | 1. Log in with the correct password. 2. Log out. 3. Enter 4 wrong passwords. 4. Log in with the correct password. | The account is not locked, because the counter reset on the successful login. | boundary | extra |