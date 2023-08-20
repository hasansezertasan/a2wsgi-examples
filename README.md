# FastAPI Mount Examples

The goal of this project is to provide examples of how to mount sub applications written in different frameworks to FastAPI.

## Progress

| Framework   | Mount | Middleware  | Cookies | JWT   | Dependencies  |
| :---        | :---: | :---:       | :---:   | :---: | :---:         |
| Flask       |✅     |✅          |✅       |🔳    |🔳             |
| FastAPI     |✅     |🔳          |✅       |🔳    |🔳             |
| Django      |✅     |🔳          |🔳       |🔳    |🔳             |
| Starlette   |✅     |🔳          |🔳       |🔳    |🔳             |
| Tornado     |🔳     |🔳          |🔳       |🔳    |🔳             |
| Bottle      |🔳     |🔳          |🔳       |🔳    |🔳             |
| Robyn       |🔳     |🔳          |🔳       |🔳    |🔳             |
| GradIO      |✅     |🔳          |🔳       |🔳    |🔳             |
| PyWebIO     |✅     |🔳          |🔳       |🔳    |🔳             |
| NiceGUI     |🔳     |🔳          |🔳       |🔳    |🔳             |
| Reflex      |🔳     |🔳          |🔳       |🔳    |🔳             |
| Plotly Dash |🔳     |🔳          |🔳       |🔳    |🔳             |
| Streamlit   |🔳     |🔳          |🔳       |🔳    |🔳             |

## How to run

- Requirements
  - Docker
  - Docker Compose
- Steps
  1. Clone the repository
  2. Go to the project directory
  3. Run `docker-compose up --build`
  4. Go to `http://localhost:8000/docs` to see the API documentation
  5. Enjoy!

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Authors

- [hasansezertasan](https://www.github.com/hasansezertasan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
