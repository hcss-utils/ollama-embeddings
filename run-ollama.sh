#!/usr/bin/env bash

ollama serve &
ollama list
ollama pull nomic-embed-text

ollama serve &
ollama list
ollama pull llama3.1:8b-instruct-q4_0
