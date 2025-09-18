# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is an **Interactive Food Search and RAG Chatbot System** that uses vector similarity search to recommend food items based on natural language queries. The system combines ChromaDB for vector storage, SentenceTransformers for embeddings, and a structured food dataset to provide an intelligent food recommendation experience via a command-line interface.

## Architecture

### Core Components

- **`interactive_search.py`** - Main CLI application entry point with interactive chatbot interface
- **`shared_functions.py`** - Core RAG functionality including data loading, collection management, and similarity search
- **`FoodDataSet.json`** - Rich food dataset with nutritional information, ingredients, and metadata
- **`smoke_test.py`** - Dependency verification script

### Technology Stack

- **Vector Database**: ChromaDB with HNSW index using cosine similarity
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2 model)
- **Data Processing**: NumPy, SciPy for numerical operations
- **AI Integration**: IBM Watson AI SDK for potential LLM integration
- **Environment Management**: python-dotenv for configuration

### RAG Architecture Flow

1. **Data Ingestion**: JSON food data is loaded and normalized with required fields
2. **Embedding Generation**: Food descriptions are converted to vector embeddings using comprehensive text representations (name, description, ingredients, cuisine type, cooking method, taste profile, health benefits, nutrition)
3. **Vector Storage**: ChromaDB collection stores embeddings with rich metadata for filtering
4. **Query Processing**: User queries are embedded and matched against the food database
5. **Result Ranking**: Similarity scores are calculated and results are formatted with comprehensive metadata

## Development Commands

### Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### Testing and Validation

```bash
# Verify all dependencies are installed correctly
python smoke_test.py

# Run the interactive food search system
python interactive_search.py
```

### Development Workflow

```bash
# Deactivate virtual environment when done
deactivate

# Check Python and package versions
python --version
python smoke_test.py
```

## Key Implementation Details

### Data Structure

The food dataset uses a rich JSON schema with these key fields:
- `food_id`, `food_name`, `food_description`
- `food_ingredients` (array), `cuisine_type`, `cooking_method`
- `food_calories_per_serving`, `food_nutritional_factors`
- `food_health_benefits`, `food_features` (taste, texture, appearance)

### Search Functionality

- **Basic Similarity Search**: `perform_similarity_search()` - semantic search across all food items
- **Filtered Search**: `perform_filtered_similarity_search()` - search with cuisine and calorie constraints
- **Collection Management**: Automatic deduplication with unique ID generation
- **Rich Text Embedding**: Combines multiple food attributes into comprehensive search text

### Interactive Features

- Real-time CLI-based food recommendations
- Similarity scoring with percentage display
- Related search suggestions based on cuisine types and calorie ranges
- Error handling and user guidance for improved search queries

## Code Organization

- **Separation of Concerns**: UI logic in `interactive_search.py`, core RAG functionality in `shared_functions.py`
- **Error Handling**: Comprehensive exception handling throughout the search pipeline
- **Type Hints**: Full type annotations for better code maintainability
- **Modular Design**: Reusable functions for collection creation, data population, and search operations

## Environment Variables

The system supports `.env` files for configuration (loaded via python-dotenv). Likely used for IBM Watson AI API keys and other sensitive configurations.
