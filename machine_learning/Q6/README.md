# How to Execute?

1. Open the terminal and move to project directory

    ```
    cd ./<path/to/project/directory>
    ```

2. Make sure you have docker installed. If not follow the following command

    1. If you're using a Debian-based distribution (such as Ubuntu), run the following command to install Docker:

        ```
        sudo apt install docker.io
        ```
    2. If you're using Snap, run the following command to install Docker:

        ```
        sudo snap install docker
        ```

3. Create a docker image with the following command

    ```
    docker build -t loan-prediction-app .
    ```

4. Run the Docker container:

    Once the Docker image is built, you can run the container using the following command:

    ```
    docker run -p 5000:5000 loan-prediction-app
    ```