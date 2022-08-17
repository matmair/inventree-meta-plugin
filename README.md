# inventree-meta-plugin

Meta project for InvenTree plugins. This repo contains general helpers to streamline InvenTree plugin development.

## Workflow

This keeps the workflows as simple as possible. Just bump the version to get the new flows.

```yaml
name: Plugin checking and building
on:
  push:
    branches: ['main', 'master']
  pull_request:
    types: [opened, edited, reopened]
  release:
    types: [published]

jobs:
  plugin-action:
    uses: matmair/inventree-meta-plugin/.github/workflows/plugin_action.yml@v1.0
   secrets: inherit
```

The workflow runs flake8 and - if a release was published - builds and publishes to PyPi. For this to work you need to set a secret named `PYPI_API_TOKEN` with a valid token for publishing to PyPi.
Please scope the token to only work for the specific project and use a new one for each plugin. You might have to push the project once before the new scope becomes available in the [account settings](https://pypi.org/manage/account/).
