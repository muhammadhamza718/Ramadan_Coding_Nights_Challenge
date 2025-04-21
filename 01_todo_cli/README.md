# 📝 Todo CLI

A powerful command-line interface application for managing tasks with advanced features like priorities, due dates, filtering, and statistics.

![Todo CLI](https://img.shields.io/badge/Todo%20CLI-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Click](https://img.shields.io/badge/Click-8.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **Task Management**: Add, list, complete, and remove tasks
- **Priority Levels**: Assign high, medium, or low priority to tasks
- **Due Dates**: Set due dates for tasks
- **Filtering**: View completed or pending tasks
- **Sorting**: Sort tasks by priority, due date, or creation date
- **Statistics**: View task completion statistics
- **Data Persistence**: Tasks are saved to a JSON file
- **Automatic Backups**: Backups are created before each save operation
- **Colored Output**: Enhanced readability with colored terminal output
- **Error Handling**: Robust error management for reliable operation

## 📋 Requirements

- Python 3.8 or higher
- Click
- Colorama

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/muhammadhamza718/Ramadan_Coding_Nights_Challenge/01_todo_cli.git
   cd 01_todo_cli
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python todo_list.py
   ```

## 💻 Usage

### Adding Tasks

```bash
# Add a simple task
python todo_list.py add "Buy groceries"

# Add a task with priority
python todo_list.py add "Pay bills" --priority high

# Add a task with due date
python todo_list.py add "Call mom" --due-date 2023-12-25

# Add a task with both priority and due date
python todo_list.py add "Submit report" --priority high --due-date 2023-12-31
```

### Listing Tasks

```bash
# List all tasks
python todo_list.py list

# List only completed tasks
python todo_list.py list --completed

# List only pending tasks
python todo_list.py list --pending

# Sort tasks by priority
python todo_list.py list --sort priority

# Sort tasks by due date
python todo_list.py list --sort due_date

# Sort tasks by creation date
python todo_list.py list --sort created_at
```

### Managing Tasks

```bash
# Mark a task as completed
python todo_list.py complete 1

# Remove a task
python todo_list.py remove 1
```

### Viewing Statistics

```bash
# Show task statistics
python todo_list.py stats

# Show application version
python todo_list.py version
```

## 🛠️ Development

The application is structured with the following components:

- `todo_list.py`: Main application file
- `requirements.txt`: Dependencies
- `README.md`: Documentation
- `todo.json`: Task storage file
- `todo.log`: Log file
- `backups/`: Directory for automatic backups

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Muhammad Hamza**

- GitHub: [@muhammadhamza718](https://github.com/muhammadhamza718)

## 🙏 Acknowledgments

- [Click](https://click.palletsprojects.com/) for the amazing CLI framework
- [Python](https://www.python.org/) for the programming language
- [Colorama](https://pypi.org/project/colorama/) for cross-platform colored output
- All contributors who have helped improve this project
