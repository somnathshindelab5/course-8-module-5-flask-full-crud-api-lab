from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


@app.route("/events", methods=["POST"])
def create_event():
    # Accept JSON input and validate that it contains a title.
    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Create a new event with the next available ID.
    new_event_id = max(event.id for event in events) + 1 if events else 1
    new_event = Event(new_event_id, title)
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Find the event by ID and update its title.
    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    for event in events:
        if event.id == event_id:
            event.title = title
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Remove the matching event from the in-memory list.
    for index, event in enumerate(events):
        if event.id == event_id:
            del events[index]
            return "", 204

    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
