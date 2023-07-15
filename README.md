# FastAPI Boilerplate

This is a simple FastAPI boilerplate project with a health check and hello world endpoint.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure that you have the following installed on your local machine:

- Python 3.10+
- pip

### Installation & Usage

Clone the repository:

```bash
git clone https://github.com/username/project.git
cd project
```
Create a virtual environment and activate it:


```
python3 -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
```
Install the necessary packages:
```
pip install -r requirements.txt
```
Start the server:
```
uvicorn app.main:app --reload
```
or
```
pythom -m app.main
```

This will start the server at http://localhost:8000.   
You can interact with the API directly using a tool like curl or Postman, or you can view the automatic interactive API documentation at http://localhost:8000/docs.

## Endpoints

This FastAPI boilerplate has the following endpoints:

- `/health` - Health check endpoint returning the status of the application.
- `/hello` - Returns a Hello World message.

## Testing


## Built With
FastAPI - The web framework used


# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate. For larger changes, please open an issue first to discuss what you would like to change.


## License

This project is licensed under the MIT License

## Acknowledgments

- Thanks to [tiangolo](https://github.com/tiangolo) for creating FastAPI, a high-performance, easy-to-learn, and fast-to-code framework for building web APIs.
- Hat tip to anyone whose code was used or inspired the creation of this project.
