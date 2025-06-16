# Test Plan for OpenCart Demo

## 1. Project Overview

This test plan covers functional and non-functional testing of the OpenCart demo website, an e-commerce platform for online shopping. The goal is to ensure that the core functionalities work correctly in various usage scenarios.

## 2. Test Objectives

- Verify core functionalities: registration, login, search, cart, checkout.
- Ensure main processes work properly in normal and error scenarios.
- Evaluate usability and smoothness of the purchase process.

## 3. Scope of Testing

- Included:
  - Registration of new users
  - Login/logout
  - Product search
  - Adding products to the cart
  - Checkout process
  - Appearance and functioning of main pages (homepage, category, product, etc.)
- Excluded:
  - API testing (for now)
  - Advanced security testing
  - Direct database testing

## 4. Test Environment

- Devices: PC or laptop with Windows/macOS/Linux
- Browsers: Google Chrome, Mozilla Firefox (latest versions)
- Tools:
  - Manual Testing: documentation in Markdown on GitHub
  - Automation: Selenium with Python
  - Performance: JMeter

## 5. Types of Testing

- Manual functional testing
- Automated functional testing
- Performance testing (load testing)
- Regression testing (after changes)

## 6. Acceptance Criteria

- All critical test cases should pass without major issues.
- Registration and login functionalities must be stable and work as expected.
- The purchase process should complete successfully.

## 7. Risks and Potential Issues

- High load may impact performance.
- Bugs may appear in the payment and checkout process.
- UI changes might cause difficulties in automated testing.

## 8. Timeline

| Activity            | Deadline |
| ------------------- | -------- |
| Test Plan Creation  | 2 days   |
| Manual Testing      | 4 days   |
| Automation          | 5 days   |
| Performance Testing | 3 days   |
| Final Documentation | 1 day    |

---
