# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## CLISIPY-1.0 - 2026-07-08

### Added

- **Multi-language Support**: Convert pseudocode to 25+ programming languages including Python, C++, C, Java, Ruby, C#, PHP, Rust, Go, Lua, Swift, Kotlin, Dart, GDScript, JavaScript, Zig, Julia, F#, and Cython
- **AI-Powered Code Generation**: Integration with Groq API and Llama 3.3 70B model for accurate and intelligent pseudocode-to-code conversion
- **Command-Line Interface**: Simple and intuitive CLI tool for converting pseudocode files to executable code
- **Clean Code Output**: Generates production-ready code without markdown formatting or unnecessary additions
- **Language Validation**: Automatic verification that output file extensions match the specified programming language
- **Best Practices Compliance**: Generated code follows current standards and modern practices for each supported language
- **Memory Management Awareness**: Special handling and optimization for low-level languages without garbage collection
- **Error Handling**: Comprehensive error detection and user-friendly error messages for:
  - Missing or invalid input files
  - Incorrect file formats
  - Language validation failures
  - API connection issues and rate limiting
  - Timeout and status errors
- **Environment Variable Management**: Secure API key handling using `.env` file configuration
- **Rich Terminal Output**: Enhanced terminal formatting with color-coded messages and styling
- **Comprehensive Documentation**: Detailed README with installation instructions, usage examples, and project overview

### Features

- Input validation for pseudocode files (`.txt` format, non-empty verification)
- Support for both Git clone and ZIP download installation options
- Detailed system prompts that guide AI to produce:
  - Clean and modern code
  - Proper library imports
  - Avoidance of hallucinations
  - Prevention of legacy code patterns
  - Memory-safe implementations for low-level languages
- Flexible pseudocode-to-multiple-languages workflow

### Technical Highlights

- Modular architecture with separate concerns:
  - `app.py` - Application entry point
  - `run.py` - Workflow orchestration
  - `ai_helpers.py` - Groq API integration
  - `file_helpers.py` - File I/O operations
  - `language_file_helpers.py` - Language and file validation
  - `system_prompt.py` - AI instruction generation
  - `write_code.py` - Code output handling
- Robust exception handling for API interactions
- Case-insensitive language name matching
- Extension-based language identification

For more information, visit [CLISIPY on GitHub](https://github.com/Anas-AbdelRaoof/CLISIPY)
