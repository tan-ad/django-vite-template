# ✨ Django + Vite + Vue SPA Template ✨

A template for building modern web applications using Django as the backend API and Vue.js (managed by Vite) as the frontend Single Page Application (SPA), running in a containerized Docker development environment.

This template provides a solid foundation with:

*   **Decoupled Architecture:** Separate backend (Django) and frontend (Vue/Vite) codebases.
*   **Fast Development:** Vite's lightning-fast HMR (Hot Module Replacement) for frontend development.
*   **Robust Backend:** Django & Django REST Framework for building APIs, handling authentication, and database interactions.
*   **Containerized Dev Environment:** Consistent setup using Docker and Docker Compose.

---

## ⚙️ Technology Stack

*   **Backend:**
    *   Python 3.13+
    *   Django 5.1+
    *   Django REST Framework
    *   `django-environ` (Environment variables)
    *   `django-cors-headers` (CORS handling)
    *   `django-vite` (Vite integration)
    *   SQLite (Default development DB)
*   **Frontend:**
    *   Node.js / npm
    *   Vue.js 3
    *   Vite
    *   `vue-router` (Client-side routing)
    *   `axios` (HTTP client)
*   **Development Environment:**
    *   Docker
    *   Docker Compose

---

## 📁 Project Structure

django-vite-template/ <-- Git repository root
├── backend/ <-- Django project root (BASE_DIR)
│ ├── django_vite_template/ <-- Django settings/config directory
│ │ ├── init.py
│ │ ├── settings.py <-- Main settings (uses django-environ)
│ │ ├── urls.py <-- Main URL routing (includes API, Admin, SPA catch-all)
│ │ ├── views.py <-- Contains index_view for SPA shell
│ │ └── ... (wsgi.py, asgi.py)
│ ├── api/ <-- Example Django app for API endpoints
│ │ ├── models.py
│ │ ├── views.py <-- API Views (e.g., PingView)
│ │ ├── urls.py
│ │ └── ...
│ ├── users/ <-- Custom Django user app (example)
│ ├── templates/ <-- Django templates
│ │ └── base.html <-- Main entry HTML shell (uses django-vite tags)
│ ├── frontend_dist/ <-- Vite build output directory (TARGET, gitignored)
│ ├── manage.py
│ ├── requirements.txt <-- Python dependencies
│ ├── Dockerfile <-- Backend Docker instructions
│ └── .env.example <-- Example environment file (Copy to .env)
│
├── frontend/ <-- Vue/Vite project root
│ ├── public/
│ ├── src/
│ │ ├── assets/
│ │ ├── components/ <-- (Optional: Add shared Vue components)
│ │ ├── views/ <-- Vue route components (HomeView.vue, etc.)
│ │ ├── router/ <-- Vue Router configuration
│ │ ├── services/ <-- API service module (api.js)
│ │ ├── App.vue <-- Main Vue component shell
│ │ └── main.js <-- Vue app entry point
│ ├── index.html <-- Vite's source HTML (not directly used by Django)
│ ├── package.json <-- Node dependencies & scripts
│ ├── vite.config.js <-- Vite configuration (proxy, build output)
│ ├── Dockerfile <-- Frontend Docker instructions
│ └── node_modules/ <-- (gitignored)
│
├── venv/ <-- Python virtual environment (gitignored)
├── .dockerignore <-- Files to ignore for Docker builds
├── .gitignore
├── docker-compose.yml <-- Docker Compose configuration for development
└── README.md <-- This file


---

## 🚀 Getting Started (Development)

This project uses **Docker Compose** for a consistent development environment. Follow the steps below to get the application running. Optional steps are included for enhancing your local IDE experience.

### Prerequisites

*   [Git](https://git-scm.com/)
*   [Docker Engine](https://docs.docker.com/engine/install/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Often included with Docker Desktop)
*   [Python 3.13+](https://www.python.org/) (Required if setting up local venv for IDE)
*   [Node.js and npm](https://nodejs.org/) (Required if setting up local Node modules for IDE)

### Setup & Running with Docker (Primary Method)

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd django-vite-template
    ```

2.  **Create Backend Environment File (`.env`):**
    The backend requires environment variables for configuration, especially secrets.
    *   Navigate to the backend directory: `cd backend`
    *   Copy the example environment file: `cp .env.example .env`
    *   **Generate a SECRET_KEY:** The default `.env.example` has a placeholder. Generate a new, secure key using Django's utility. If you have Python installed locally:
        ```bash
        # Ensure you are in the 'backend' directory
        python manage.py shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        ```
        (If you don't have Python locally yet, you can temporarily comment out the `env_file` line in `docker-compose.yml`, run `docker-compose run --rm backend python manage.py shell -c '...'`, copy the key, uncomment `env_file`, and then proceed).
    *   **Edit `.env`:** Open the newly created `backend/.env` file and **replace** the placeholder value for `SECRET_KEY` with the key you just generated. Review other variables – the defaults in `.env.example` are generally suitable for Docker development.
    *   Navigate back to the project root: `cd ..`

3.  **Build and Run Containers:**
    From the project root directory (where `docker-compose.yml` is located):
    ```bash
    docker-compose up --build
    ```
    *   This builds the Docker images (installing Python and Node dependencies *inside* the images) and starts the `backend` and `frontend` containers.
    *   Your local code is mounted into the containers for live updates.
    *   Logs from both containers will appear in your terminal.

4.  **Access the Application:**
    Once both containers show they are running successfully, open your web browser:
    ➡️ **`http://localhost:8000`**

5.  **Stopping:** Press `Ctrl+C` in the terminal running `docker-compose`. To remove containers, use `docker-compose down`.

---

## 💻 IDE Integration & Local Tooling (Optional)

While Docker runs the application, installing dependencies locally can significantly improve your IDE experience (autocompletion, linting, debugging hints). **These steps are optional and do not affect how the application runs via Docker.**

### Backend (Python/Django)

1.  **Ensure Prerequisites:** Python 3.13+ installed locally.
2.  **Navigate:** `cd backend`
3.  **Create & Activate venv:**
    ```bash
    python -m venv venv
    # Activate (use appropriate command for your OS - see below)
    source venv/bin/activate # Linux/macOS/Git Bash
    # venv\Scripts\activate.bat # Windows Cmd
    # venv\Scripts\Activate.ps1 # Windows PowerShell
    ```
4.  **Install Dependencies:**
    ```bash
    # Ensure venv is active
    pip install -r requirements.txt
    ```
5.  **IDE Configuration:** Configure your IDE (e.g., VS Code with the Python extension) to use the Python interpreter from `./venv/bin/python` (or `.\venv\Scripts\python.exe`). This enables features like IntelliSense, Go to Definition, linting (Flake8/Pylint), and formatting (Black/isort) based on the installed packages.

### Frontend (Node.js/Vue)

1.  **Ensure Prerequisites:** Node.js and npm installed locally.
2.  **Navigate:** `cd frontend`
3.  **Install Dependencies:**
    ```bash
    npm install
    ```
4.  **IDE Configuration:** This allows your IDE (e.g., VS Code with Volar/Vue extensions, ESLint, Prettier extensions) to provide accurate autocompletion for Vue and JavaScript, run linters, format code, and perform type checking based on the locally installed `node_modules`.

**Key Takeaway:** The local `venv/` and `frontend/node_modules/` directories created by these optional steps are primarily for your IDE's benefit on your host machine. The Docker containers use the dependencies installed *during their image build* process.

---

## 🔑 Key Configuration Files

*   **`backend/.env`**: (Created from `.env.example`) Stores Django environment variables. **DO NOT COMMIT.**
*   **`backend/.../settings.py`**: Main Django settings (loads from `.env`).
*   **`frontend/vite.config.js`**: Vite config (proxy, build).
*   **`docker-compose.yml`**: Development service definitions.
*   **`backend/Dockerfile` & `frontend/Dockerfile`**: Image build instructions.

---

## ❗ Production Considerations

**This setup is for DEVELOPMENT ONLY.** Deploying requires changes:

1.  **Django:** `DEBUG=False`, secure `SECRET_KEY`, production `ALLOWED_HOSTS`/`CORS`, `DJANGO_VITE_DEV_MODE=False`, production DB, HTTPS settings.
2.  **Frontend:** Run `npm run build`.
3.  **Server:** Use Gunicorn/uWSGI + Nginx.
4.  **Static Files:** Run `collectstatic`, serve via Nginx.
5.  **Docker:** Multi-stage builds, remove dev volumes, secure secrets.

---

Happy Coding! 🚀
