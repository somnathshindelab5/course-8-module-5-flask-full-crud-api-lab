# Event Management API

This Flask application provides a simple RESTful API for managing events. It uses an in-memory list of Event objects to simulate a lightweight database and supports creating, updating, and deleting events.

## Routes

- POST /events - Create a new event
- PATCH /events/<id> - Update an existing event title
- DELETE /events/<id> - Remove an event

## Example Requests and Responses

### Create an event

Request:

```bash
curl -X POST http://localhost:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon"}'
```

Response:

```json
{"id": 3, "title": "Hackathon"}
```

### Update an event

Request:

```bash
curl -X PATCH http://localhost:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon 2025"}'
```

Response:

```json
{"id": 1, "title": "Hackathon 2025"}
```

### Delete an event

Request:

```bash
curl -X DELETE http://localhost:5000/events/2
```

Response:

```text
204 No Content
```

## Notes

- The API returns JSON responses with `jsonify()`.
- Successful creation returns `201 Created`.
- Successful updates return `200 OK`.
- Successful deletion returns `204 No Content`.
- Missing events return `404 Not Found` and a helpful error message.
