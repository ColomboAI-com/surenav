# Contributing to SureNav

Thank you for your interest in contributing to SureNav!

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/surenav.git
cd surenav
pip install -e ".[dev]"
playwright install chromium
```

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Follow PEP 8
- Use Black for formatting: `black src/`
- Run linting: `flake8 src/ --max-line-length=120`

## Pull Request Guidelines

- Update documentation for new features
- Add tests for bug fixes and new features
- Ensure all tests pass
- Keep commits focused and atomic

## Reporting Issues

- Use GitHub Issues
- Include reproduction steps
- Provide system information (OS, Python version)
- Include error messages and logs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
