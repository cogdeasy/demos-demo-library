# Library Service Update Playbook

This playbook is triggered by a scheduler to check for library updates and create PRs in dependent services.

## Instructions

1. **Check Release Notes**
   - Clone `cogdeasy/demos-demo-library`
   - Read `RELEASE_NOTES.md` to find the latest version
   - Look at the "Services to Update" section - ONLY update services listed there
   - If no services are listed, do nothing and report "No services to update"

2. **For Each Service Listed**
   - Check if the service already has a PR for this version (skip if yes)
   - Read `.devin/service-update-template.md` for update instructions
   - Clone the service repo
   - Detect project type (pom.xml = Java, requirements.txt = Python)
   - Apply updates following the template

3. **Create PR**
   - Title: `chore: bump demos-demo-library to <version>`
   - Body must include:
     - Version being updated to
     - Summary of changes from release notes
     - List of files modified
     - Reference to library release notes

4. **Report Results**
   - List all PRs created
   - List any services skipped (already up to date)
   - List any errors encountered

## Important

- **Only update services explicitly listed in RELEASE_NOTES.md "Services to Update" section**
- Do NOT update services that are not listed
- This gives humans control over which services get updated and when
