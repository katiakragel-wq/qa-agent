**Acceptance criteria (from Ticket-1: Login with email and password)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Valid email and password log the user in | A registered account exists and the user is logged out | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Valid email with wrong password does not log in | A registered account exists and the user is logged out | 1. Open the login page. 2. Enter the registered email. 3. Enter an incorrect password. 4. Click "Log in". | User is not logged in and stays on the login page. | negative | AC1 |
| TC-03 | Account is locked on the 5th failed attempt, not the 4th | A registered account exists and is not locked | 1. Submit a wrong password 4 times. 2. Confirm the account is not locked by logging in with the correct password. 3. Submit a wrong password a 5th time. 4. Try to log in with the correct password. | After 4 failures the correct password still works. After the 5th failure the account is locked and the correct password is rejected. | boundary | AC2 |
| TC-04 | Correct password is rejected while the account is locked | The account has been locked by 5 failed attempts less than 15 minutes ago | 1. Open the login page. 2. Enter the correct email and password. 3. Click "Log in". | Login is refused and a lockout message is shown. The user is not logged in. | negative | AC2 |
| TC-05 | Lock expires after 15 minutes | The account was locked exactly 15 minutes ago | 1. Wait until 15 minutes after the lock started. 2. Enter the correct email and password. 3. Click "Log in". | Login succeeds and the user is logged in. | boundary | AC2 |
| TC-06 | Wrong password shows a generic error message | A registered account exists and is not locked | 1. Enter the registered email. 2. Enter an incorrect password. 3. Click "Log in". | An error such as "Invalid email or password" is shown. The message does not say which field is wrong. | negative | AC3 |
| TC-07 | Unregistered email shows the same generic error message | No account exists for the email used | 1. Enter an unregistered email. 2. Enter any password. 3. Click "Log in". | The same generic error message as TC-06 is shown. It does not reveal that the email is unknown. | negative | AC3 |
| TC-08 | Remember me keeps the user logged in after closing the browser | A registered account exists and the user is logged out | 1. Log in with valid credentials and check "Remember me". 2. Close the browser completely. 3. Reopen the browser and go to the application. | User is still logged in without entering credentials. | positive | AC4 |
| TC-09 | Remember me session expires after 30 days | User logged in with "Remember me" checked, 30 days ago | 1. Reopen the application 30 days after login. | The session has expired and the user must log in again. | boundary | AC4 |
| TC-10 | Session is not kept when Remember me is unchecked | A registered account exists and the user is logged out | 1. Log in with valid credentials and leave "Remember me" unchecked. 2. Close the browser completely. 3. Reopen the browser and go to the application. | User is asked to log in again. | negative | AC4 |
| TC-11 | Password characters are masked on entry | The login page is open | 1. Click in the password field. 2. Type a password. | Each typed character is displayed as a mask (for example a dot or asterisk), not as plain text. | positive | AC5 |
| TC-12 | Pasted long password is fully masked | The login page is open and a password of 128 characters is copied | 1. Click in the password field. 2. Paste the 128-character password. | All 128 characters are displayed as masked characters. None are shown in plain text. | boundary | AC5 |
| TC-13 | Login with an email at maximum length (254 characters) | A registered account exists with a 254-character email, and the user is logged out | 1. Enter the 254-character email. 2. Enter the correct password. 3. Click "Log in". | Login succeeds and the user is logged in. | boundary | extra |
| TC-14 | SQL injection string in email field is rejected safely | The login page is open | 1. Enter `' OR '1'='1` in the email field. 2. Enter any password. 3. Click "Log in". | Login is refused with the generic error message. No database error is shown and the user is not logged in. | negative | extra |
| TC-15 | Submitting empty email and password is blocked | The login page is open | 1. Leave the email and password fields empty. 2. Click "Log in". | Form validation prevents submission and asks the user to fill in both fields. No login request succeeds. | negative | extra |
| TC-16 | Email is matched regardless of letter case | A registered account exists with the email in lowercase | 1. Enter the email in uppercase or mixed case. 2. Enter the correct password. 3. Click "Log in". | Login succeeds. | positive | extra |

**Coverage check:** AC1 has TC-01, TC-02. AC2 has TC-03, TC-04, TC-05. AC3 has TC-06, TC-07. AC4 has TC-08, TC-09, TC-10. AC5 has TC-11, TC-12. The extra cases are TC-13 to TC-16, which are all positive, negative, or boundary.