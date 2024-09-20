# Retrieval-Augmented Generation (RAG) System

This project implements a Retrieval-Augmented Generation (RAG) system using Python. It processes text data from various sources, including CSV files and PDFs, to create embeddings and store them in a vector store for efficient retrieval. The system leverages the `langchain` library for text splitting and embedding, and `Chroma` for vector storage.

## Key Features

- **Text Splitting**: Divides text into manageable chunks for embedding.
- **Embeddings**: Generates text embeddings using the nomic-embed-text model.
- **Vector Store**: Stores and retrieves embeddings using Chroma.
- **Interactive Q&A**: Allows users to ask questions and get responses based on the stored embeddings.

## Overview
Content Machine AI is an intelligent content generation and social media analytics system built with Retrieval-Augmented Generation (RAG). It transforms social media profile analytics from CSV files into valuable insights, enabling users to automate content creation and understand engagement trends with precision.

### Text Splitting

Divides large text data into manageable chunks to create effective embeddings.

### Embeddings

Generates text embeddings using the `nomic-embed-text` model for accurate and meaningful representations of the text data.

### Vector Store

Utilizes Chroma to store and retrieve embeddings, enabling efficient and fast searches within the text data.

### Interactive Q&A

Provides an interface for users to ask questions and receive responses based on the stored embeddings, enhancing the retrieval of relevant information from large text datasets.

### LangWatch Integration
LangWatch dashboard for monitoring and observability.

## Pre-Conditions

1. **Ensure that Ollama is installed on your laptop.**
2. **Ensure `llama3` model is installed using Ollama.**
3. **Ensure that you install `nomic-embed-text` using Ollama.** Run the command:
   ```bash
   ollama run nomic-embed-text
   ```

## Installation

Install `pipenv` to add all the project dependencies.

To install packages using `pipenv`, follow these steps:

1. **Install `pipenv` if you haven't already:**
   ```bash
   pip install pipenv
   ```

2. **Create a `Pipfile` if you don't have one yet:**
   ```bash
   pipenv install
   ```

3. **Install the necessary packages using `pipenv`:**
   ```bash
   pipenv install <package-name>
   ```

This will add the packages to your `Pipfile` and create a `Pipfile.lock` to ensure reproducible builds.

## Example Commands

After running these commands, your `Pipfile` should include the installed packages, and you can use `pipenv shell` to activate the virtual environment.

## Development Environment

The project has been created in PyCharm. If you have PyCharm, you should be able to directly run this code much more easily.