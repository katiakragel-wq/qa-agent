**Acceptance criteria (from Ticket-1: Login with email and password)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Log in with valid credentials | A registered account exists with a known email and password | 1) Open the login page. 2) Enter the registered email. 3) Enter the correct password. 4) Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Log in with an unregistered email is rejected | No account exists for the email used | 1) Open the login page. 2) Enter an unregistered email and any password. 3) Click "Log in". | Login fails. User is not logged in. | negative | AC1 |
| TC-03 | Four failed attempts do not lock the account | A registered account exists and is not locked | 1) Enter the correct email and a wrong password, and submit 4 times. 2) Enter the correct password and submit. | The first 4 attempts fail. The 5th attempt with the correct password succeeds and the user is logged in. | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account | A registered account exists and is not locked | 1) Enter the correct email and a wrong password, and submit 5 times. 2) Enter the correct password and submit. | After the 5th failure the account is locked. The login with the correct password is refused with a lock message. | positive | AC2 |
| TC-05 | Lock expires after 15 minutes | Account was locked by 5 failed attempts at time T | 1) Wait until T + 15 minutes. 2) Enter the correct email and password. 3) Click "Log in". | Login succeeds after the lock expires. | boundary | AC2 |
| TC-06 | Wrong password shows generic error | A registered account exists and is not locked | 1) Enter a valid registered email and a wrong password. 2) Click "Log in". | An error such as "Invalid email or password" is shown. The message does not say which field is wrong. | negative | AC3 |
| TC-07 | Unknown email shows the same generic error | No account exists for the email used | 1) Enter an unregistered email and any password. 2) Click "Log in". 3) Compare the message with the one from a wrong password. | The same generic error message is shown as for a wrong password. It does not reveal that the email is unknown. | negative | AC3 |
| TC-08 | Remember me keeps the session after browser restart | A registered account exists | 1) Log in with "Remember me" checked. 2) Close and reopen the browser. 3) Open the account page. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-09 | Remember me session expires after 30 days | User logged in with "Remember me" checked on day 0 | 1) Advance the clock to day 30 plus 1 minute. 2) Open the account page. | The session has expired and the user is asked to log in again. | boundary | AC4 |
| TC-10 | Session without "Remember me" does not persist | A registered account exists | 1) Log in with "Remember me" unchecked. 2) Close and reopen the browser. 3) Open the account page. | User is no longer logged in and must log in again. | negative | AC4 |
| TC-11 | Typed password is masked | User is on the login page | 1) Click the password field. 2) Type a password. | Characters are displayed as masked dots or asterisks, not as plain text. | positive | AC5 |
| TC-12 | Pasted password is masked | User is on the login page and has a password in the clipboard | 1) Click the password field. 2) Paste the password. | The pasted value is masked in the same way as typed input. | negative | AC5 |
| TC-13 | Empty email and password are rejected | User is on the login page | 1) Leave email and password empty. 2) Click "Log in". | Validation message is shown. No login request is sent and the user is not logged in. | negative | extra |
| TC-14 | Email is matched case-insensitively | A registered account exists with email "user@example.com" | 1) Enter "USER@Example.com" and the correct password. 2) Click "Log in". | Login succeeds, assuming the system treats emails case-insensitively. | positive | extra |
| TC-15 | SQL injection in email field is rejected safely | User is on the login page | 1) Enter `' OR '1'='1` in the email field and any password. 2) Click "Log in". | Login fails. No database error is shown and the user is not logged in. | negative | extra |
| TC-16 | Failed-attempt counter resets after successful login | A registered account exists and is not locked | 1) Fail 4 times. 2) Log in successfully. 3) Fail 4 more times. 4) Log in with the correct password. | The account is not locked at any point. The final login succeeds. | boundary | extra |