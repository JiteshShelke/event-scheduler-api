"""
Event Scheduler System - Flask REST API

Features:
- Create, Read, Update, Delete events
- Search events by title or description
- Persistent storage using JSON file

Author: Jitesh Shelke
"""

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'events.json'

def load_events():
    """
    Load events from the JSON file.
    Returns:
        list: List of events
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_events(events):
    """
    Save events to the JSON file.
    Args:
        events (list): List of events to save
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

@app.route('/events', methods=['GET'])
def get_events():
    """
    Get all events sorted by start_time.
    Returns:
        JSON: List of events
    """
    events = load_events()
    events.sort(key=lambda x: x['start_time'])
    return jsonify(events), 200

@app.route('/events', methods=['POST'])
def create_event():
    """
    Create a new event.
    Returns:
        JSON: Created event data or error
    """
    events = load_events()
    data = request.get_json()
    
    required = ['title', 'description', 'start_time', 'end_time']
    if not data or not all(k in data for k in required):
        return jsonify({'error': 'Missing fields. Required: title, description, start_time, end_time'}), 400
    
    event_id = events[-1]['id'] + 1 if events else 1
    data['id'] = event_id
    events.append(data)
    save_events(events)
    return jsonify({'message': 'Event created', 'event': data}), 201

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """
    Update an existing event by ID.
    Returns:
        JSON: Updated event data or error
    """
    events = load_events()
    data = request.get_json()
    
    for event in events:
        if event['id'] == event_id:
            event.update(data)
            save_events(events)
            return jsonify({'message': 'Event updated', 'event': event}), 200
    return jsonify({'error': f'Event with id {event_id} not found'}), 404

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Delete an event by ID.
    Returns:
        JSON: Success message or error
    """
    events = load_events()
    updated_events = [event for event in events if event['id'] != event_id]
    
    if len(events) == len(updated_events):
        return jsonify({'error': f'Event with id {event_id} not found'}), 404
    
    save_events(updated_events)
    return jsonify({'message': f'Event with id {event_id} deleted'}), 200

@app.route('/events/search', methods=['GET'])
def search_events():
    """
    Search events by title or description using query param 'q'.
    Returns:
        JSON: List of matching events or error
    """
    query = request.args.get('q', '').lower()
    events = load_events()
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required for search'}), 400
    
    results = [event for event in events if query in event['title'].lower() or query in event['description'].lower()]
    
    return jsonify({'results': results, 'count': len(results)}), 200

# Health check route (Extensibility example)
@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    Returns:
        JSON: Status message
    """
    return jsonify({'status': 'Event Scheduler API is running'}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
