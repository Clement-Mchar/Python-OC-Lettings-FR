Deployment
===========

The deployment of the application is automated using GitHub Actions. The workflow file located in the `.github/workflows` directory defines the deployment process.

Creating a Web Service on Render
--------------------------------

1. Log in to your Render account.
2. Navigate to your dashboard and click on "New > Web Service" to create a new service.
3. Connect your repository and configure the following settings:
   - **Start Command**: `gunicorn oc_lettings_site.wsgi`
   - **Instance Type**: Free
   - **Auto-Deploy**: No (set this in the "Advanced" settings).
4. Deploy the service manually.
5. Add the Render service address to `ALLOWED_HOSTS` in your `settings.py` file.

Configuring Sentry
-------------------

1. Create a Sentry project and select Django as the platform.
2. Obtain the Sentry DSN and set it as the `SENTRY_KEY_URL` in your `.env` file.

Setting Up GitHub Actions Secrets
----------------------------------

1. Go to the repository's "Settings" on GitHub.
2. In the "General" tab, rename the main branch to `master`.
3. Navigate to "Secrets and Variables > Actions > New repository secret" and add the following secrets:
   * `DOCKER_USERNAME`: Your Docker Hub username.
   * `DOCKER_PASSWORD`: Your Docker Hub password.
   * `RENDER_DEPLOY_HOOK`: The deployment hook URL from Render settings.
   * `SECRET_KEY`: Your Django secret key from the `.env` file.
   * `SENTRY_KEY_URL`: The Sentry DSN from your `.env` file.

Deployment Process
-------------------

The deployment process consists of multiple stages:

1. **Tests and Coverage**: This stage runs on the `ubuntu-latest` environment. It installs dependencies, runs linting checks with Flake8, and executes tests using Pytest while generating a coverage report. The coverage report is uploaded as an artifact.
   
2. **Build Docker Image**: After the tests pass, this stage builds the Docker image. The image is built using Docker Compose and includes the `SECRET_KEY` and `SENTRY_KEY_URL` as build arguments. Once built, the image is pushed to Docker Hub.

3. **Deploy Image to Render**: If the image is successfully built, it is deployed to Render. This step is conditional on the deployment being triggered from the `master` branch.

Local Execution (Optional)
--------------------------


To test the deployment process locally, you can run the following commands:

.. code-block:: bash

    docker compose build
    docker compose up

After testing, you can manually redeploy your project on Render, or it will automatically redeploy on the next commit.
