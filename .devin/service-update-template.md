# Service Update Template

When updating dependent services for this library, follow these instructions.

## General Rules

1. Always update the library version first
2. Add new feature toggles as DISABLED by default
3. New endpoints should check the feature toggle before executing
4. All new operations need proper error handling

## Java/Maven Services (pom.xml detected)

### Version Update
- Update `<version>` tag for `demos-demo-library` in pom.xml

### Feature Toggles
- Add to `src/main/resources/application.properties`:
  ```
  math.<operation>.enabled=false
  ```

### New Endpoints
- Add to the controller class (e.g., `MathController.java`)
- Use `@PostMapping("/<operation>")`
- Check feature toggle before executing
- Return appropriate HTTP status codes

### Error Handling
- `ArithmeticException` → HTTP 400 with message "Division by zero"
- Other exceptions → HTTP 500

### Verification
- Run `mvn compile` to verify changes

## Python/FastAPI Services (requirements.txt detected)

### Version Update
- Update `library_version` in `app/config.py`

### Feature Toggles
- Add to `Settings` class in `app/config.py`:
  ```python
  <operation>_enabled: bool = False
  ```
- Add to `.env.example`:
  ```
  <OPERATION>_ENABLED=false
  ```

### New Endpoints
- Add to `app/main.py`
- Use `@app.post("/<operation>")`
- Check `settings.<operation>_enabled` before executing
- Return appropriate HTTP status codes

### Error Handling
- `ZeroDivisionError` → HTTP 400 with message "Division by zero"
- Other exceptions → HTTP 500

### Verification
- Check syntax with `python -m py_compile app/main.py`

## PR Requirements

- Title: `chore: bump demos-demo-library to <version>`
- Description must list all changes made
- Reference the library PR that triggered the update
