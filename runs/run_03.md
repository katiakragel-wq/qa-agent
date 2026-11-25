**Acceptance criteria (from Ticket-1)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Log in with valid credentials | A registered user exists with a known email and password | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Log in with a valid email at maximum allowed length | A registered user exists whose email is at the longest length the system accepts (e.g., 254 characters) | 1. Open the login page. 2. Enter the long email. 3. Enter the correct password. 4. Click "Log in". | Login succeeds and the user reaches their account page. | boundary | AC1 |
| TC-03 | Account is not locked after 4 failed attempts | A registered user exists; account is not locked | 1. Attempt login with the correct email and a wrong password 4 times. 2. Log in with the correct password. | The 4 failed attempts show an error each time. The 5th login with the correct password succeeds. | boundary | AC2 |
| TC-04 | Account is locked on the 5th failed attempt | A registered user exists; account is not locked | 1. Attempt login with the correct email and a wrong password 5 times. 2. Immediately log in with the correct password. | After the 5th failure the account is locked. The correct-password login is rejected with a lock message. | boundary | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts less than 15 minutes ago | 1. Wait until 15 minutes have passed since the lock. 2. Log in with the correct password. | Login succeeds. | boundary | AC2 |
| TC-06 | Account stays locked just before 15 minutes | Account was locked by 5 failed attempts 14 minutes 59 seconds ago | 1. Attempt login with the correct password. | Login is rejected with a lock message. | boundary | AC2 |
| TC-07 | Wrong password shows generic error | A registered user exists | 1. Enter the correct email and a wrong password. 2. Click "Log in". | An error such as "Invalid email or password" is shown. The message does not say which field is wrong. | negative | AC3 |
| TC-08 | Unknown email shows the same generic error | No account exists for the email used | 1. Enter an unregistered email and any password. 2. Click "Log in". | The same generic error as TC-07 is shown. It does not say the email is unknown. | negative | AC3 |
| TC-09 | Remember me keeps the user logged in after browser restart | A registered user exists; user is logged out | 1. Log in with valid credentials and "Remember me" checked. 2. Close and reopen the browser. 3. Open the account page. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-10 | Session expires after 30 days with Remember me | User logged in with "Remember me" checked 30 days ago | 1. Open the account page 30 days and 1 minute after login. | User is logged out and asked to log in again. | boundary | AC4 |
| TC-11 | Session without Remember me does not persist | A registered user exists; user is logged out | 1. Log in with "Remember me" unchecked. 2. Close and reopen the browser. 3. Open the account page. | User is required to log in again. | negative | AC4 |
| TC-12 | Password is masked while typing | User is on the login page | 1. Click into the password field. 2. Type "Secret123". | Characters are displayed as masked symbols (dots or asterisks), not as plain text. | positive | AC5 |
| TC-13 | Pasted password is also masked | User is on the login page; password is copied to the clipboard | 1. Click into the password field. 2. Paste the password. | The pasted characters are displayed masked, not as plain text. | boundary | AC5 |
| TC-14 | SQL injection in the email field is rejected safely | User is on the login page | 1. Enter `' OR '1'='1` in the email field. 2. Enter any password. 3. Click "Log in". | Login is rejected with the generic error. No account data is exposed and no server error appears. | negative | extra |
| TC-15 | Maximum-length password is accepted | A registered user exists with a password at the longest length the system allows (e.g., 128 characters) | 1. Enter the correct email. 2. Enter the full-length correct password. 3. Click "Log in". | Login succeeds. | boundary | extra |
| TC-16 | Submitting empty fields is blocked | User is on the login page | 1. Leave email and password empty. 2. Click "Log in". | Login is not attempted. Validation messages are shown for the empty fields. | negative | extra |
| TC-17 | Successful login resets the failed-attempt counter | A registered user exists; 4 failed attempts have been made | 1. Log in with the correct password. 2. Log out. 3. Make 4 more failed attempts. | The account is not locked after the 4 new failures, because the counter was reset on successful login. | boundary | extra |