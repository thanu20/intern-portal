Intern Portal Dashboard 🎓💼

This is a basic Full Stack Intern Portal built as part of a Full Stack Developer Internship Task. It helps interns view their referral code, track the total donations they’ve raised, and view reward milestones. It is built using **HTML, CSS, JavaScript** for the frontend and **Python Flask** for the backend.



✨ Features

* Welcome banner with intern name
* Dynamic referral code display
* Live donations counter fetched from backend
* Reward milestones (₹5000 - Bronze, ₹10000 - Silver, ₹20000 - Gold)
* Simple and responsive design



🔧 Technologies Used

Frontend:

* HTML5
* CSS3
* JavaScript

Backend:

* Python 3
* Flask
* Flask-CORS


🖥️ How to Run This Project Locally

1. Clone the Repository

Open your terminal and run:

bash
git clone https://github.com/thanu20/intern-portal.git
cd intern-portal


 2. Set Up and Run Backend

bash
cd backend/intern_task
python -m venv venv         # Create virtual environment
venv\Scripts\activate       # Activate it (Windows)

pip install flask flask-cors
python app.py


 This will start the backend server at:
  👉 [http://127.0.0.1:5000/api/user](http://127.0.0.1:5000/api/user)


3. Open Frontend

 Go to the folder: `frontend`

 Right-click on `index.html` and open it in your browser
  (Or use a Live Server extension in VS Code)

 The dashboard will fetch data from your backend and display it!

📂 Folder Structure
intern-portal/
│
├── frontend/
│   └── index.html
│   └── style.css
│   └── script.js
│
├── backend/
│   └── intern_task/
│       └── app.py
│
└── README.md

📸 Project Screenshot

![Screenshot](screenshot.png)

GitHub Repository:
[https://github.com/thanu20/intern-portal](https://github.com/thanu20/intern-portal)

🙋‍♀️ About Me
Hi! I’m Linganaboina Thanuja, a Computer Science student passionate about web development and learning full-stack skills.
This is my full-stack mini project and it was really exciting to build! 

📬 Feedback

If you have suggestions or spot any issues, feel free to open an issue or drop feedback.

