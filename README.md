# Demos Math Library

A shared Java library providing mathematical operations for demo services.

## Overview

This library provides core math functionality that can be used across multiple services. It includes configurable feature toggles to enable/disable operations.

## Features

| Operation | Method | Toggle |
|-----------|--------|--------|
| Addition | `add(int a, int b)` | `additionEnabled` |
| Subtraction | `subtract(int a, int b)` | `subtractionEnabled` |

## Installation

Add to your `pom.xml`:

```xml
<dependency>
    <groupId>com.demos</groupId>
    <artifactId>demos-demo-library</artifactId>
    <version>1.1.0</version>
</dependency>
```

## Usage

```java
import com.demos.math.MathOperations;
import com.demos.math.MathConfig;

// Basic usage
MathOperations math = new MathOperations();
int sum = math.add(5, 3);        // Returns 8
int diff = math.subtract(10, 4); // Returns 6

// With configuration
MathConfig config = new MathConfig();
config.setSubtractionEnabled(true);
```

## Configuration

Services using this library should add these properties to `application.properties`:

```properties
# Feature toggles (all default to false except addition)
math.addition.enabled=true
math.subtraction.enabled=false
```

## Project Structure

```
demos-demo-library/
├── pom.xml
├── src/main/java/com/demos/math/
│   ├── MathOperations.java    # Core math functions
│   └── MathConfig.java        # Feature toggle configuration
└── .github/
    ├── workflows/
    │   └── notify-dependents.yml    # Auto-triggers service updates
    └── PULL_REQUEST_TEMPLATE/
        └── devin_pr_template.md     # PR template for service updates
```

## Automated Service Updates

This repository includes automation that triggers [Devin AI](https://devin.ai) to update dependent services when changes are merged.

### How it works

1. Create a PR with changes and fill out the **Service Update Instructions** in the PR template
2. When merged, GitHub Actions triggers Devin
3. Devin automatically creates PRs in dependent services with:
   - Version bump in `pom.xml`
   - New configuration properties
   - Feature toggles

### Dependent Services

- [demos-demo-service](https://github.com/cogdeasy/demos-demo-service)

## Contributing

When adding new features:

1. Add the operation to `MathOperations.java`
2. Add a feature toggle to `MathConfig.java`
3. Update the version in `pom.xml`
4. Create a PR using the template and fill out **Service Update Instructions**

## Version History

| Version | Changes |
|---------|---------|
| 1.1.0 | Added subtraction operation with feature toggle |
| 1.0.0 | Initial release with addition operation |

## License

MIT
