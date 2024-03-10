# Doing a clean poetry install

To perform a clean install of your dependencies in a Poetry-managed Python project, you need to first clear out the existing dependencies and the associated virtual environment, and then reinstall the dependencies as specified in your `pyproject.toml` file. Here's how you can do this:

1. **Deactivate the current virtual environment**: If you are inside a Poetry shell (virtual environment), exit it first. You can simply type `exit` in the terminal if you are using Poetry's shell.

2. **Remove the current virtual environment**: Poetry creates a virtual environment for each project. You can remove it using the following command:

   ```
   poetry env remove python
   ```

   This command will remove the virtual environment associated with the current project. Replace `python` with the specific Python version if your project is using a different one.

3. **Clear Poetry Cache (Optional)**: Sometimes, the local cache might cause issues. You can clear it with:

   ```
   poetry cache clear --all pypi
   ```

4. **Delete the `poetry.lock` file**: This file locks your project to specific versions of dependencies. Deleting it will allow Poetry to resolve dependencies afresh:

   ```
   rm poetry.lock
   ```

5. **Install dependencies anew**: Now you can install your dependencies from scratch based on your updated `pyproject.toml` file:

   ```
   poetry install
   ```

   This command will create a new virtual environment and install all the dependencies specified in `pyproject.toml`. It will also create a new `poetry.lock` file locking the project to these specific versions.

6. **Activate the new virtual environment**: Once the installation is complete, you can activate the new virtual environment:

   ```
   poetry shell
   ```
