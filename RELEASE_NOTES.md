# Release Notes

## Version 1.3.0
**Release Date:** 2026-02-19

### New Features
- `divide(int a, int b)` - Division operation returning double
- `divisionEnabled` feature toggle (default: false)

### Breaking Changes
None

### Services to Update
<!-- Add service names here when ready for them to be updated -->
<!-- Example: cogdeasy/demos-demo-service, cogdeasy/demos-demo-service-2 -->
- cogdeasy/demos-demo-service
- cogdeasy/demos-demo-service-2

### Update Notes
Services should add a `/divide` endpoint that:
- Returns double (not int)
- Handles ArithmeticException → HTTP 400 "Division by zero"

---

## Version 1.2.0
**Release Date:** 2026-02-19

### New Features
- `multiply(int a, int b)` - Multiplication operation
- `multiplicationEnabled` feature toggle (default: false)

### Services to Update
- cogdeasy/demos-demo-service
- cogdeasy/demos-demo-service-2

### Update Notes
Add `/multiply` endpoint gated by feature toggle.

---

## Version 1.1.0
**Release Date:** 2026-02-18

### New Features
- `subtract(int a, int b)` - Subtraction operation
- `subtractionEnabled` feature toggle (default: false)

### Services to Update
- cogdeasy/demos-demo-service

### Update Notes
Add `/subtract` endpoint gated by feature toggle.
