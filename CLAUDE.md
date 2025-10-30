# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flask web application for tracking cafes with information about wifi availability, power outlets, and coffee quality. Users can view existing cafes from CSV data and add new cafes via a web form.

## Development Setup

**Install dependencies:**
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
pip3 install -r requirements.txt
```

**Run the application:**
```bash
python main.py
```

The app runs in debug mode by default on `http://localhost:5000`.

## Architecture

**Data Flow:**
- Cafe data is stored in `cafe-data.csv` (7 columns: name, location, open, close, coffee, wifi, power)
- CSV data is read and converted to `CafeDataClass` instances on the `/cafes` route
- New cafes submitted via form are stored in-memory in `cafe_added` list (not persisted to CSV)
- Both CSV-loaded and form-submitted cafes are displayed together

**Key Components:**
- `main.py`: Flask app with 3 routes (home, add_cafe, cafes)
- `AddCafeForm.py`: WTForms form with validation (note: location field requires URL format)
- `CafeDataClass.py`: Dataclass for cafe data structure
- `templates/`: Jinja2 templates using Bootstrap5 styling
- `static/css/styles.css`: Dark theme styles

**Important Notes:**
- The app uses a hardcoded `SECRET_KEY` in `main.py:23` - should be moved to environment variable for production
- Added cafes are not persisted to CSV; they only exist in memory (`cafe_added` list) during app runtime
- Form submission on `/add` route doesn't redirect after success, causing potential duplicate submissions on refresh
