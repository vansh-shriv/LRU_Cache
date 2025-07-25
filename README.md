# LRU Cache Simulator (Python + Flask)

A fully functional **Least Recently Used (LRU) Cache Simulator** built in Python using a custom data structure and served via a web interface using **Flask** and **Tailwind CSS**.

> Designed for interviews, CS fundamentals, and memory management simulation.

---

##  Features

- ✅ **LRU Cache core logic** implemented using `Doubly Linked List` + `HashMap`
- ✅ Command-line interface (CLI) to simulate put/get/cache operations
- ✅ Dynamic cache capacity setting
- ✅ **Responsive Flask web app**
<!-- - ✅ Beautiful display of current cache contents --> [in Progress]
- ✅ Reusable Python module structure (`lru.py`, `cli.py`, `app.py`)
- ✅ Beginner-friendly and fully modular code

---

## 🧠 How LRU Works

- Accessed or inserted keys move to the **most recently used** (end of DLL).
- If capacity is full, the **least recently used** key (front of DLL) is evicted.
- `O(1)` for both `.get()` and `.put()` operations using efficient data structures.

---

## 🏗️ Folder Structure
LRU-Cache-Simulator/
├── app.py # Flask Web Application
├── cli.py # Command Line Interface
├── lru.py # LRU Cache Logic
├── templates/
│ └── index.html # Web UI (Stitch + Tailwind)
├── static/ # Optional for custom assets
├── tests.py # Unit tests (coming soon)
└── README.md # Project documentation



---

## ⚙️ Setup Instructions

### 1. Clone and Install

git clone https://github.com/your-username/LRU-Cache-Simulator.git
cd LRU-Cache-Simulator
pip install flask

### 2. Run the Flask App
python app.py
Then open your browser at [PORT] which its running 

### 3. Run via CLI (optional)
python cli.py init 3{capacity}
python cli.py put 1 100
python cli.py get 1
python cli.py cache



🧪 Tech Stack

Python 3
Flask
Tailwind CSS (via CDN)
Google Stitch UI (exported HTML)
Jinja2 for dynamic HTML rendering


📦 Future Scope
Ideas to extend this project into a more powerful tool:

🔁 LFU Cache Support (Least Frequently Used) with frequency-count eviction.
📊 Graphs showing cache hits and misses over time.
☁️ Export simulation logs to CSV or JSON.
👤 User-based sessions and analytics.
🧪 Add PyTest-based test coverage.

👨‍💻 Author
vansh_shriv – GitHub
Made for strengthining CS fundamentals 