#!/usr/bin/env bash

ollama serve &
ollama list
ollama pull nomic-embed-text

ollama serve &
ollama list
ollama pull qwen2.5:7b-instruct-q5_K_S
