# FitBuddy-AI-Fitness-Generator
FitBuddy is an AI-powered web application that generates personalized 7-day workout plans based on user fitness goals. The application uses FastAPI for the backend and integrates Google's Gemini AI model to create customized fitness routines.


Introduction

FitBuddy is an AI-powered web application designed to help users generate personalized fitness plans. Many people struggle to create structured workout routines that match their fitness goals. FitBuddy solves this problem by using generative AI to create customized workout suggestions based on the user’s information.
The application collects basic fitness details such as age, weight, fitness goals, and workout intensity. Based on these inputs, the system generates a personalized 7-day workout plan using a generative AI model. The project is developed using FastAPI for the backend and integrates Google's Gemini AI model for intelligent plan generation.

*Pre-requisites

Before running the FitBuddy application, certain software and tools need to be installed. Python is required as the main programming language for the project. A virtual environment is recommended to manage dependencies and avoid conflicts between different Python libraries.
The backend of the application is built using FastAPI, which allows efficient handling of user requests and API communication. Additionally, the Gemini AI API is used to generate fitness recommendations. Other required libraries are installed through a requirements file to ensure smooth project setup.

*Project Workflow

The workflow of FitBuddy begins when the user opens the web application and enters their fitness details. These details may include information such as age, weight, fitness goals, and preferred workout intensity.
Once the user submits the form, the input data is sent to the FastAPI backend. The backend processes the information and prepares a prompt that is sent to the Gemini AI model. The AI model analyzes the request and generates a personalized workout plan.

After generating the response, the AI sends the result back to the backend, which then forwards it to the frontend interface. The generated fitness plan is finally displayed to the user in an easy-to-read format.

 *Model Selection and Architecture

[Research and Select the Appropriate Generative AI Model]

For the FitBuddy project, different generative AI models were explored to determine which one would best suit the application’s requirements. The main goal was to select a model capable of generating meaningful and structured workout plans based on user input.

Google’s Gemini AI model was selected because it provides powerful natural language generation capabilities and integrates smoothly with Python applications. It can generate detailed responses and adapt the workout plans according to different user goals such as weight loss, muscle gain, or general fitness improvement.

[ Define the Architecture of the Application]

The FitBuddy application follows a simple and efficient client-server architecture. The system is divided into three main components: the frontend, the backend, and the AI processing layer.

The frontend is responsible for interacting with the user and collecting input information through a web form. The backend, built using FastAPI, processes the user input and manages communication between the frontend and the AI model.

The AI processing layer uses the Gemini AI model to generate personalized fitness plans. Once the plan is generated, it is sent back through the backend and displayed on the user interface.

*Core Functionalities Development
[Develop the Core Functionalities]

The main functionality of FitBuddy is to generate personalized fitness plans using artificial intelligence. The system collects user data such as age, weight, fitness goals, and workout preferences. This data is then converted into a structured prompt that is sent to the AI model.

The AI processes the request and generates a detailed workout routine tailored to the user's needs. This allows users to receive customized fitness guidance without manually planning their routines.

[Implement the FastAPI Backend]

FastAPI is used to build the backend of the FitBuddy application. The backend is responsible for managing routes, processing user input, and communicating with the AI model.

When the user submits their fitness information, FastAPI receives the request and sends it to the AI model for processing. After receiving the AI-generated response, the backend sends the result back to the frontend so that it can be displayed to the user.

*routes.py Development

The routes.py file is responsible for managing the different routes used in the application. These routes define how the application responds to different user requests.

For example, one route may load the home page of the application, while another route processes the user's fitness information and generates a workout plan. By organizing the routing logic in a separate file, the code remains clean and easier to maintain.

*Frontend Development

[Designing and Developing the User Interface]

The user interface of FitBuddy is designed to be simple and easy to use. The frontend allows users to enter their fitness details through a structured form. The goal of the design is to ensure that users can easily understand how to use the application and quickly generate their fitness plans.

HTML and CSS are used to build the interface, providing a clean layout and clear navigation.

[Creating Dynamic Templates with Jinja2]

Jinja2 templates are used to dynamically display the results generated by the AI model. When the backend receives the fitness plan from the AI model, it sends the data to the template.

The template then renders the workout plan on the results page, allowing users to see their personalized fitness routine immediately after submitting their information.

*Deployment
[Preparing the Application for Local Deployment]

Before deployment, all necessary dependencies are installed using the requirements file. A virtual environment is also configured to manage project libraries efficiently.

The FastAPI server is then started using Uvicorn, which runs the application locally.

[Testing and Verifying Local Deployment]

After starting the server, the application is accessed through a web browser using the local host address. Users can test the application by entering their fitness details and verifying whether the generated workout plan appears correctly.

This step ensures that all components of the application are functioning properly.

*How to Run the Project

1. Clone the repository
git clone <repository-link>

2. Install dependencies
pip install -r requirements.txt

3. Run the FastAPI server
uvicorn app:app --reload

4. Open the application in the browser
http://127.0.0.1:8000

*Conclusion

The FitBuddy project demonstrates how generative AI can be used to simplify fitness planning. By integrating FastAPI with the Gemini AI model, the application can automatically generate personalized workout plans based on user input.

The project highlights the potential of AI-driven solutions in improving accessibility to fitness guidance and helping users maintain a structured workout routine.

