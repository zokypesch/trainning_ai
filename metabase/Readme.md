To set up Metabase with Docker, follow these steps:

1. **Install Docker**  
   Ensure Docker is installed on your system. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop).
   or to install Docker on Windows, follow these steps:

    ### **1. System Requirements**  
    Ensure your system meets these requirements:
    - Windows 10 (Pro, Enterprise, or Education) or Windows 11
    - Enable **Hyper-V** and **Containers** features (for Windows Pro/Enterprise)
    - WSL2 (Windows Subsystem for Linux 2) for Docker Desktop

    ---

    ### **2. Download Docker Desktop**  
    1. Go to the [Docker Desktop download page](https://www.docker.com/products/docker-desktop/).
    2. Download the Docker Desktop installer for Windows.

    ---

    ### **3. Install Docker Desktop**  
    1. Run the downloaded installer (`Docker Desktop Installer.exe`).
    2. Follow the installation wizard:
    - Accept the license agreement.
    - Ensure the options for **WSL 2** and **Hyper-V** are checked.
    3. Click **Install**.

    ---

    ### **4. Enable WSL 2** (if not already enabled)  
    1. Open PowerShell as Administrator.
    2. Run the following commands:

    - Enable the WSL feature:
        ```bash
        dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
        ```
    - Enable the Virtual Machine Platform:
        ```bash
        dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
        ```

    3. Set WSL 2 as the default version:
    ```bash
    wsl --set-default-version 2
    ```

    4. Download and install the [Linux kernel update package](https://aka.ms/wsl2kernel).

    ---

    ### **5. Start Docker Desktop**  
    1. Open Docker Desktop from the Start Menu.
    2. Complete the setup steps in the Docker Dashboard.

    ---

    ### **6. Verify the Installation**  
    Open PowerShell or Command Prompt and run:
    ```bash
    docker --version
    ```

    You should see the installed Docker version.

    ---

    Let me know if you need further assistance!

2. **Create a `docker-compose.yml` file**  
   Use the following configuration:

   ```yaml
   version: '3'
   services:
     metabase:
       image: metabase/metabase:latest
       container_name: metabase
       ports:
         - "3000:3000"
       environment:
         - MB_DB_FILE=/metabase-data/metabase.db
       volumes:
         - ./metabase-data:/metabase-data
   ```

3. **Steps to Run**  
   - Create a directory for the Metabase setup:
     ```bash
     mkdir metabase && cd metabase
     ```
   - Save the above `docker-compose.yml` file in this directory.
   - Start Metabase using Docker Compose:
     ```bash
     docker-compose up -d
     ```

4. **Access Metabase**  
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000). Follow the on-screen instructions to complete the setup.

Let me know if you encounter any issues!