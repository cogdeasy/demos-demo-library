# Library Service Update Playbook

This playbook is triggered by a scheduler to check for library updates and create PRs in dependent services.

## Prerequisites

- This playbook runs in the context of the library repository (already available)
- You have access to `devinwiki` which contains knowledge about dependent services

## Instructions

### Step 1: Discover Dependent Services

Query `devinwiki` to find all services that depend on this library:
- Search for services using `demos-demo-library`
- This gives you the current list of dependent services at runtime
- Do not rely on hardcoded service lists

### Step 2: Check Release Notes

- Read `RELEASE_NOTES.md` to find the latest version
- Look at the "Services to Update" section
- Cross-reference with services discovered from devinwiki
- ONLY update services that appear in BOTH:
  1. The devinwiki (confirmed dependents)
  2. The "Services to Update" section (human-approved for update)
- If no services match, report "No services to update"

### Step 3: Read Update Template

- Read `.devin/service-update-template.md` for language-specific instructions
- This template defines how to update Java vs Python services

### Step 4: For Each Approved Service

- Check if the service already has a PR for this version (skip if yes)
- Clone the service repo
- Detect project type (pom.xml = Java, requirements.txt = Python)
- Apply updates following the template

### Step 5: Create PR

- Title: `chore: bump demos-demo-library to <version>`
- Body must include:
  - Version being updated to
  - Summary of changes from release notes
  - List of files modified
  - Reference to library release notes

### Step 6: Report Results

- List all PRs created
- List services skipped (already up to date)
- List services in devinwiki but not approved for update
- List any errors encountered

## Important

- **Query devinwiki first** to get the authoritative list of dependent services
- **Only update services explicitly listed in RELEASE_NOTES.md "Services to Update" section**
- The intersection of devinwiki dependents AND approved services determines what gets updated
- This gives humans control while ensuring we only update actual dependents
